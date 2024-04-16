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

### Function application, GroupBy & window

~~~
DataFrame.apply(参数是一列)
DataFrame.map(将一列数据转成另外一种类型)
DataFrame.applymap 已经废弃了
DataFrame.pipe(链式处理的函数，第一个参数是.pipe前面的对象，第二个之后的参数才是真实的参数) 例如：
def subtract_federal_tax(df):
    return df * 0.9
def subtract_state_tax(df, rate):
    return df * (1 - rate)
def subtract_national_insurance(df, rate, rate_increase):
    new_rate = rate + rate_increase
    return df * (1 - new_rate)
df.pipe(subtract_federal_tax)
    .pipe(subtract_state_tax, rate=0.12)
    .pipe(subtract_national_insurance, rate=0.05, rate_increase=0.02)

DataFrame.agg(['sum', 'min']) 执行聚合函数
DataFrame.aggregate(['sum', 'min']) 执行聚合函数
DataFrame.transform() 执行一个函数，返回和以前一样的行列的dataframe
DataFrame.groupby([列名1,列名2]) 这是一个中间函数，必须得接聚合函数才行
DataFrame.rolling 滑动窗口，这也是一个中间函数，必须得接聚合函数才有意义
DataFrame.expanding 扩展窗口，这也是一个中间函数，必须得接聚合函数才有意义
DataFrame.ewm 加权指数计算
~~~

### Computations / descriptive stats

~~~
DataFrame.abs 返回表中各个字段的绝对值
DataFrame.all 返回true或者false，判定是不是都是True
DataFrame.any 返回是否有一个是True
DataFrame.clip(lower=n, upper=m) 把小于n的修剪成n，把大于m的修剪成m
DataFrame.corr 计算同一dataframe中各列的相关性
DataFrame.corrwith 计算该表与另外一个表的相关性
DataFrame.count 计算各列非null的值的数量
DataFrame.cov计算列的成对协方差
DataFrame.cummax返回具有最大累积值的 DataFrame
DataFrame.cummin返回具有最小累积值的 DataFrame
DataFrame.cumprod查找到目前为止在任何轴上看到的值的累积乘积
DataFrame.cumsum查找任何轴上的累加总和值
DataFrame.describe基本的统计详细信息，例如数据帧的百分位数，均值，标准差等或一系列数值
DataFrame.diff  返回一个 DataFrame，其中包含每行的值与默认情况下前一行的值之间的差值
DataFrame.eval函数用于在调用 DataFrame 实例的上下文中评估表达式。 该表达式在 DataFrame 的列上求值
DataFrame.kurt 函数使用Fisher的峰度定义 (正常的峰度== 0.0)在请求的轴上返回无偏峰度。 由N-1归一化
DataFrame.kurtosis返回样本的 Fisher 无偏峰度
DataFrame.max对象中的最大值
DataFrame.mean返回所请求轴的平均值
DataFrame.median返回所请求轴的中位数
DataFrame.min返回所请求轴的最小值
DataFrame.mode
DataFrame.pct_change
DataFrame.prod将每列中的所有值相乘，并返回每列的乘积
DataFrame.product请求axis的乘积值
DataFrame.quantile
DataFrame.rank
DataFrame.round
DataFrame.sem
DataFrame.skew
DataFrame.sum
DataFrame.std
DataFrame.var
DataFrame.nunique
DataFrame.value_counts
~~~

### Reindexing / selection / label manipulation

~~~
DataFrame.add_prefix
DataFrame.add_suffix
DataFrame.align
DataFrame.at_time
DataFrame.between_time
DataFrame.drop
DataFrame.drop_duplicates
DataFrame.duplicated
DataFrame.equals
DataFrame.filter
DataFrame.first
DataFrame.head
DataFrame.idxmax
DataFrame.idxmin
DataFrame.last
DataFrame.reindex
DataFrame.reindex_like
DataFrame.rename
DataFrame.rename_axis
DataFrame.reset_index
DataFrame.sample
DataFrame.set_axis
DataFrame.set_index
DataFrame.tail
DataFrame.take返回给定位置索引中的元素
DataFrame.truncate在某个索引值之前和之后截断Series或DataFrame。 这是基于高于或低于某些阈值的索引值进行布尔索引的有用捷径。 用法： DataFrame. truncate (before=None, after=None, axis=None, copy=True)
~~~

### Missing data handling

Missing data handling
~~~~~~~~~~~~~~~~~~~~~
.. autosummary::
   :toctree: api/

   DataFrame.backfill
   DataFrame.bfill
   DataFrame.dropna
   DataFrame.ffill
   DataFrame.fillna
   DataFrame.interpolate
   DataFrame.isna
   DataFrame.isnull
   DataFrame.notna
   DataFrame.notnull
   DataFrame.pad
   DataFrame.replace

