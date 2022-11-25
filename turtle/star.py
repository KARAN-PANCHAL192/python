import turtle
t=turtle.Pen()
color=("yellow","red","green","purple")
turtle.bgcolor("black")
for i in range(450):
    t.pencolor(color[i%4])
    t.forward(i)
    t.left(150)
    t.speed(50)
exitonclick()
    