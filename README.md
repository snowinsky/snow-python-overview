# snow-python-overview

> https://docs.python.org/zh-cn/3.13/tutorial/index.html python官方文档

## python安装

> 和jdk类似，只是安装之后如果想安装第三方模块，可以用

~~~python
python -m pip install --upgrade SomePackage
~~~

编写的是.py文件，打包成.whl文件来供别人调用。
如果想执行，可以用py2exe打包成.exe文件在windows上，
或者用py2app打包在macos上，
或者用pex打包在linux上。

和go比较类似。

## 语法分析

- 用反斜杠\可以把多行的语句拼接成一行。
- 用#开头是注释
- 用# -*- coding: <encoding-name> -*- 来做编码声明
- 用缩进来确定代码层级，缩进错了也得不到有效的效果
- 关键字不能使用作为变量名
- 软关键字match type case等也最好不要做变量名
- 以下划线开头并以下划线结尾的有特殊含义
~~~
#### 关键字
- 赋值型关键字 False None True 
- 控制型关键字 if else elif break continue pass return 
- 逻辑型关键字 is not or and 
- 工具型关键字 import await  in raise class
- 异常型关键字 try except finally， assert del with yield async
- 定义型关键字 def class global lambda as from nonlocal
~~~

## 程序的本质(对象具有标识、类型、值三个属性)

> 程序本质上就是在描述“对象与对象之间的关系”。而每个对象都拥有标识，类型和值。一个对象被创建后，标识永远不变(is可以比较两个对象标识是否一样，id()则会返回具体的标识)。

> type()返回一个对象的类型，类型也是不可变的。对象被创建出来，最好显示的被关闭，否则可能会被垃圾回收。

## 对象的值

#### 1.None没赋值的对象，false
#### 2.NotImplemented没事实现的方法的返回值，不应该判断true和false
#### 3.Ellipsis true
#### 4.numbers.Number
> 数字对象不可变
- numbers.Integral 整数，包括整数和负数(包括int和bool)
- numbers.Real (float) 双精度浮点数
- numbers.Complex (complex) 复数z.real 和 z.imag 用来标识实部和虚部

#### 5.array 序列sequence
> len(a)返回长度，a[i]返回值，a[-i]也支持，a[i:j]也支持

> 有限长度，有序的集合叫序列

- 不可变序列 
    - string（使用unicode实现的，ord()把一个字符转成整数，chr()把一个整数转成字符，字符串.encode()将字符串转成指定bytes类型，bytes.decode()转会字符串）

    ~~~
    >>> "a".ord()                                                         
    Traceback (most recent call last):                                    
    File "<stdin>", line 1, in <module>                                 
    AttributeError: 'str' object has no attribute 'ord'                   
    >>> ord("a")                                                          
    97                                                                    
    >>> chr(97)                                                           
    'a'                                                                   
    >>> ord("aaa")                                                        
    Traceback (most recent call last):                                    
    File "<stdin>", line 1, in <module>                                 
    TypeError: ord() expected a character, but string of length 3 found   
    >>> "aaa".encode()                                                    
    b'aaa'                                                                
    >>> b'aaa'.decode()                                                   
    'aaa'                                                                 
    >>>                                                                   
    ~~~
    - tuple

    ~~~
    ~~~

    - bytes

    ~~~
    ~~~
- 可变序列
    - 爱仕达发


#### 6.不重复且不可变对象组成的无序且有限的集合
- len()返回长度
- 不能用下标访问
- 但是能迭代
- set()构造器创建
- add()可以修改
- frozenset创建不可变集合

#### 7.mapping 键值对 ap[k]=v
#### 8.字典 


