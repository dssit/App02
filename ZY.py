from pyecharts import Bar, Line, Grid


# 1. 准备数据
from pyppeteer import options

# 1. 准备数据
cate = ["湖北", "四川", "重庆", "河北", "云南"]
Confirmed_diagnosis_data = [450, 300, 232, 224, 144]
death_data = [50, 30, 22, 24, 44]

# 2. 创建图表对象
bar = Bar()
bar.add_xaxis(cate)
bar.add_yaxis("确诊人数", Confirmed_diagnosis_data)
bar.add_yaxis("死亡人数", death_data)
bar.set_global_opts(title_opts=options.TitleOpts(title="柱状图",pos_left="51%"),legend_opts=options.LegendOpts(pos_left="60%"))

line = Line()
line.add_xaxis(cate)
line.add_yaxis("确诊人数", Confirmed_diagnosis_data)
line.add_yaxis("死亡人数", death_data)
# bug 这里控制不了图例的类型
line.set_global_opts(title_opts=options.TitleOpts(title="线性图",pos_left="1%"),legend_opts=options.LegendOpts(pos_left="10%"))


# 3. 创建组合类对象
grid = Grid()

# 4. 在组合对象中添加需要组合的图表对象
grid.add(bar, grid_opts=options.GridOpts(pos_left="55%"))
grid.add(line, grid_opts=options.GridOpts(pos_right="55%"))

# 5. 渲染数据
grid.render_notebook()