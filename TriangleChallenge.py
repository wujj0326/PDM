import turtle
radius = 200
length = radius * 1.7321
theta=1
def triangle(col):
    radius = 200
    length = radius * 1.7321
    trian.color(col)
    trian.right(30)
    trian.penup()
    trian.backward(radius)
    trian.left(theta)
    radius=radius*0.9709
    length=radius*1.7321
    trian.forward(radius)
    trian.left(150)
    trian.pendown()
    trian.forward(length)
    for i in range(2):
        trian.left(120)
        trian.forward(length)

#Draw the first triangle

trian = turtle.Turtle()
trian.penup()
trian.left(90)
trian.forward(radius)
trian.left(150)
trian.pendown()

trian.forward(length)
for i in range(2):
    trian.left(120)
    trian.forward(length)

for i in range(20):
    triangle("red")
    triangle("orange")
    # triangle("yellow",radius,length)
    # triangle("green",radius,length)
    # triangle("blue",radius,length)
    # triangle("darkblue",radius,length)
    # triangle("purple",radius,length)

turtle.done()