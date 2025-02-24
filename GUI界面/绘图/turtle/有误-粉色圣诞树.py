from turtle import *

# 初始化设置
setup(500, 700)
screensize(bg="wheat")
pencolor("#01863f")  # 设定笔的颜色
pensize(12)  # 设定笔的粗细
speed("fastest")  # 设置绘图速度为最快

# 定义画笔起点
x_start = 0
y_start = 260
circle_radius = 12  # 红色圆圈的半径


def draw_layer(x, y, angle, num_segments, length):
    """绘制圣诞树的层"""
    penup()
    goto(x, y)
    seth(angle)  # 设置初始角度
    pendown()
    for _ in range(num_segments):
        fd(length)  # 向前移动指定长度
        # 依据角度偏移
        if angle < 0:
            right(2)  # 向右偏移2度
        else:
            left(2)  # 向左偏移2度


def draw_zigzag(x, y, angle, num_iterations, segment_length):
    """绘制折线"""
    penup()
    goto(x, y)
    pendown()
    for _ in range(num_iterations):
        seth(angle)
        for _ in range(5):
            fd(segment_length)  # 画出指定长度的线段
        seth(-angle)  # 切换方向


def draw_circle(x, y, radius):
    """绘制圆圈"""
    penup()
    goto(x, y)
    pendown()
    fillcolor("red")
    begin_fill()
    circle(radius)  # 画圈
    end_fill()


def draw_tree():
    """绘制整棵树"""
    # 绘制树的层
    draw_layer(x_start, y_start, -120, 12, 10)
    draw_layer(x_start, y_start, -60, 12, 10)
    draw_zigzag(x_start - 79, y_start - 94, -40, 2, 10)

    # 继续添加其他层的绘制
    draw_layer(x_start - 50, y_start - 122, -120, 8, 10)
    draw_layer(x_start + 50, y_start - 122, -60, 8, 10)
    draw_zigzag(x_start - 106, y_start - 185, -45, 3, 10)

    draw_layer(x_start - 80, y_start - 220, -120, 8, 10)
    draw_layer(x_start + 80, y_start - 220, -60, 8, 10)
    draw_zigzag(x_start - 135, y_start - 283, -48, 4, 10)

    draw_layer(x_start - 120, y_start - 310, -120, 8, 10)
    draw_layer(x_start + 120, y_start - 310, -60, 8, 10)
    draw_zigzag(x_start - 170, y_start - 373, -46, 5, 10)


def draw_trunk():
    """绘制树干"""
    penup()
    fillcolor("#5f3c23")
    pencolor("#5f3c23")
    goto(-25, -135)
    pendown()
    begin_fill()
    seth(-90)
    fd(100)
    seth(0)
    fd(50)
    seth(90)
    fd(100)
    end_fill()


# 绘制圣诞树及其装饰
draw_tree()
draw_trunk()

# 绘制红色圆圈
draw_circle(x_start - 72, y_start - 103, circle_radius)
draw_circle(x_start - 30, y_start - 133, circle_radius)
draw_circle(x_start + 43, y_start - 132, circle_radius)

hideturtle()  # 隐藏海龟
done()  # 结束绘制
