#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python 模块(Module)，是一个 Python 文件，以 .py 结尾

pi = 3.14

#计算圆的面积
def cycleArea(radius):
    return pi*radius**2

print(cycleArea(3), "平方米")

#计算圆的周长
def cyclePerimeter(radius):
    return 2*pi*radius

print(cyclePerimeter(3), "米")

#导入另一个模块，就是引入另一个py文件中的内容
import _03_function as logger
logger.log('aa', 'bb')
#只导入一部分功能 from 模块名 import 模块的部分功能，部分功能
#from _03_function import log
#log("asdf", "abc")
#也可以导入所有的内容
#from _00_hello_world import *

# 当你导入一个模块，Python 解析器对模块位置的搜索顺序是：
#
# 1、当前目录
# 2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
# 3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
# 模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

# 也就是先找当前文件夹，然后找PYTHONPATH指定的文件夹，最后找默认文件夹

def testGlobalVar():
    global pi
    pi = pi + 1
    return pi

print(testGlobalVar())

dirResult = dir()
for dirResultElement in dirResult:
    print("当前的模块所包含的方法", dirResultElement)

print(__name__)
print(__package__)
print(__doc__)
print(__builtins__)

globalsResult = globals()
print(globalsResult)

localsResult = locals()
print(localsResult)

from pypackage.person import println

println("sdfsadfa", "sdfsdf", "sdfsdf")

