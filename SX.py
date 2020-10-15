from pyecharts.charts import Bar, Line, Grid


# 1. 准备数据
from pyecharts import options

cate = ["湖北", "四川", "重庆", "河北", "云南"]
Confirmed_diagnosis_data = [450, 300, 232, 224, 144]
death_data = [50, 30, 22, 24, 44]

# 2. 创建图表对象

line = Line()
line.add_xaxis(cate)
line.add_yaxis("quezhen人数", Confirmed_diagnosis_data)
line.add_yaxis("siwang人数", death_data)
# legend_opts : 以容器line顶部为开始，控制line的图例位置在容器line宽度的3%处
line.set_global_opts(title_opts=options.TitleOpts(title="线性图"),legend_opts=options.LegendOpts(pos_top="3%"))



bar = Bar()
bar.add_xaxis(cate)
bar.add_yaxis("确诊人数", Confirmed_diagnosis_data)
bar.add_yaxis("死亡人数", death_data)
# pos_top : 以容器line顶部为开始，控制标题的位置在容器line宽度的50%处
bar.set_global_opts(title_opts=options.TitleOpts(title="柱状图",pos_top='100%'),legend_opts=options.LegendOpts(pos_top="55%"))


# 3. 创建组合类对象
grid = Grid()

# 4. 在组合对象中添加需要组合的图表对象
grid.add(line, grid_opts=options.GridOpts(pos_bottom="60%"))
grid.add(bar, grid_opts=options.GridOpts(pos_top="60%"))

# 5. 渲染数据
grid.render("a.html")