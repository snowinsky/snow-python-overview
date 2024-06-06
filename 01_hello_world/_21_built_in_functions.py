#!/usr/bin/python
# -*- coding: UTF-8 -*-

## 传说中的python内置函数  https://img-blog.csdnimg.cn/direct/9981a806ed244dae9730442a2ccacc48.jpeg
## 分类
# 入门函数 input() print() help()
# 数学函数 sum() max(), min(), divmod() abs() pow() round()
# 数据类型函数 int() str() bool() float() tuple() list() dict() set()
# 序列迭代函数 len() slice() sorted() reverse() filter() all() any() iter() next() range() enumerate() zip() map()
# 对象函数 id() type() isinstance() issubclass() staticmethod() super()
# 操作对象的函数 format() repr() eval() exec() open()
# 操作对象属性的函数 setattr() getattr() hasattr() delattr() property() vars()

class Simple_Class_Super(object):
    '''
    Simple_Class_Super help

    '''
    def __init__(self):
        pass

def simple_funs():
    aaa = input("Please input some words:::::")
    print(f"your input is {aaa}", help(aaa))
    scs = Simple_Class_Super()
    print("the Simple Class Super help is ", help(scs))

def seq_funs():
    '''
    len() slice() sorted() reverse() filter() all() any() iter() next() range() enumerate() zip() map()
    :return:
    '''
    seq = ['aa', 'bb', '00', 11, 44, 3, 23]
    print(slice(1,6,2))


if __name__ == '__main__':
    print("start to test the built-in functions")
    # simple_funs()
    seq_funs()

