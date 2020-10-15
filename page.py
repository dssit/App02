# # 2. 创建图表对象
# line = Line(init_opts=opts.InitOpts(width='1000px', height='600px'))
# line.add_xaxis(attr)
# line.add_yaxis("最小值房价", v0)
# line.add_yaxis("最大值房价", v1)
# line.add_yaxis("平均值房价", v2)
# line.add_yaxis("中位数房价", v3)
#
# # legend_opts : 以容器line顶部为开始，控制line的图例位置在容器line宽度的3%处
# line.set_global_opts(title_opts=options.TitleOpts(title="厦门市租房价分析"), legend_opts=options.LegendOpts(pos_top="2%"))
#
# # 设置行名
# columns = attr
#
# # bar是实例对象
# bar = Bar(init_opts=opts.InitOpts(width='1000px', height='600px'))
# # x轴数据
# bar.add_xaxis(xaxis_data=["海沧", "湖里", "集美", "思明", "翔安", "同安"])
#
# data = [1, 2, 5, 6, 8, 6]
#
# # # 第一个参数是图例名称，第二个参数是y轴数据
# bar.add_yaxis(series_name="平均值房价", yaxis_data=data)
# bar.add_yaxis(series_name="最大值房价", yaxis_data=data)
#
# # , , , , ,
# # x轴和y轴转换
# # bar.reversal_axis()
#
# # 设置全局项
# bar.set_global_opts(
#     # 设置表的标题
#     title_opts=opts.TitleOpts(title='不同平台分析表'),
#     # 设置y轴倾斜度
#     yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=60)),
#     # 设置图例is_show=False是不显示图例
#     legend_opts=opts.LegendOpts(is_show=True),
#     # 设置划动
#     datazoom_opts=opts.DataZoomOpts(type_='slider', range_start=0, range_end=1500)
# )
#
# # 3. 创建组合类对象
# grid = Grid()
# # 4. 在组合对象中添加需要组合的图表对象
# grid.add(line, grid_opts=options.GridOpts(pos_bottom="60%"))
# # grid.add(bar, grid_opts=options.GridOpts(pos_top="60%"))
#
# grid.render("厦门市租房分析.html")