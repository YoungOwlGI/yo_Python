import turtle
turtle.speed(1)
turtle.pensize(4)

turtle.color('black', 'black')
turtle.begin_fill()
#右中圆
turtle.circle(50,180)
#左大圆
turtle.circle(100,180)
#左中圆
turtle.left(180)
turtle.circle(-50,180)
turtle.end_fill()

turtle.color('white', 'white')
turtle.begin_fill()
#上小圆
turtle.left(90)
turtle.penup()
turtle.forward(35)
turtle.right(90)
turtle.pendown()
turtle.circle(15)
turtle.end_fill()

turtle.color('black', 'black')
turtle.begin_fill()
#下小圆
turtle.left(90)
turtle.penup()
turtle.backward(70)
turtle.pendown()
turtle.left(90)
turtle.circle(15)
turtle.end_fill()

#右大圆
turtle.right(90)
turtle.up()
turtle.backward(65)
turtle.right(90)
turtle.down()
turtle.circle(100, 180)

turtle.done()
