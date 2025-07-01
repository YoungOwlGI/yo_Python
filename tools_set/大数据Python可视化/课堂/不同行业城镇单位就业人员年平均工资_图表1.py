import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("TkAgg")
df = pd.read_excel('不同行业城镇单位就业人员年平均工资.xlsx',index_col=0)
x = df.index

y = df['2021年']
plt.figure(figsize=(8,4))
plt.rcParams['font.sans-serif'] = 'SimHei'
# -------------------------------------
plt.title('21年各行业城镇单位平均工资折线图')
plt.ylabel('平均工资')
# 旋转角度
plt.xticks(rotation = 290)
for a,b in zip(x,y):
    plt.text(a,b,'%d'%b,ha = 'right')
plt.plot(x,y,"b-.o")
plt.legend("2021年")
plt.show()