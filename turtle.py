import turtle
li = turtle.Turtle()
li.screen.bgcolor("black")
li.pensize(5)
li.color("green")
li.left(-90)
li.backward(90)
li.speed(50000)
li.shape("turtle")

def love(li):
    if li<50:
     return
    else:
     li.forward(li)
     li.color("yellow")
     li.circle(90)
     li.color("green")
     li.left(90)
     
     love(3*li/4)

    li.right(90)
    love(3*li/4)
    li.left(30)
    li.backward(li)
    love(90)
turtle.done()
