# lxml

> 一个python中可以操作xml的三方jar
>
> 这次主要是研究它的xpath玩法
> 

lxml的安装和导入
~~~python
pip install lxml
from lxml import  etree
~~~

解析本地的xml文件
~~~python
html=etree.parse('xx.html',etree.HTMLParser())
aa=html.xpath('//*[@id="s_xmancard_news"]/div/div[2]/div/div[1]/h2/a[1]/@href')
print(aa)
~~~

解析在线的xml文件
~~~python
from lxml import etree
import requests
rep=requests.get('https://www.baidu.com')
html=etree.HTML(rep.text)
aa=html.xpath('//*[@id="s_xmancard_news"]/div/div[2]/div/div[1]/h2/a[1]/@href')
print(aa)
~~~

比如，有个html片段
~~~html
<a herf="http://www.baidu.com">百度搜索</a>
~~~
如果想获取http://www.baodu.com和百度搜索，有如下的方法
~~~python
a_text_val=html.xpath('//*[@id="s_xmancard_news"]/div/div[2]/div/div[1]/h2/a[1]/text()')

a_href_val=html.xpath('//*[@id="s_xmancard_news"]/div/div[2]/div/div[1]/h2/a[1]/@href')
~~~
其实重点的是/a[1]/text()就是拿取第一个<a>然后获取text，/a[1]/@href就是拿取第一个<a href="ssss">

如果是只获取到a这个标签之后呢？
~~~python
aa=html.xpath('//*[@id="s_xmancard_news"]/div/div[2]/div/div[1]/h2/a[1]')

aa.text #获取标签value

aa.attrib.get('href') #获取标签属性
~~~

下面是使用xpath的具体的例子。看什么w3c文档，看例子会用就行了。文档？没听说过谁能用文字把维纳斯雕塑的样子描述清楚的。

我的观点：用文字去描述一个实际应用的东西，就像是给瞎子讲颜色。
~~~python
#text是一个字符串，是一个xml的字符串
html = lxml.etree.HTML(text:str)

#第一个参数是一个文件路径，这个文件必须是xml格式的
html = lxml.etree.parse('./ex.html',etree.HTMLParser())


from lxml import etree

#获取所有的xml节点信息，尽量别用，超级多
result = html.xpath('//*')
#获取所有的li标签，不管上下级关系
result = html.xpath('//li')
#获取所有li标签下的a标签，必须是第一级的，用div一格就找不到了
result = html.xpath('//li/a')
#获取所有li节点的所有的a标签，和上面一个就差一点，就成了取所有的了，不是只取第一级的了
result = html.xpath('//li//a')
#获取所有a标签，href=link.html，然后找它的父节点，然后找class属性
result = html.xpath('//a[@href="link.html"]/../@class')
#获取所有class属性为ni的li节点
result = html.xpath('//li[@class="ni"]')
#获取所有li节点的文本，就是标签夹着的部分的内容，又叫text
result = html.xpath('//li/text()')
#获取所有li节点的a节点的href属性
result = html.xpath('//li/a/@href')
#获取所有li节点（class属性值中包含li）下的a标签的text
result = html.xpath('//li[contains(@class,"li")]/a/text())
#当li的class属性有多个值时，需用contains函数完成匹配
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
#多属性匹配
result = html.xpath('//li[1]/a/text()')
result = html.xpath('//li[last()]/a/text()')
result = html.xpath('//li[position()<3]/a/text()')
result = html.xpath('//li[last()-2]/a/text()')
#按序选择，中括号内为XPath提供的函数
result = html.xpath('//li[1]/ancestor::*')
#获取祖先节点
result = html.xpath('//li[1]/ancestor::div')
result = html.xpath('//li[1]/attribute::*')
#获取属性值
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
#获取直接子节点
result = html.xpath('//li[1]/descendant::span')
#获取所有子孙节点
result = html.xpath('//li[1]/following::*[2]')
#获取当前节点之后的所有节点的第二个
result = html.xpath('//li[1]/following-sibling::*')
#获取后续所有同级节点
~~~

~~~python

~~~