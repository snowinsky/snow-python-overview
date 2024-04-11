#!/usr/bin/python3
# -*- coding: UTF-8 -*-

list1 = [1,2.22,'abc']
newList1 = [str(element) for element in list1 if element != None]
print(newList1) # ['1', '2.22', 'abc']
newTupleFromList1 = (str(element) for element in list1 if element != None)
print(tuple(newTupleFromList1))

tuple1 = (1,2.22,'abc')
iter_tuple1 = iter(tuple1) # 迭代器
# for 循环使用迭代器
for e in iter_tuple1:
    print(e)


set1 = set((1,2.22,'abc'))
iter_set1 = iter(set1)
# while 循环使用迭代器
while True:
    try:
        e = next(iter_set1)
        print(e)
    except StopIteration:
        break

dict1 = {'a':1, 'b':12.123, 'c':"sfds"}

###################  迭代器  ############################

class NewClassImplementInteratable:
    '''
    一个类，如果想被迭代，就必须实现两个方法 __iter__() 与 __next__()
    '''
    def __init__(self, list1):
        self.list1 = list1
    
    def __iter__(self):
        return iter(self.list1)
    
    def __next__(self):
        return next(__iter__(self))

ccc = NewClassImplementInteratable([1,2,3,4,5])
iter_ccc = iter(ccc)
for el in iter_ccc:
    print(el)
    
###################  迭代器  ############################

###################  特殊的迭代器yield  ############################
# 函数中用到了yield内置函数的，叫生成器，这样的函数是把yield当return语句使用
# 但又会在next再次调用时继续执行，相当于输出了一个中间结果，例如
def countdown(n):
    while n > 0:
        yield n
        n -= 1

countdownGen = countdown(5)
for a in countdownGen:
    print(a)
