# 导入要使用的模块
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType


# 将每个图 封装到 函数

# 1.条形图
def bar_datazoom_slider() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add_xaxis(Faker.days_attrs)
            .add_yaxis("思明区", Faker.days_values)
            .add_yaxis("湖里区", Faker.days_values)
            .add_yaxis("集美区", Faker.days_values)
            .add_yaxis("海沧区", Faker.days_values)
            .add_yaxis("同安区", Faker.days_values)
            .add_yaxis("翔安区", Faker.days_values)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


# 2.带标记点的折线图
def line_markpoint() -> Line:
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))

            .add_xaxis(Faker.choose())
            .add_yaxis(
            "商家A",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
        )
            .add_yaxis(
            "商家B",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint"))
    )
    return c


# 3.玫瑰型饼图
def pie_rosetype() -> Pie:
    v = Faker.choose()
    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))

            .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )

            .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
    )
    return c


# 表格
def table_base() -> Table:
    table = Table()

    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    rows = [
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Adelaide", 1295, 1158259, 600.5],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="Table")
    )
    return table


def page_simple_layout():
    page = Page(layout=Page.DraggablePageLayout)
    # 将上面定义好的图添加到 page
    page.add(
        bar_datazoom_slider(),
        line_markpoint(),
        pie_rosetype(),
        table_base(),)

    page.render("page_simple_layout.html")


if __name__ == "__main__":
    page_simple_layout()