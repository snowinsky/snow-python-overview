# pandas 基操

> https://www.knowledgedict.com/tutorial/pandas-dataframe.html#:~:text=Pandas%20DataFrame%20%E5%B8%B8%E7%94%A8%E6%93%8D%E4%BD%9C%E5%8F%8A%E5%9F%BA%E6%9C%AC%E7%9F%A5%E8%AF%86%E7%82%B9%E8%AF%A6%E8%A7%A3%201%20%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF%20%E7%BB%93%E6%9E%84%20DataFrame%20%E7%94%B1%E4%B8%89%E4%B8%AA%E4%B8%BB%E8%A6%81%E7%BB%84%E4%BB%B6%E7%BB%84%E6%88%90%EF%BC%8C%E5%88%86%E5%88%AB%E6%98%AF,...%205%20%E4%BB%8E%E7%B3%BB%E5%88%97%E7%9A%84%E5%AD%97%E5%85%B8%E6%9D%A5%E5%88%9B%E5%BB%BA%20DataFrame%20%E5%AD%97%E5%85%B8%E7%9A%84%E7%B3%BB%E5%88%97%E5%8F%AF%E4%BB%A5%E4%BC%A0%E9%80%92%E4%BB%A5%E5%BD%A2%E6%88%90%E4%B8%80%E4%B8%AA%20DataFrame%E3%80%82%20%E6%89%80%E5%BE%97%E5%88%B0%E7%9A%84%E7%B4%A2%E5%BC%95%E6%98%AF%E9%80%9A%E8%BF%87%E7%9A%84%E6%89%80%E6%9C%89%E7%B3%BB%E5%88%97%E7%B4%A2%E5%BC%95%E7%9A%84%E5%B9%B6%E9%9B%86%E3%80%82%20

> api doc url = https://pandas.pydata.org/docs/reference/

~~~python
DataFrame构造函数
pandas.DataFrame( data = None, # 按列展示的数据，如果元素是一个列表，则表示这是一行数据
                  index: Optional[Axes] = None, # 行名，行名可以是从0开始的数字，也可以自定为任意的值
                  columns: Optional[Axes] = None, #列名，
                  dtype: Optional[Dtype] = None, #列类型，每一列的类型可以不一样，所以，列类型这一项应该是和data中的数据对应的
                  copy: bool = False) # 只对数组数据类型有效，默认是false，表示不复制为二维数组来处理数据

可以用下面的方法获取对应的值：
print('df.columns=', df.columns)
print('df.index=', df.index)
print('df.values=', df.values)
print('df.dtypes=', df.dtypes)
~~~

~~~python
import pandas as pd

data = [['Alex', 18], ['Clark', 12, 1], ['Dean', 25], ['Tiffany', 23, 0]]
df = pd.DataFrame(data, columns=['Name', 'Age', 'Sex'])
print(df)
输出结果：
      Name  Age  Sex
0     Alex   18  NaN
1    Clark   12  1.0
2     Dean   25  NaN
3  Tiffany   23  0.0

print(df.)
~~~

~~~python
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print df
输出结果
      Age      Name
0     28        Tom
1     34       Jack
2     29      Steve
3     42      Ricky
~~~

~~~python
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print df
输出结果
         Age    Name
rank1    28      Tom
rank2    34     Jack
rank3    29    Steve
rank4    42    Ricky
~~~

~~~python
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print df
输出结果
    a    b      c
0   1   2     NaN
1   5   10   20.0
~~~

~~~python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
输出结果
      one    two
a     1.0    1
b     2.0    2
c     3.0    3
d     NaN    4
~~~
