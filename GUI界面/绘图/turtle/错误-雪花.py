import tkinter as tk
import turtle
import random
import math


class Snow():
    def __init__(self, t):
        self.t = t
        self.r = 6  # 雪花的半径
        self.reset()  # 初始化雪花属性

    def draw(self):
        # 绘制雪花形状，确保不超出边界
        if self.y > 250:  # 只绘制在可视区域内
            self.t.pensize(self.outline)
            self.t.penup()
            self.t.goto(self.x, self.y)
            self.t.pendown()
            self.t.color(self.color)

            # 绘制雪花的形状
            for _ in range(6):  # 雪花有6个分支
                self.t.forward(self.r)
                self.t.backward(self.r)
                self.t.right(60)  # 每个分支旋转60度

    def move(self):
        if self.y >= -500:
            self.y -= self.speed
            self.x -= self.speed * math.sin(self.f)
            self.f -= 0.1
        else:
            self.reset()

    def reset(self):
        self.x = random.randint(-250, 250)  # 限制在绘制范围内
        self.y = random.randint(500, 1000)  # 从更高的地方开始
        self.f = random.uniform(-math.pi, math.pi)
        self.speed = random.randint(8, 15)  # 增加速度范围
        self.color = random.choice(colors)
        self.outline = random.randint(1, 3)  # 随机轮廓宽度


# 更加偏蓝的背景颜色
colors = ["white", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow"]
background_color = "#87CEEB"  # 天空蓝

if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(master=root, width=500, height=500, bg=background_color)
    canvas.pack()
    screen = turtle.RawTurtle(canvas=canvas)
    screen.hideturtle()
    screen.speed(0)
    screen.penup()

    # 增加雪花的数量
    num_snowflakes = 100  # 增加到100个雪花
    snowflakes = [Snow(screen) for _ in range(num_snowflakes)]

    def animate():
        screen.clear()  # 在每次绘制之前清除之前的内容
        for snowflake in snowflakes:
            snowflake.move()
            snowflake.draw()
        root.after(30, animate)  # 每30毫秒调用一次 animate

    animate()
    root.mainloop()
