from pyecharts import Map
# 区县 -- 具体城市内的区县  xx县
quxian = ['思明区', '湖里区', '集美区', '海沧', '同安', '翔安区']
values3 = [3, 5, 7, 8, 2, 4, ]


# 信阳地图 数据为信阳市下的区县
map3 = Map("厦门地图", '厦门', width=1600, height=800)
map3.add("厦门", quxian, values3, visual_range=[1, 10], maptype='厦门', is_visualmap=True, visual_text_color='#000')
map3.render("厦门地图.html")