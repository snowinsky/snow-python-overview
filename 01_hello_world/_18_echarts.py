#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from pyecharts.charts import Bar
from pyecharts.charts import Bar3D
# 折线图	Line	from pyecharts.charts import Line
# 柱状图	Bar	from pyecharts.charts import Bar
# 散点图	Scatter	from pyecharts.charts import Scatter
# 饼图	Pie	from pyecharts.charts import Pie
# 雷达图	Radar	from pyecharts.charts import Radar
# 热力图	HeatMap	from pyecharts.charts import HeatMap
# K 线图	Kline	from pyecharts.charts import Kline
# 箱线图	Boxplot	from pyecharts.charts import Boxplot
# 地图	Map	from pyecharts.charts import Map
# 词云图	WordCloud	from pyecharts.charts import WordCloud
# 仪表盘	Gauge	from pyecharts.charts import Gauge
# 漏斗图	Funnel	from pyecharts.charts import Funnel
# 树图	Tree	from pyecharts.charts import Tree
# 平行坐标系图	Parallel	from pyecharts.charts import Parallel
# 桑基图	Sankey	from pyecharts.charts import Sankey
# 地理坐标系图	Geo	from pyecharts.charts import Geo
# 时间线图	Timeline	from pyecharts.charts import Timeline
# 3D 散点图	Scatter3D	from pyecharts.charts import Scatter3D
# 3D 柱状图	Bar3D	from pyecharts.charts import Bar3D
# 3D 曲面图	Surface3D	from pyecharts.charts import Surface3D


# 准备数据
x_data = ['一月', '二月', '三月', '四月', '五月']
y_data = [10, 20, 15, 25, 30]

# 创建柱状图
bar_chart = Bar()
bar_chart.add_xaxis(x_data)
bar_chart.add_yaxis("销售额", y_data)

# 也可以传入路径参数，如 bar_chart.render("bar_chart.html")
bar_chart.render("./snow-python-overview/01_hello_world/files/bar_chart.html")