Reshaping, sorting, transposing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autosummary::
   :toctree: api/

   DataFrame.droplevel
   DataFrame.pivot
   DataFrame.pivot_table
   DataFrame.reorder_levels
   DataFrame.sort_values
   DataFrame.sort_index
   DataFrame.nlargest
   DataFrame.nsmallest
   DataFrame.swaplevel
   DataFrame.stack
   DataFrame.unstack
   DataFrame.swapaxes
   DataFrame.melt
   DataFrame.explode
   DataFrame.squeeze
   DataFrame.to_xarray
   DataFrame.T
   DataFrame.transpose

Combining / comparing / joining / merging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autosummary::
   :toctree: api/

   DataFrame.assign
   DataFrame.compare
   DataFrame.join
   DataFrame.merge
   DataFrame.update

Time Series-related
~~~~~~~~~~~~~~~~~~~
.. autosummary::
   :toctree: api/

   DataFrame.asfreq
   DataFrame.asof
   DataFrame.shift
   DataFrame.first_valid_index
   DataFrame.last_valid_index
   DataFrame.resample
   DataFrame.to_period
   DataFrame.to_timestamp
   DataFrame.tz_convert
   DataFrame.tz_localize

.. _api.frame.flags:

Flags
~~~~~

Flags refer to attributes of the pandas object. Properties of the dataset (like
the date is was recorded, the URL it was accessed from, etc.) should be stored
in :attr:`DataFrame.attrs`.

.. autosummary::
   :toctree: api/

   Flags


.. _api.frame.metadata:

Metadata
~~~~~~~~

:attr:`DataFrame.attrs` is a dictionary for storing global metadata for this DataFrame.

.. warning:: ``DataFrame.attrs`` is considered experimental and may change without warning.

.. autosummary::
   :toctree: api/

   DataFrame.attrs


.. _api.dataframe.plotting:

Plotting
~~~~~~~~
``DataFrame.plot`` is both a callable method and a namespace attribute for
specific plotting methods of the form ``DataFrame.plot.<kind>``.

.. autosummary::
   :toctree: api/
   :template: autosummary/accessor_callable.rst

   DataFrame.plot

.. autosummary::
   :toctree: api/
   :template: autosummary/accessor_method.rst

   DataFrame.plot.area(x=None, y=None, **kwargs)绘制堆积面积图。 面积图直观地显示定量数据。
   DataFrame.plot.bar(x=None, y=None, **kwargs) 制作垂直条形图
   DataFrame.plot.barh(x=None, y=None, **kwargs) 制作水平条形图
   DataFrame.plot.box(by=None, **kwargs) 制作 DataFrame 列的箱线图。 箱线图是一种通过四分位数以图形方式描绘数值数据组的方法。
   DataFrame.plot.density使用高斯核生成核密度估计图
   DataFrame.plot.hexbin (x, y, C=None, reduce_C_function=None, gridsize=None, **kwargs) 生成六边形分箱图
   DataFrame.plot.hist(by=None, bins=10, **kwargs) 绘制一个 DataFrame 列的直方图
   DataFrame.plot.kde(bw_method=None, ind=None, **kwargs) 使用高斯核生成核密度估计图
   DataFrame.plot.line(x=None, y=None, **kwargs) 将 Series 或 DataFrame 绘制为线条
   DataFrame.plot.pie生成饼图
   DataFrame.plot.scatter(x, y, s=None, c=None, **kwargs) 创建具有不同标记点大小和颜色的散点图

.. autosummary::
   :toctree: api/

   DataFrame.boxplot
   DataFrame.hist


.. _api.frame.sparse:

Sparse accessor
~~~~~~~~~~~~~~~

Sparse-dtype specific methods and attributes are provided under the
``DataFrame.sparse`` accessor.

.. autosummary::
   :toctree: api/
   :template: autosummary/accessor_attribute.rst

   DataFrame.sparse.density

.. autosummary::
   :toctree: api/
   :template: autosummary/accessor_method.rst

   DataFrame.sparse.from_spmatrix
   DataFrame.sparse.to_coo
   DataFrame.sparse.to_dense


Serialization / IO / conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autosummary::
   :toctree: api/

   DataFrame.from_dict
   DataFrame.from_records
   DataFrame.to_orc
   DataFrame.to_parquet
   DataFrame.to_pickle
   DataFrame.to_csv
   DataFrame.to_hdf
   DataFrame.to_sql
   DataFrame.to_dict
   DataFrame.to_excel
   DataFrame.to_json
   DataFrame.to_html
   DataFrame.to_feather
   DataFrame.to_latex
   DataFrame.to_stata
   DataFrame.to_gbq
   DataFrame.to_records
   DataFrame.to_string
   DataFrame.to_clipboard
   DataFrame.to_markdown
   DataFrame.style
   DataFrame.__dataframe__