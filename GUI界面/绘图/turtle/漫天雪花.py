# -- coding: utf-8 --
from turtle import *  # 导入turtle标准库
from random import *  # 导入random标准库


def snow():
    hideturtle()  # 隐藏画笔
    speed(10)  # 设置画笔移动速度为10
    pensize(2)  # 设置画笔大小为2
    # 利用for循环绘制雪花
    for i in range(100):
        r = random()  # 设置r为0~1之间的随机数
        g = random()
        b = random()
        pencolor(r, g, b)  # 设置画笔的颜色
        penup()  # 抬笔
        setx(randint(-350, 350))  # 设置x坐标为-350~350的随机数
        sety(randint(-150, 270))  # 设置y坐标为-50~270的随机数
        pendown()  # 落笔
        dens = randint(8, 12)  # 设置dens为8~12的随机数
        snowsize = randint(10, 14)  # 设置snowsize为10~14的随机数
        for j in range(dens):
            forward(snowsize)  # 画笔向前移动snowsize像素
            backward(snowsize)  # 画笔向后移动snowsize像素
            right(360 / dens)  # 顺时针旋转360/dens度


def ground():
    hideturtle()  # 隐藏画笔
    speed(10)  # 设置画笔移动速度为10
    # 利用for循环绘制地面
    for i in range(300):
        pensize(randint(5, 10))  # 设置画笔大小为5~10的随机数
        x = randint(-400, 350)  # 设置x坐标为-400~350的随机数
        y = randint(-280, -150)  # 设置y坐标为-280~-150的随机数
        r = -y / 280
        g = -y / 280
        b = -y / 280
        pencolor(r, g, b)  # 设置画笔的颜色
        penup()  # 抬笔
        goto(x, y)  # 画笔移动到（x,y）坐标处
        pendown()  # 落笔
        forward(randint(40, 100))  # 画笔向前移动40~100像素随机数


def main():
    setup(800, 600, 0, 0)  # 设置画布大小及左上角位置
    tracer(False)  # 打开/关闭龟动画，并为更新图纸设置延迟
    bgcolor("black")  # 设置背景颜色为黑色
    snow()  # 调用snow()函数，绘制雪花
    ground()  # 调用ground()函数，绘制地面
    tracer(True)
    done()


main()  # 调用main()主函数
