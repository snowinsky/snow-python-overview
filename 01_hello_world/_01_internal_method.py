#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Abc:
    a = 0
    b = 1.1
    c = "abc...."

    __abs__ = abs(b)


# python的内置函数，什么地方都可以直接使用

# (a,b,c) tuple 相当于一个数组
# [a,b,c] list 相当于一个链表
# {a:av, b:bv, c:cv} dictionary相当于数据库表中的一行数据，所以，每一个列都是不同的


############################  math相关操作
# abs 返回一个数字类型的绝对值
print("abc = ", abs(0))
print("abc = ", abs(1))
print("abc = ", abs(-1))
print("abc = ", abs(-1.1))
#555 print(abs("-1.111111")) #TypeError: bad operand type for abs(): 'str'

# pow(base, exp, mod=None) 乘方 base的exp次方

# round(number, ndigits=None) 四舍五入 把number这个数小数点后保留ndigits位小数，如果不写就是不保留

# sum(iterable, /, start=0) 求和
print("sum = ", sum([1,2,3]))

# divmod(a, b) 返回a/b的商和余数
divmodResule = divmod(10, 3)
print("divmod = ", divmodResule[0], ".....", divmodResule[1])
print("divmod = ", type(divmodResule))
############################  math相关操作

print("list = ", list((1,2.2554,"a")))


########################### 迭代器相关操作
# iter(object)
# next(iterator)
it1 = iter("sdf")
try:
    while True:
        print("iter next = ", next(it1))
except StopIteration:
    pass

# iter(object, sentinel)
# next(iterator, default)

# all(iterable) 所有值都为true则返回true
# aiter(async_iterable) 返回一个异步迭代器
# awaitable anext(async_iterator, default) 返回异步迭代器的异步next值
# any(iterable) 任意一个值为true则返回true
# sorted(iterable, /, *, key = None, reverse = False)
# filter(function, iterable) 过滤iterable中的所有不符合function的条件的元素

# max(iterable, *, key=None)
# max(iterable, *, default, key=None)
# max(arg1, arg2, *args, key=None)
# min(iterable, *, key=None)
# min(iterable, *, default, key=None)
# min(arg1, arg2, *args, key=None)

# reversed(seq) #反转，sequence是有顺序的，这个函数就是反序


# zip(*iterables, strict=False) # 把多个iterable压缩都一起
print("zip = ",zip((1,2,3,'a'), ['a','b','c','d'], ['one','two',True, False])) #zip =  <zip object at 0x000002D69BF1B900>
print("zip = ",list(zip((1,2,3,'a'), ['a','b','c','d'], ['one','two',True, False, ''f'sss''']))) #zip =  [(1, 'a', 'one'), (2, 'b', 'two'), (3, 'c', True), ('a', 'd', False)]


########################### 迭代器相关操作

########################## 对象创建，格式转换

# int(x=0)
# int(x, base=10)
# complex(real=0, imag=0)或者complex(string)返回一个复数
# float(x=0.0) 创建浮点数

# enumerate(iterable, start=0) 将一个迭代器转化为对象，从start开始
print('enumerate = ', enumerate([1,2.222,'abc']))
print('enumerate = ', list(enumerate([1,2.222,'abc'])))


# dict(**kwarg) 创建字典类
print("dict =", dict())
# dict(mapping, **kwarg)创建字典类
print("dict =", dict(a=1, b=111.111, c="abc"))
# dict(iterable, **kwarg)创建字典类
print("dict =", dict([['a', 1],['b', 22.1222],['c', "abc"]]))

# ascii(object) 返回对象的ascii码格式

# bin(x) 将数字类型转换为二进制字符串，以0b开头
# hex(x) 将数字类型转换为十六进制字符串，以0x开头
# oct(x)

# bool(x=False) 返回bool型


# bytearray(source, encoding, errors) 将source按照encoding的方式转成byte数组，报错则记录到errors里边
# bytes(source, encoding, errors) 将source按照encoding的方式转成bytes对象，报错则记录到errors里边


# chr(i) 把一个数字转成字符
# ord(c) 把一个字符转成数字
########################## 对象创建，格式转换

# format(value, format_spec='') 将value按第一个参数进行格式化
# frozenset(iterable=set()) 创建一个frozenset

# len(s)

# list
# list(iterable)

# range(stop)
# range(start, stop, step=1)
# set
# set(iterable)
# str(object='')
# str(object=b'', encoding='utf-8', errors='strict')

# slice(stop)
# slice(start, stop, step=None)
# tuple(iterable)

# map(function, iterable, *iterables)


############################ 针对对象中的属性的操作
# getattr(object, name) 获取object中属性是name的值
# getattr(object, name, default)获取object中属性是name的值
# hasattr(object, name)
# delattr(object, name) 删除object中名字叫name的属性
# setattr(object, name, value)
############################ 针对对象中的属性的操作

######################### 获取object的相关信息的方法

# globals() 返回实现当前模块命名空间的字典
# locals()
# vars()
# vars(object)
# dir(object) 返回object的所有属性列表

# hash(object) 返回object的hash
# id(object)返回对象的标识

# isinstance(object, classinfo)
# issubclass(class, classinfo)

# object
# memoryview(object)

# breakpoint(*args, **kws) 进入调试器
# callable(object) 返回true false，判断object是否可调用
# @classmethod 注解，加载方法上，标注该方法为静态方法
class ABC(object):
    a = 1
    b = 'a'
    
    def __init__(self,a, b):
        self.a = a
        self.b = b
    
    def printMyself(self):
        print(self.a, self.b)
        return "print a b complete"

    @classmethod
    def firstStaticMethod(self):
        print("ABC.firstStaticMethod")

print("自定义类ABC，调用类方法 = ", ABC(11, 'aa').printMyself())
# print(ABC.printMyself()) #TypeError: ABC.printMyself() missing 1 required positional argument: 'self'
print(ABC.firstStaticMethod()) #ABC.firstStaticMethod

# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1) 编译成代码
# eval(expression, globals=None, locals=None) 把expression字符串当成python的表达式去执行
# exec(object, globals=None, locals=None, /, *, closure=None) 动态执行python代码，只能执行void的方法
#　repr(object)

# class type(object)
# class type(name, bases, dict, **kwds)
a = 111
b = 11.11
c = "asdfas"
print(type(a))
print(type(b))
print(type(c))
# <class 'int'>
# <class 'float'>
# <class 'str'>


######################### 获取object的相关信息的方法




######################### 针对文件的ＩＯ操作
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# print(*objects, sep=' ', end='\n', file=None, flush=False)

# class property(fget=None, fset=None, fdel=None, doc=None)

# __import__(name, globals=None, locals=None, fromlist=(), level=0)

# @staticmethod

# print(__name__)