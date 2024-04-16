import pandas as pd

df = pd.DataFrame(
    data=[[1, "code1", "name1", 11.1, '2024-03-15', True], [2, "code2", "name2", 22.2, '2024-03-18', False]],
    index=["id1", "id2"],
    columns=["ID", "CODE", "NAME", "AMT", "INT_DATE", 'IS_MAN'],
)

# print(df)
#      ID   CODE   NAME   AMT
# id1   1  code1  name1  11.1
# id2   2  code2  name2  22.2

print(df.info(verbose=True))

print(df.select_dtypes(include=['float64']))

print(df.axes) #坐标的信息，就是行列信息

print(df.ndim) #返回表的维度，只有一列的Series，返回1，DataFrame这种表格的，返回2

print(df.size) #表中共存了多少值，row*columns

print(df.shape) # (rowcount, columncount)

print(df.memory_usage(True, True))

print(df.set_flags(copy=True))

print('********************************')
# 按列名转成对应的类型
print(df.astype({'ID':'int32', 'CODE':'string', 'NAME':'string'}, copy=False, errors='raise').dtypes)
print('********************************')
# 自动识别并转换成最合适的类型
print(df.convert_dtypes().dtypes)
print('********************************')
print(df.infer_objects().dtypes)
print('********************************')
print(df.to_numpy())
print('********************************')
d = {'num_legs': [4, 4, 2, 2],
     'num_wings': [0, 0, 2, 2],
     'class': ['mammal', 'mammal', 'mammal', 'bird'],
     'animal': ['cat', 'dog', 'bat', 'penguin'],
     'locomotion': ['walks', 'walks', 'flies', 'walks']}
df = pd.DataFrame(data=d)
df = df.set_index(['class', 'animal', 'locomotion'])
print(df.xs('mammal'))
print('********************************')
df = pd.DataFrame(data=[[10,20,30],[10.1,20.2,30.3]])
print(df)
print(df.div(3))
print(df.truediv(3))

print('********************************')

df = pd.DataFrame(data={"ID":[1,2], "CODE":['one','two'], "NAME":['HEBEI', 'HEBEI'], "AMT":[11.11,22.22]})
print(df)
print(df.groupby(['NAME']).sum("AMT"))
print('********************************')
print(df.to_json())
print(df.to_xml())



