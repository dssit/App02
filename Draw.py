# -*- coding: utf-8 -*-

from pyecharts import Map
# 1. 准备数据
def draw_bar(all_list):
    print("开始绘图")
    attr = ["海沧", "湖里", "集美", "思明", "翔安", "同安"]

    v0 = all_list[0]
    v1 = all_list[1]
    v2 = all_list[2]
    v3 = all_list[3]

    # 信阳地图 数据为信阳市下的区县
    attrlist= ["海沧区", "湖里区", "集美区", "思明区", "翔安区", "同安区"]

    map3 = Map("厦门地图", '厦门', width=1600, height=800)
    map3.add("厦门", attrlist, v2, visual_range=[1000, 4000], maptype='厦门', is_visualmap=True, visual_text_color='#000')
    map3.render("厦门租房价格分析地图.html")