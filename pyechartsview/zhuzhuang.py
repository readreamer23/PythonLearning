from pyecharts import Bar

#柱状图示例
attr = ["衬衫", "羊毛衫", "雪纺衫", "电视", "手机", "手电筒"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)

#生成Html网页文件显示柱状图
bar.render("render_zhu.html")
