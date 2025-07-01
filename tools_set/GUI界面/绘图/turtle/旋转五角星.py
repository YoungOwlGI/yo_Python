import turtle
import cv2

# 设置画图速度为最快
turtle.speed("fastest")

# 设置画笔宽度为1
turtle.pensize(1)

# 设置画笔颜色为红色
turtle.pencolor("#496d89")

# 开始循环，循环次数为2000次
for y in range(2000):
    # 向前移动的距离随着y的增加而增加，这里乘以3是为了让移动距离变化更快
    turtle.forward(3 * y)

    # 向左转20度
    turtle.left(20)

    # 由于之前的左转，这里向右转175度是为了调整方向，使得下次循环时能够正确移动
    # 注意：左转20度后再右转175度，相当于左转5度（因为180度-175度=5度）
    # 如果你想让海龟回到原始的前进方向，你应该左转或右转180度
    turtle.right(175)

# 如果需要，可以添加结束画图的命令，例如隐藏海龟
turtle.hideturtle()

# 等待用户关闭窗口
turtle.done()
