#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

# 必选参数
def log(p1, p2):
    '''
    :param p1:
    :param p2:
    :return:
    '''
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), p1, p2)
    pass

if __name__ =="__main__": #python是一个脚本语言，它的所有的可以执行的语句都会在import，run等等的时候被执行，而非脚本语言是需要把所有的执行语句都放到main方法中，而这句话就是为了保证在import的时候，这些语句不被执行
   # stuff only to run when not called via 'import' here
   log("sdf", "11")
   log(p2="wo shi p2", p1="I'm p1")

# 参数设置默认值
def log(p1="I'm null p1", p2=None):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), p1, p2)
    return
if __name__ =="__main__":
    log()

# 不定行参数
def log(p1, *param):
    for p in param:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), p1, p)
    return
if __name__ =="__main__":
    log("log...不定长。。。", 1, 2, 'a', 'b', "adafsdf", time.localtime())

# 匿名函数, 只能一行语句，写多行时，就得写具体的自定义函数
noFun1 = lambda arg1,arg2: arg1 * 3.14 + arg2
if __name__ =="__main__":
    print(noFun1(1,2))
    print(noFun1(3,4))



