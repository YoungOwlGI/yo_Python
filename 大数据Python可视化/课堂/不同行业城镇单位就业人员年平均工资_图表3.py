from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
import pandas as pd
df = pd.read_excel('不同行业城镇单位就业人员年平均工资.xlsx',index_col=0)
df = df.sort_index(axis='columns')
x = df.columns.tolist()
y = df.index.tolist()
    = df.reset_index(drop=True)

df = df.sort_values(by='按行业（元）')
df = df.reset_index(drop=True)
c = (
    Line()
   .add_xaxis(df['金融业'])
   .add_yaxis('平均工资', df['2021年'], is_smooth=True, is_symbol_show=False)
   .set_global_opts(
        title_opts=opts.TitleOpts(title='不同行业城镇单位就业人员年平均工资'),
        xaxis_opts=opts.AxisOpts(name='单位名称'),
        yaxis_opts=opts.AxisOpts(name='平均工资', min_=0, max_=10000),
        datazoom_opts=[opts.DataZoomOpts(range_start=0, range_end=100)],
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,
            type_='piecewise',
            pieces=[
                {'min': 0, 'color': '#f7f7f7'},
                {'min': 1000, 'max': 3000, 'color': '#d94e5d'},
                {'min': 3000, 'color': '#5793f3'},
            ],
            pos_top='10%',
            pos_right='10%',
            range_text=['0', '1000', '3000', '5000'],
            range_color=['#f7f7f7', '#d94e5d', '#5793f3'],
        ),
    )
)
