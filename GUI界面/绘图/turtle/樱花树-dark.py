from turtle import *
from random import *
from math import *


# 定义绘制树的函数
def draw_tree(n, length):
    # 下笔
    pendown()
    # 计算阴影效果的灰度值
    shade = cos(radians(heading() + 45)) / 8 + 0.25
    # 设置笔的颜色
    pencolor(shade, shade, shade)
    # 设置笔的粗细，与递归深度成比例
    pensize(n / 3)
    # 向前移动绘制树枝
    forward(length)

    # 如果递归深度大于0，则继续递归绘制
    if n > 0:
        # 随机生成右分支和左分支的偏转角度
        right_branch_angle = random() * 15 + 10
        left_branch_angle = random() * 15 + 10
        # 计算下一个分支的长度
        next_length = length * (random() * 0.25 + 0.7)
        # 右转一定角度，绘制右分支
        right(right_branch_angle)
        draw_tree(n - 1, next_length)
        # 左转一定角度，绘制左分支
        left(right_branch_angle + left_branch_angle)
        draw_tree(n - 1, next_length)
        # 转回来
        right(left_branch_angle)
    else:
        # 绘制叶子
        right(90)
        # 计算叶子颜色
        leaf_color = cos(radians(heading() - 45)) / 4 + 0.5
        # 设置叶子的颜色
        pencolor(leaf_color, leaf_color * 0.8, leaf_color * 0.8)
        # 画一个圆形作为叶子
        circle(3)
        left(90)

        # 添加飘落叶子的效果
        if random() > 0.7:
            # 抬笔
            penup()
            # 保存当前朝向
            saved_heading = heading()
            # 随机飘落角度
            angle = -40 + random() * 80
            # 设置朝向
            setheading(angle)
            # 随机飘落距离
            distance = int(800 * random() * 0.5 + 400 * random() * 0.3 + 200 * random() * 0.2)
            # 向前移动
            forward(distance)
            # 恢复朝向
            setheading(saved_heading)
            # 下笔
            pendown()
            right(90)
            # 计算飘落叶子颜色
            leaf_color = cos(radians(heading() - 45)) / 4 + 0.5
            # 设置飘落叶子的颜色
            pencolor(leaf_color * 0.5 + 0.5, 0.4 + leaf_color * 0.4, 0.4 + leaf_color * 0.4)
            # 画一个小圆形作为飘落的叶子
            circle(2)
            left(90)
            # 抬笔
            penup()
            # 返回原位置
            setheading(angle)
            backward(distance)
            setheading(saved_heading)
            # 抬笔
    penup()
    # 退回原位置
    backward(length)


# 设置背景色
bgcolor(0.5, 0.5, 0.5)
# 隐藏turtle形状
hideturtle()
# 设置绘制速度为最快
speed(0)
# 关闭动画更新
tracer(1, 0)  # 画图过程不需要延迟
# 初始设置
penup()  # 抬笔
backward(100)  # 后退100
left(90)  # 左转90度
penup()  # 抬笔
backward(300)  # 后退300
# 开始绘制树，递归深度为12，初始长度为100
draw_tree(12, 100)
# 结束绘制
done()