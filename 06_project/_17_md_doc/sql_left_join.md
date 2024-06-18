# 从left join的坑谈sql解析器的编程思想

请看案例：

有两张表，t_sin_req_res, t_sin_req_detail,第二张表是第一张的副表，和第一张表有一对一的关系。
两张表靠request_id这个key进行关联。

生产上每天大概有700万的数据产生在两张表中。因此两张表按天分区了。

现在想找出某一天只在第一张表中有，而第二张表中没有的数据。

left join。。。

~~~sql
select
	sr.id, sr.request_id, sd.request_id, sd.dd_type 
from
	app_vendor.t_sin_req_res sr
left join
	app_vendor.t_sin_req_detail sd 
on
	sr.request_id = sd.request_id
where
	sr.cdate between '2024-04-26'::timestamp and '2024-04-27'::timestamp
	and sd.cdate between '2024-04-26'::timestamp and '2024-04-27'::timestamp
	and sd.request_id is null
~~~

很奇怪，结果是找不到。

甚至于，我都知道是哪一条：

~~~sql
select * from app_vendor.t_sin_req_res sr where sr.id = 43152100;
~~~

没办法，用not exists试试吧，总感觉从语义上来讲，not exits更容易理解

~~~sql
select
	sr.id
from
	app_vendor.t_sin_req_res sr
where
	sr.cdate >= '2024-01-01'::timestamp
	and not exists(
	select
		1
	from
		app_vendor.t_sin_req_detail sd
	where
		sd.cdate >= '2024-01-01'::timestamp
		and sd.request_id = sr.request_id 
    );
~~~

ok，终于找到了。

什么原因呢？

其实，left join改一下也能找出来。
~~~sql
select
	sr.id, sr.request_id, sd.request_id, sd.dd_type 
from
	app_vendor.t_sin_req_res sr
left join
	app_vendor.t_sin_req_detail sd 
on
	sr.request_id = sd.request_id
	and sd.cdate between '2024-04-26'::timestamp and '2024-04-27'::timestamp
where
	sr.cdate between '2024-04-26'::timestamp and '2024-04-27'::timestamp
	and sd.request_id is null
~~~

**差异就是把对第二张表的时间区间的条件从where里挪到了on里了。**

官方的回答是

> left join中被连接的表的过滤条件，如果写到了 where 的后面，  left join会失效， 变成 inner join 



其实，官方的回答很恶心，让人更加的不明白，只靠脑子硬记忆，是没什么用的。这就是个**sql的语法树解析顺序**问题。

~~~
sql解析器是先解析where条件，尽量把两个表缩小，然后再判断from中两个表的关联关系

而不是先解析from建立好关联关系，然后再从结果集上用where缩表

不然，先解析from，如果是笛卡尔积关联，那就先疯掉了。好不容易疯完了，再看where条件，就要一条。哭都找不到坟头。
~~~

