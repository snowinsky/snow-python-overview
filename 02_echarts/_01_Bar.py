from pyecharts import options as opts
from pyecharts.charts import Bar

# 这是一个假数据对象，提供数据
from pyecharts.faker import Faker

x_data = Faker.choose()
y1_data = Faker.values()
y2_data = Faker.values()

renderedAbsPathStr = (  # 把链式调用的代码放在括号里，避免手动加反斜杠
    Bar()
    .add_xaxis(xaxis_data=x_data)  # 给x轴设置数据，数据是list格式的字符串
    .add_yaxis(
        series_name="商家1", y_axis=y1_data
    )  # 给y轴设置数据，数据是list格式的字符串
    .add_yaxis(series_name="商家2", y_axis=y2_data)  # 可以给每个y轴起个名字，这是图例的名字
    .set_global_opts(
        title_opts=opts.TitleOpts(title="这是主标题", subtitle="这是副标题")
    )
    .render("bar_base.html") # 如果是在jupyter notebook当中 render_notebook()
)
# render返回的是生成的html文件的绝对路径
print(renderedAbsPathStr)

# 设置图例的位置和展示格式
# .set_global_opts(
# legend_opts=opts.LegendOpts(type_="scroll", orient="vertical",pos_top="15%",pos_left="7%") # 图裂的位置
# label_opts=opts.LabelOpts(formatter="{b}: {c}") # 结果的展现形式

# 多根柱子叠在一起，而不是顺序排列
# .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

# x轴下面的文字太长可以斜着显示
# .set_global_opts(
#         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=15)),

# 还可以加个滑块，来放大缩小数据
# .set_global_opts(
#         title_opts=opts.TitleOpts(title="Bar-DataZoom（滑块-垂直）"),
#         datazoom_opts=opts.DataZoomOpts(orient="vertical"),
        
# 还可以把数据的放大缩小放在内部或者外部
# .set_global_opts(
#         title_opts=opts.TitleOpts(title="Bar-DataZoom（内置+外置）"),
#         datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
#     )

# 设置柱子之间的空隙
# .add_yaxis("商家1", Faker.values(), gap="0%")

# 柱子不一定要立着，还可以躺着
# .reversal_axis()
#     .set_series_opts(label_opts=opts.LabelOpts(position="right"))

