import turtle

# 初始化turtle
window = turtle.Screen()
window.bgcolor("white")
love = turtle.Turtle()
love.speed(1)  # 较快的速度
love.color("red")


# 绘制爱心的函数（与上一个示例相同）
def draw_heart(x_start, y_start, size):
    window_half = window.window_width() / 2
    love.penup()
    love.goto(x_start, y_start)  # 移动到起始位置
    love.pendown()
    love.begin_fill()  # 开始填充颜色

    # 绘制爱心左边的曲线
    love.left(140)
    love.forward(size)
    love.circle(-size / 2, 200)  # 绘制一个200度的圆弧
    love.left(120)
    love.circle(-size / 2, 200)  # 绘制另一个200度的圆弧

    # 绘制爱心右边的曲线
    # love.forward(size)
    # love.right(140)
    # love.circle(size / 2, 200)  # 绘制一个200度的圆弧
    # love.right(120)
    # love.circle(size / 2, 200)  # 绘制另一个200度的圆弧

    # 填充颜色并结束填充
    love.end_fill()


# 绘制爱心
# draw_heart(0, -window.window_height() / 2 + 100, 100)  # 根据窗口大小调整起始位置和大小
draw_heart(-50, -50, 200)
# 结束绘制，等待用户关闭窗口
turtle.done()