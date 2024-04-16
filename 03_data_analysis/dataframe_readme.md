# 1. DataFrame

## 1.1. Constructor
- data ndarray (structured or homogeneous), Iterable, dict, or DataFrame
- index 行索引信息
- columns 列名信息
- dtypes 列属性信息
- copy 

## 1.2. Attributes and underlying data
~~~
DataFrame.index:       The index (row labels) of the DataFrame. 行索引信息
- DataFrame.columns:      The column labels of the DataFrame. 列名信息
- DataFrame.dtypes:    Return the dtypes in the DataFrame. 列属性信息
- DataFrame.info([verbose, buf, max_cols, ...]):      Print a concise summary of a DataFrame. 返回表信息的summary
- DataFrame.select_dtypes([include, exclude]):     Return a subset of the DataFrame's columns based on the column dtypes. 返回一个子表，根据dtype选取
- DataFrame.values:     Return a Numpy representation of the DataFrame. 返回表的value信息，不含行列
- DataFrame.axes:      Return a list representing the axes of the DataFrame. 返回行列的标识信息
- DataFrame.ndim:      Return an int representing the number of axes / array dimensions. 返回表维度，一还是二
- DataFrame.size:      Return an int representing the number of elements in this object. 返回value中值的数量
- DataFrame.shape:      Return a tuple representing the dimensionality of the DataFrame. 返回(row count, column count)
- DataFrame.memory_usage([index, deep]):    Return the memory usage of each column in bytes. 返回内存使用情况
- DataFrame.empty:     Indicator whether Series/DataFrame is empty. 返回是否为空
- DataFrame.set_flags(*[, copy, ...]):      Return a new object with updated flags. 返回一个更新过的flag的表
~~~


## 1.3. Conversion
~~~
DataFrame.astype 将某几列的类型转成对应的类型
DataFrame.convert_dtypes 将所有列转成最合适的类型
DataFrame.infer_objects 将object转成合适的类型
DataFrame.copy 创建副本
DataFrame.bool 尝试将数字转成bool
DataFrame.to_numpy 转换成一个二维数组
~~~

### Indexing, iteration
~~~
DataFrame.head(n) 返回前n行
DataFrame.at[row_index, columns_name] = new_value 
DataFrame.iat[row_idx, column_idx] = new_value
DataFrame.loc[row_index, columns_name] = new_value
DataFrame.iloc[row_idx, column_idx] = new_value
DataFrame.insert(new_column_idx, new_column_name, new_column_value)
DataFrame.__iter__
DataFrame.items() return {column_name, column_series}
DataFrame.keys() return Index([column_name,,,])
DataFrame.iterrows return {row_index, row_series}
DataFrame.itertuples return {column_name=column_value,,,}
DataFrame.pop(column_name)
DataFrame.tail(n)
DataFrame.xs(column_name) 不能用来赋值
DataFrame.get([row_index, column_name])
DataFrame.isin([value list of values]) 返回一个二维矩阵，包含的数据打上True
DataFrame.where(cond=条件， other=replace_to_value(条件值为False时，用这个值代替源值), inplace=True(改源数据)/False(不改源数据))
DataFrame.mask() 和where一样，只是它mask源数据
DataFrame.query(Query the columns of a DataFrame with a boolean expression)
~~~

### Binary operator functions

~~~
add, sub, mul, div, floordiv, mod, pow
+  , -  , *  , /  , //      , %  , **

DataFrame.__add__
DataFrame.add    df[['height', 'weight']] + [0.5, 1.5] 扩展了加号的功能，类似于两个表的对应值相加
DataFrame.sub    两个表对应项相减
DataFrame.mul    两个表对应项相乘
DataFrame.div    两个表对应项相除
DataFrame.truediv 
DataFrame.floordiv
DataFrame.mod
DataFrame.pow
DataFrame.dot #矩阵乘法
DataFrame.radd
DataFrame.rsub
DataFrame.rmul
DataFrame.rdiv
DataFrame.rtruediv
DataFrame.rfloordiv
DataFrame.rmod
DataFrame.rpow
DataFrame.lt
DataFrame.gt
DataFrame.le
DataFrame.ge
DataFrame.ne
DataFrame.eq
DataFrame.combine #按一定的规则将两个表组合到一起
DataFrame.combine_first
~~~

