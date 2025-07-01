import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
df = pd.read_excel('不同行业城镇单位就业人员年平均工资.xlsx',index_col=0)
df = df.sort_index(axis=1)
x = df.columns
y = df.loc['金融业']
plt.figure(figsize=(10,6))
sns.set_style('whitegrid',rc={'font.sans-serif':'SimHei'})
sns.set_palette(sns.color_palette("Paired", 12))
sns.lineplot(x=x,y=y,marker='o',markersize=5,label='金融业')
plt.xlabel('年份')
plt.ylabel('平均工资')
for i in range(len(x)):
    plt.text(i,y[i]+0.5,y[i],ha='center',va='bottom',fontsize=10)
plt.title('不同行业城镇单位就业人员年平均工资')
plt.show()