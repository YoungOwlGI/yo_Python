import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel('某公司产品销售数据.xlsx')

df = df.groupby('地区').sum(numeric_only=True)

sns.set_style(style='ticks', rc={'font.sans-serif': 'SimHei',
                                 "axes.edgecolor": "0.15", "figure.facecolor": "0.96"})
sns.set_palette(sns.color_palette('husl', 8))

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(y=df.index, x=df['销售额（万元）'], ax=ax)  # 交换 x 和 y 参数

ax.set_ylabel('地区')
ax.set_xlabel('销售额（万元）')

for p in ax.patches:
    ax.annotate(int(p.get_width()),
                (p.get_width(), p.get_y() + p.get_height() / 2),
                ha='center', va='center',
                xytext=(10, 0), textcoords='offset points')

plt.title('某公司产品销售数据-----寇亚杰-小猫头鹰')
plt.show()
