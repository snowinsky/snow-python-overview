import pandas as pd

d = {
    "one": pd.Series([1, 2, 3], index=["a", "b", "c"]),
    "two": pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"]),
}
print(
    "########DataFrame本质上是一个列存储的二维数组，第一维是列，第二维度是行#########"
)
print("########表信息#########")
df = pd.DataFrame(d)
print("df=", df)
print("列信息=", df.columns)
print("行信息=", df.index)
print("值信息=", df.values)
print("列类型=", df.dtypes)

print("########列操作#########")
oneColumn = df["one"]  # 列选取用中括号加列名
print("df.column.one=", oneColumn)
print(type(oneColumn))  # pandas.core.series.Series
print(oneColumn.name)
print("Adding a new column by passing as Series:")
df["three"] = pd.Series(
    [10, 20, 30], index=["a", "b", "c"]
)  # 增加列也是直接用中括号加列名来增加
print(df)

print("Adding a new column using the existing columns in DataFrame:")
df["four"] = (
    df["one"] + df["three"]
)  # 增加列赋值时可以用已有列的值操作进行赋值，可见pandas.core.series.Series实现了__add__等方法，所以可以用加减乘除号来直接操作

print("Deleting the first column using DEL function:")
del df["one"]  # 列删除直接用del
print(df)

# using pop function
print("Deleting another column using POP function:")
df.pop("two")  # 列删除也可以用dataframe的pop方法
print(df)

print("########行操作#########")
print(df.loc)  # <pandas.core.indexing._LocIndexer object at 0x0000027F39EEB200>
print(df.iloc)  # <pandas.core.indexing._iLocIndexer object at 0x0000013BDB7FAF30>
bRow = df.loc["b"]  # 选取行就得用dataframe提供的localindex数据结构了，loc[列名]
ibRow = df.iloc[1]  # iloc[列索引]
print("df.row.b=", bRow)
print("df.row.1=", ibRow)
print(type(bRow))  # <class 'pandas.core.series.Series'>
print(type(ibRow))  # <class 'pandas.core.series.Series'>

print(
    type(df[1:2])
)  # <class 'pandas.core.frame.DataFrame'> 这种用切片选取行的方式，其实获取的不是行，是一个子表
print(df[1:2])


df = pd.DataFrame(data=[[1, 2], [3, 4]], columns=["a", "b"])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=["a", "b"])

df = df._append(
    df2
)  # 新增行，其实不是新增了row，而是新增了一个子表，然后把子表拼到原来的表上

# Drop rows with label 0
df = df.drop(
    0
)  # 删除行，根据row index去删除行，index相同的行都会被删除掉，删除的不一定是一行

print(df)

print(
    "以上都是对dataframe这种数据结构的行列的单独操作，下面研究一下对DataFrame的行列的聚合操作"
)

df = pd.DataFrame(
    data={
        "ID": [-1, 1, 2, 3, 4, 5, 6],
        "CODE": ["yishu", "one", "two", "three", "four", "five", "six"],
        "NAME": ["复数", "苹果", "绿厂", "小米", "蓝厂", "荣耀", "小米"],
        "AMOUNT": [-2453.44, 1551.45, 5421.45, 4881.54, 4185.15, 4882.25, 4885.52],
        "FAKE": [0, 0, None, None, 0, 0, 0],
    },
    index=["fake", "iphone", "vivo", "xiaomi", "oppo", "honor", "redmi"],
)

print("整表数据\n", df)

# 查看前5行数据
print("前五行\n", df.head())
# 查看后5行数据
print("后五行\n", df.tail())
# 查看数据的描述性统计信息
print("整表数据统计信息\n", df.describe())

# 整表数据
#          ID   CODE NAME    AMOUNT
# iphone   1    one   苹果    155.45
# vivo     2    two   绿厂    542.45
# xiaomi   3  three   小米    488.54
# oppo     4   four   蓝厂  41858.15
# honor    5   five   荣耀    488.25
# redmi    6    six   小米   4885.52
# 选择行和列：
print(
    "选择vivo行的AMOUNT列\n", df.loc["vivo", "AMOUNT"]
)  # 选择第一行的列名是name的这一项
print("选择第一行的第二列\n", df.iloc[0, 1])  # 选择第一行的第二列
# 选择行：
print("选择vivo行\n", df.loc["vivo"])
print("选择第一行\n", df.iloc[0])
# 选择列：
print("选择NAME列\n", df["NAME"])

# 计算列的平均值
print("AMOUNT的平均值\n", df["AMOUNT"].mean())
# 计算列之间的相关性
df.corr()
# 删除某些列或行
print("删除FAKE列\n", df.drop(columns=["FAKE"], axis=1))
print("删除fake行\n", df.drop(index=["fake"]))

# 检查缺失值
print("检查是否为null\n", df.isnull())
# 填充缺失值
print("用0填充NaN位置\n", df.fillna(0))

# 分组和聚合
# df.groupby('NAME').mean()

print(df)


import matplotlib.pyplot as plt


# 绘制线图
df.plot(x="CODE", y="AMOUNT")
# 绘制散点图
df.plot.scatter(x="CODE", y="AMOUNT")
# 绘制条形图
df.plot.bar(x="CODE", y="AMOUNT")

plt.show()
