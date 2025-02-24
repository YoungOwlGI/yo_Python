import turtle
# 创建一个turtle对象
t = turtle.Turtle()
# 色彩
t.color("blue")
# 画一个正方形
for _ in range(4):
    t.forward(100)     
    t.right(90)
# 画一个正三角形
for _ in range(3):
    t.forward(100)
    t.right(240)
# 画一个倒三角形
for _ in range(3):
    t.forward(100)
    t.right(120)
# 画一个六边形
for _ in range(6):
    t.forward(100)
    t.right(60)
# 画一个五角星
for _ in range(5):
    t.forward(100)
    t.right(144)
# 画一个其他
for _ in range(300):
    t.forward(2)
    t.right(2)
#圆形
turtle.circle(100)