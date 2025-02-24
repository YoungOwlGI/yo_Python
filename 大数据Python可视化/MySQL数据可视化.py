"""
尚未完成制作，敬请期待
"""

import pymysql
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie

# 连接到 MySQL 数据库
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='xiaomty',
    database='yo_economy'
)

# 查询数据
query = "SELECT * FROM DOP财产分割"
data = pd.read_sql(query, connection)

# 获取不同财产所在的财产总和，忽略负值
property_locations = data['平台'].unique()
property_sums = []
for location in property_locations:
    values = data[data['平台'] == location]['财产']
    positive_values = [v for v in values if v >= 0]
    if positive_values:
        property_sums.append(sum(positive_values))
    else:
        property_sums.append(0)

print(property_sums)

# 创建饼状图数据和标签
sizes = property_sums
labels = property_locations

# 使用 pyecharts 绘制饼状图
pie = (
    Pie()
    .add("", [list(z) for z in zip(labels, sizes)])
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    .set_global_opts(title_opts=opts.TitleOpts(title="不同财产所在的财产比例"))
)

# 渲染图表，默认会在浏览器中打开
pie.render("property_distribution.html")
