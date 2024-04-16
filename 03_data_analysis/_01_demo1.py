#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

for x in dir(pd):
    if x.startswith('read'):
        print('pandas 可以读取：', x)
# pandas 可以读取： read_clipboard
# pandas 可以读取： read_csv
# pandas 可以读取： read_excel
# pandas 可以读取： read_feather
# pandas 可以读取： read_fwf
# pandas 可以读取： read_gbq
# pandas 可以读取： read_hdf
# pandas 可以读取： read_html
# pandas 可以读取： read_json
# pandas 可以读取： read_orc
# pandas 可以读取： read_parquet
# pandas 可以读取： read_pickle
# pandas 可以读取： read_sas
# pandas 可以读取： read_spss
# pandas 可以读取： read_sql
# pandas 可以读取： read_sql_query
# pandas 可以读取： read_sql_table
# pandas 可以读取： read_stata
# pandas 可以读取： read_table
# pandas 可以读取： read_xml

# https://zhuanlan.zhihu.com/p/633465160
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html
# pandas有很多的read方法，返回结果是一种叫做DataFrame的列存储数据库的表的数据结构。它特别类似于java中的ResultSet这种数据结构。
# DataFrame其实一个二维表格的结构，有行有列，有每一行的index(从0开始)
# 它就是个dictionary， key就是列名，value就是这一整列的数据，
    # >>> d = {'col1': [1, 2], 'col2': [3, 4]}
    # >>> df = pd.DataFrame(data=d)
    # >>> df
    #    col1  col2
    # 0     1     3
    # 1     2     4
# 里边有些名词解释一下
#   只有一列的dataframe叫series
#   行前面的索引从0开始，叫loc或者iloc
#   行叫axis，列叫column
#   每一列叫series


try:
    aaa = pd.read_clipboard()
    for y in aaa:
        print("clipboard data =", y)
except:
    pass
    
    
    
################## 数据分析第一步：读取源数据 ################


sales=pd.read_excel('D:/ws-py/snow-python-overview/03_data_analysis/2018_data_set.xlsx',dtype='object')

### 连接数据的大体状况

print('数据源的数据采样', sales.info) # 返回行列值并抽签前后五行的数据做采样
print('数据源的体量，行列', sales.shape) # 只返回(row_count, column_count)

print('数据源的前五行', sales.head) #抽样前五行
print('数据源的后五行', sales.tail) #抽样后五行

################## 数据分析第二步：数据清洗 ################
### 选取部分列
subsales = sales.iloc[0:6500, 0:6]
print(subsales.head)

### 把某些列的列名更名 inplace表示在原来的数据上更改
subsales.rename(columns={'购药时间':'销售时间', '社保卡号':'身份证号'},inplace=True)
print(subsales.head)

### ① 删除缺失数据（dropna方法）；② 填充缺失数据（filina方法）
###### dropna默认丢弃任何含有缺失值的行，即dropna()等价于dropna(axis=0,how='any')
## ''' axis=0 表示drop整行， 1 表示只drop相关列
## ''' how=any，all 一行中的任意一列为null，或者所有列都为null
## ''' subset=[] 表示只看列名是这个几个的列，其他列有没有值不管
subsales = subsales.dropna(axis=0, subset=['销售时间','身份证号'], how='any')

### 列数据类型转换
print('转换前的金额类型为：\n',subsales.dtypes)
subsales['销售数量']=subsales['销售数量'].astype('float') #默认类型是object，数字类型的转成数字比较方便进行数字类型的处理
subsales['应收金额']=subsales['应收金额'].astype('float')
print('转换后的金额类型为：\n',subsales.dtypes)

print(type(subsales['销售时间'].str))

subsales['销售时间-格式化'] = subsales['销售时间'].apply(lambda a: str(a).split(' ', 1)[0])
print('转换前的日期类型为：\n',subsales.dtypes)
subsales['销售时间-格式化']=pd.to_datetime(subsales['销售时间-格式化'],format='%Y-%m-%d',errors='coerce')
print('转换后的日期类型为：\n',subsales.dtypes)

subsales = subsales.dropna(axis=0, subset=['销售时间-格式化','身份证号'], how='any')

### 排序
subsales=subsales.sort_values(by='销售时间-格式化',ascending=True) 
print('排序后的数据集为：\n',subsales.head())
# 重置索引 就是前面的行号
subsales=subsales.reset_index(drop=True) 
print(subsales.head())

print(subsales.describe())

########################  第三步 构建模型  其实就是按提出的指标进行数据汇总 #########################################################
# 绘制线图
subsales.plot(x="销售时间-格式化", y="销售数量")
# 绘制散点图
#df.plot.scatter(x="CODE", y="AMOUNT")
# 绘制条形图
#df.plot.bar(x="CODE", y="AMOUNT")
plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置中文字体为SimHei 这样中文就不会显示成方块了
plt.rcParams['axes.unicode_minus'] = False # 解决负号'-'显示为方块的问题
plt.show()



