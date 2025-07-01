import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel("某公司产品销售数据.xlsx")
df = df.groupby("季度").sum(numeric_only=True)

sns.set_style(style="whitegrid", rc={
    "font.sans-serif": "SimHei", "axes.edgecolor": "0.15", "figure.facecolor": "0.96"})

plt.figure(figsize=(10, 6))
sns.barplot(x="季度", y="销售额（万元）", data=df, palette="Blues_d", hue="季度", legend=False)  # 加入 hue 参数

plt.title("某公司产品销售数据-----寇亚杰-小猫头鹰")
plt.xlabel("季度")
plt.ylabel("销售额（万元）")

for index, row in df.iterrows():
    plt.text(index, row["销售额（万元）"], f'{row["销售额（万元）"]:.0f}', ha='center')

plt.show()
