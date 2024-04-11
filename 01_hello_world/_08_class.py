#!/usr/bin/python
# -*- coding: UTF-8 -*-

class App1:
    '''
    这是类定义的一部分，相当于javadoc, 调用__doc__方法就可以打印出来这部分的内容
    '''
    
print(type(App1()))
a_app1 = App1()
b_app1 = App1()
print(a_app1 == b_app1)
print(a_app1 is b_app1)
print(a_app1.__doc__)

########################## class的内部方法 ##########################################
# 下面的方法是每一个class被创建时就被默认创建的，可以重写这些方法
# __init__( self [,args...] ) 构造函数 简单的调用方法: obj = className(args)
# __del__( self ) 析构方法, 删除一个对象 简单的调用方法 : del obj
# __repr__( self ) 转化为供解释器读取的形式 简单的调用方法 : repr(obj)
# __str__( self ) 用于将值转化为适于人阅读的形式 简单的调用方法 : str(obj)
# __cmp__ ( self, x ) 对象比较 简单的调用方法 : cmp(obj, x)
########################## class的内部方法 ##########################################

########################## class的属性 ##########################################
# 双下划线开头的属性为private的attrabute，只能通过类的方法访问
########################## class的属性 ##########################################

########################## class的方法 ##########################################
# def定义的方法，第一个参数必须是self
# 方法名以双下划线开头，就是私有方法
########################## class的方法 ##########################################
class Parent:
    '''
    '''
    id = 10 #public static的变量，类的所有实例共享，其中一个实例更新这个值，其他实例读取的就是新的值了。要考虑多线程的事. 相当于public static的
    
    _id = -10 #protected的变量，只能当前类和子类访问，不能import
    
    __id = -100 #private的变量，只能当前类访问
    
    # 构造函数，类中的所有函数第一个参数都是this，表示这个类的当前实例，另外的参数才是真正的入参
    def __init__(self, name):
        self.name = name
    
    def printSelf(self):
        print(__name__,"printSelf() id and name = ",self.id, self._id, self.__id, self.name)
        
    def _printSelf(self):
        print(__name__,"_printSelf() id and name = ",self.id, self._id, self.__id, self.name)
        
    def __printSelf(self):
        print(__name__,"__printSelf() id and name = ",self.id, self._id, self.__id, self.name)
        
    def changeId(self, newId):
        Parent.id = newId
        
parent_zhang = Parent("zhang")
parent_wang = Parent("wang")

print(Parent.id) #0
try:
    print(Parent.name) #AttributeError: type object 'Parent' has no attribute 'name'
except:
    pass

print(parent_zhang.name) #zhang

parent_wang.changeId(333)
print(parent_zhang.id, parent_wang.id, Parent.id)

print(parent_wang._id)
try:
    print(parent_wang.__id)
except:
    pass

try:
    Parent.printSelf()
except:
    pass

try:
    Parent._printSelf()
except:
    pass

try:
    Parent.__printSelf()
except:
    pass

parent_wang.printSelf()
parent_wang._printSelf()
try:
    parent_wang.__printSelf()
except:
    pass


class Child(Parent, App1): #支持多继承
    '''
    Child继承了Parent和App1，支持多继承，除了不能访问里边双下划线开头的属性和方法之外，其他的都可以的。
    而且和父类共享无下换线的属性的值，注意多线程读写。
    可以直接访问但下划线的属性和方法
    根本没法触摸到双下划线的属性和方法
    '''
    def printSelf(self):
        print(__name__, "Child printSelf id and name =", self.id, self._id, self.name)
        
    
print(dir(Child("wang_son")))

Child("li_son").changeId(444)
parent_zhang.printSelf()
Child("zhao_son").printSelf()
