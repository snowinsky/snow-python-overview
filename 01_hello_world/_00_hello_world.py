#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 安装和java jdk一样。
# 第二行注释居然是为了避免中文乱码的，也可以协程coding=UTF-8， 而且等号两边不能用空格，怪异的规则，一看就是各种修修补补

print(111)
print(111e12)
print(111.12)
print('abc')
print("abc")
########## 最喜欢的三引号文本块 ##############
print("""a
b
c""")
########## 最喜欢的三引号文本块 ##############
print(True)
print(False)

########## print函数怎么加参数来填充字符串模板 ##############
print('I love %c and %c'%('S',"M")) # %c 就是一位字符，print的格式化輸出必須将模板字符串和模板参数用百分号分隔开就行
print('I want to learn %s. How about you?' %'Python') # %s 表示string
print('I like number %d' %23) # %d 表示整数
print('10 - 23 is %d, not %u' %(-13, 13) ) # %d 表示整数 %u表示无符号数
print('return: %o' %56) # 十进制数转八进制
print('Return: %x %x' %(123, 257)) # 无符号十进制数转换为十六进制数。
print('Return: %X %X' %(123, 257)) #格式化无符号十六进制数（大写）：%X
print('PI= %f' %(3.1415926)) #浮点数
print('PI= %f, about %.2f' %(3.1415926, 3.1415926)) #浮点数可以制定精度，.2表示小数点后两位
print('%e' %(1.0e3)) #科学计数法格式化浮点数：%e
print('%g %g' %(1.0e3, 1.23)) #格式化浮点数（简写）：%g
########## print函数怎么加参数来填充字符串模板 ##############

# Python有五个标准的数据类型：#############
#
# Numbers（数字）不可变的，对它的更改都是创建新对象 又分解出int，long(也没了)，float和complex，其中int又有bool来标识True和False
# String（字符串） 不可变，所以拼接字符串很耗费资源
# List（列表）list1 = ['a', "b", 111, 11.12] 可以更改.
# Tuple（元组）tuple1 = ('a', "b", 111, 11.12)  不可更改。只读的列表，只能赋值一次。
# Dictionary（字典） dic1 = {'a':"av", 'b':"bv"}

list1 = ['a', "b", 111, 11.12]
print(list1)
list1.append("12312")
print("after append %s" %list1)
list1.remove("12312")
print("after remove %s" %list1)
tuple1 = ('a', "b", 111, 11.12)
print(tuple1)
print("tuple1 点不出任何修改其中内容的方法")
dic1 = {'a':"av", 'b':"bv"}
print(dic1)
dic1['a'] = "avv" # 修改key对应的value
print(dic1)
del dic1['a'] # 删除对应的key
print(dic1)
dic1.clear() #清空所有键值对
dic1['abc'] = 1213 #新增键值对
print(dic1)
del dic1

# print(dic1) #NameError: name 'dic1' is not defined. Did you mean: 'dict'?
# print(dic1 == None) #居然什么结果都没有，咩有任何输出

# aa = int("aasdf") #ValueError: invalid literal for int() with base 10: 'aasdf'

###################### 各种类型的转换和实现#############
print(type(int('123'))) #将x转换为一个整数

# print(type(long('216464667967797')))#将x转换为一个长整数

print(type(float('1245455.1545454')))#将x转换到一个浮点数

print(type(complex(1545488,86467497)))#创建一个复数

print(type(str(497464646)))#将对象 x 转换为字符串

print(type(repr('abacawer')))#将对象 x 转换为表达式字符串
print(repr(111/11)) # repr则是把对象转成解析器读取的形式，不管你定义的str方法怎么写
print(str(111/11)) # str调用的是str(obj)的obj参数的__str__()方法,对象输出什么时候可以自己定义的
#print(eval(111/11)) # eval是把字符串当成可执行命令来执行，所以直接给数字就报错了
print(repr('111/11')) # '111/11' 解释器看到的就是带单引号的这个东西
print(str('111/11')) # str调用的是str(obj)的obj参数的__str__()方法
print(eval('111/11')) # 直接当可执行的命令行执行出了结果，然后把结果打印了出来

print(type(eval('3+15')))#用来计算在字符串中的有效Python表达式,并返回一个对象

print(type(tuple('[1,12,123,12]'))) #将序列 s 转换为一个元组
print(tuple('[1,12,123,12]')) #('[', '1', ',', '1', '2', ',', '1', '2', '3', ',', '1', '2', ']')
print(tuple('(1,12,123,12)')) #('(', '1', ',', '1', '2', ',', '1', '2', '3', ',', '1', '2', ')')
print(tuple((1,12,123,12))) #(1, 12, 123, 12)
print(tuple([1,12,123,12])) #(1, 12, 123, 12) 把列表转成一个元组

print(type(list('123,343,234,234')))#将序列 s 转换为一个列表
print(list('123,343,234,234')) #['1', '2', '3', ',', '3', '4', '3', ',', '2', '3', '4', ',', '2', '3', '4']

print(type(set('123,343,234,234')))#转换为可变集合
print(set('123,343,234,234')) #输出不固定，{'4', '1', '2', '3', ','} 就是把字符串中的字符去重复
print(type(frozenset('123,343,234,234')))#转换为不可变集合
print(frozenset('123,343,234,234')) # 输出也是不固定的frozenset({'1', '4', '3', '2', ','})

print(type(chr(97))) #将一个整数转换为一个字符

# print(type(unichr(97)))#将一个整数转换为Unicode字符 NameError: name 'unichr' is not defined

# print(type(dict('a:123,b:343,c:234,d:234')))#创建一个字典。d 必须是一个序列 (key,value)元组。
print(dict())
print(dict([('a',1),('b',2)]))
print(dict(a=1,b=2))

print(type(ord('x')))#将一个字符转换为它的整数值
print(type(hex(97)))#将一个整数转换为一个十六进制字符串
print(type(oct(97)))#将一个整数转换为一个八进制字符串

############# if#############
aa = 1
if aa > 1 and aa != 0:
    print("a > 1")
elif aa < 1:
    print("a < 1")
else:
    print("a = 1")
############## while#############
bb = 10
while bb > 0:
    bb -= 1
    print(bb)

############# for#############
fruits = ['banana', 'apple',  'mango', 'abc']
for fruit in fruits:
    print(fruit)

for idx in range(len(fruits)):
    print(fruits[idx])

for fruit in fruits:
    if fruit == 'banana':
        print("meet banana continue")
        continue
    elif fruit == 'apple':
        print("meet apple pass")
        pass
    else:
        print("meet other=%s break" %fruit)
        break
############# 字符串的格式化 #############
######## 百分号格式化模板 %
######## 三引号字符串块
######## f字符串 定义了大括号里边带参数名的方式，冒号后带格式定义
my_binary = 0b11111001110
my_hex = 0x7e7
print(f'Binary num is {my_binary:d}, hex num is {my_hex:d}')
######## format内置函数
print(format(687368363.1415926, ',.2f')) #逗号分隔，小数点后保留两位浮点数
print(format('Yam Fish', '#^20')) # 补齐20位，用井号补，^表示把内容居中
print('Binary num is {}, hex num is {}'.format('my_binary', 'my_hex')) #格式


print('abc'.join(['111','2333','233'])) #111abc2333abc233


###  字符串模板的三种使用方式，1 百分号玩法 2 str的format函数 3 f字符串  第一种不推荐，第二种适合模板和赋值分离的情况，第三种适合模板和赋值不分离的情况
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1, txt2, txt3)

