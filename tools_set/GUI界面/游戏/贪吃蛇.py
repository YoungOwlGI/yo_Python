import turtle
import copy
from random import randrange

# 设置蛇的长度
snake = [[0, 0], [0, 10], [0, 20]]
# 蛇移动的方向(默认向上移动)
aim = [0, 10]
# 设置食物
food = [-10, 0]
wn = turtle.Screen()
# 设置标题
wn.title('贪吃蛇游戏')


# 改变蛇移动的方向
def change_direction(x, y):
    aim[0] = x
    aim[1] = y


def square(x, y, size, color):
    # 抬起画笔
    turtle.penup()
    # 画笔痕迹
    turtle.goto(x, y)
    # 放下画笔
    turtle.pendown()
    # 进行渲染
    turtle.color(color)
    turtle.begin_fill()
    # 在画布上画四笔转一圈生成一个方块
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def inside(head):
    return -250 < head[0] < 250 and -250 < head[1] < 250


# 定义蛇的移动的函数
def sanke_move():
    head = copy.deepcopy(snake[-1])
    head = [head[0] + aim[0], head[1] + aim[1]]
    print(head[0], head[1])
    # 判断是否发生了碰撞
    if head in snake or not inside(head):
        print("Game Over!")
        square(head[0], head[1], 10, "red")
        return
    # 判断蛇碰到食物后的操作
    if head == food:
        food[0] = randrange(-15, 15) * 10
        food[1] = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    snake.append(head)
    turtle.clear()
    square(food[0], food[1], 10, "blue")
    # 遍历蛇的列表画出蛇的长度
    for body in snake:
        square(body[0], body[1], 10, "black")
    # 更新，使动画的出现不是那么突兀
    turtle.update()
    turtle.ontimer(sanke_move, 300)


# 设置屏幕的大小
turtle.setup(500, 500)
# 去除一个一个画方块的动画
turtle.tracer(False)
# 去掉箭头（画画用的画笔）
turtle.hideturtle()
# 用来监听键盘（获取键盘的事件）
turtle.listen()
# 用来监听函数(通过控制转向函数达到让蛇转向的目的）
turtle.onkey(lambda: change_direction(0, 10), "Up")
turtle.onkey(lambda: change_direction(0, -10), "Down")
turtle.onkey(lambda: change_direction(-10, 0), "Left")
turtle.onkey(lambda: change_direction(10, 0), "Right")
sanke_move()
# 不让屏幕立马消失
turtle.done()
