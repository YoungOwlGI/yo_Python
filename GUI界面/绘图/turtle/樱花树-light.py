from turtle import *  # 导入 Turtle 绘图库的所有功能
from random import random  # 导入 random 模块的 random 函数
from math import cos, radians  # 导入 math 模块的 cos 和 radians 函数


def draw_tree(branch_length, level):
    """递归函数用于绘制树"""
    pd()  # 下笔，开始绘制
    # 根据当前方向和角度计算颜色值
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)  # 设置画笔颜色
    pensize(branch_length / 10)  # 根据分支长度设置画笔粗细
    forward(branch_length)  # 向前移动绘制分支的长度

    if level > 0:  # 如果还有分支级别
        # 随机生成分支的角度和长度
        angle1 = random() * 15 + 10
        angle2 = random() * 15 + 10
        new_length = branch_length * (random() * 0.25 + 0.7)

        # 绘制右侧分支
        right(angle1)
        draw_tree(new_length, level - 1)

        # 绘制左侧分支
        left(angle1 + angle2)
        draw_tree(new_length, level - 1)

        # 返回到原始位置和方向
        right(angle2)
    else:  # 如果已经到达最底层
        # 在分支末端绘制花朵
        draw_flower()

    pu()  # 抬笔，停止绘制
    backward(branch_length)  # 后退到原来的位置


def draw_flower():
    """绘制分支末端的花朵"""
    right(90)  # 调整方向，准备绘制花朵
    pencolor("pink")  # 设置画笔颜色为粉色
    circle(3)  # 绘制花朵

    left(90)  # 调整方向，准备绘制其他元素

    # 偶尔在地面上绘制落花
    if random() > 0.7:  # 根据随机概率决定是否绘制
        pu()  # 抬笔，停止绘制
        current_heading = heading()  # 记录当前方向
        angle = -40 + random() * 80  # 随机生成落花的角度
        setheading(angle)  # 设置方向
        # 计算落花的距离
        distance = int(800 * random() * 0.5 + 400 * random() * 0.3 + 200 * random() * 0.2)
        forward(distance)  # 向前移动到落花位置

        pd()  # 下笔，开始绘制
        right(90)  # 调整方向，准备绘制落花
        # 根据当前方向和角度计算颜色值
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)  # 设置画笔颜色
        circle(2)  # 绘制落花

        left(90)  # 调整方向，准备返回原始位置
        pu()  # 抬笔，停止绘制
        setheading(angle)  # 设置方向
        backward(distance)  # 后退回原始位置
        setheading(current_heading)  # 恢复到原始方向


def main():
    """主函数用于设置绘图环境并开始绘制过程"""
    bgcolor(0.956, 0.9255, 0.9882)  # 设置背景颜色为浅紫色
    speed(10)  # 设置绘制速度
    hideturtle()  # 隐藏 Turtle 笔触
    tracer(100)  # 设置追踪延迟

    pu()  # 抬笔，停止绘制
    backward(100)  # 后退一段距离
    left(90)  # 调整方向
    backward(300)  # 后退一段距离

    draw_tree(100, 12)  # 调用绘制树的函数
    done()  # 完成绘制


if __name__ == "__main__":
    main()  # 执行主函数
