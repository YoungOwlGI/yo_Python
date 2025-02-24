import turtle
import random

# 设置画布
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Flower Art")

# 创建画笔
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


# 绘制花朵函数
def draw_flower(x, y, radius, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)

    # 绘制一个花朵
    for _ in range(36):  # 绘制36个花瓣
        pen.circle(radius)
        pen.right(10)  # 每次旋转10度


# 绘制花茎函数
def draw_stem(x, y, length, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(270)  # 设置方向向下
    pen.pendown()
    pen.color(color)
    pen.pensize(2)
    pen.forward(length)


# 随机生成花朵和茎
for _ in range(20):  # 绘制20朵花
    # 随机位置
    x = random.randint(-300, 300)
    y = random.randint(0, 300)

    # 随机半径、颜色和茎长度
    radius = random.randint(10, 50)
    flower_color = random.choice(["red", "blue", "green", "yellow", "purple", "pink", "orange"])
    stem_length = random.randint(50, 200)
    stem_color = random.choice(["green", "darkgreen", "lightgreen"])

    # 绘制花朵和茎
    draw_flower(x, y, radius, flower_color)
    draw_stem(x, y - radius, stem_length, stem_color)

# 关闭窗口
screen.mainloop()
