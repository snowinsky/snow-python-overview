# JQuery 扫盲

> jquery 是一个js库，提供了操作html（元素，事件，dom），css，javascript，ajax等方式
> 
> https://www.runoob.com/manual/jquery/

## jquery基本语法
$(selector).action() # 先用selector选取html元素，然后执行action动作

例如：
- $(this).hide() 隐藏当前元素
- $("p").hide() 隐藏所有的p文字段
- $("p.test").hide() - 隐藏所有 class="test" 的 <p> 元素
- $("#test").hide() - 隐藏 id="test" 的元素
- $(document).ready(function(){  //方法体 });
- $(function(){  //方法体 }); 上一个的简化写法

### selector
~~~
- $(document) 当前html页面
- $(this) 当前元素
- $("button") 当前html页面中的所有的button元素
- $("#test") 相当于document.getElementById
- $(".test") 相当于选取所有的class='test'的元素
- $("*")	选取所有元素	在线实例
- $(this)	选取当前 HTML 元素	在线实例
- $("p.intro")	选取 class 为 intro 的 <p> 元素	在线实例
- $("p:first")	选取第一个 <p> 元素	在线实例
- $("ul li:first")	选取第一个 <ul> 元素的第一个 <li>
- $("ul li:first-child")	选取每个 <ul> 元素的第一个 <li> 元素	在线实例
- $("[href]")	选取带有 href 属性的元素	在线实例
- $("a[target='_blank']")	选取所有 target 属性值等于 "_blank" 的 <a> 元素	在线实例
- $("a[target!='_blank']")	选取所有 target 属性值不等于 "_blank" 的 <a> 元素	在线实例
- $(":button")	选取所有 type="button" 的 <input> 元素 和 <button> 元素	在线实例
- $("tr:even")	选取偶数位置的 <tr> 元素	在线实例
- $("tr:odd")	选取奇数位置的 <tr> 元素
~~~

### action

~~~
鼠标事件	        
click 按钮或者链接被按下  	
dblclick 双击
mouseenter	当鼠标指针穿过元素    
mouseleave	    当鼠标指针离开元素
hover	 光标悬停

键盘事件	
keypress
keydown	
keyup	
blur	元素失去焦点

表单事件
submit
change
focus 元素获得焦点
unload 

文档/窗口事件
load
resize
scroll
ready 页面全都加载完之后执行

~~~

### jquery自有动作

- $(selector).hide(speed,callback);
$(selector).show(speed,callback);
- $(selector).toggle(speed,callback);
- $("span").parent();
- $("div").children();
- $("div").find("span"); 孩子
- $("h2").next(); 同胞兄弟