import turtle

length = 450
angle = 170

bob = turtle.Turtle()

bob.speed(5)

bob.hideturtle()

bob.getscreen().bgcolor('#C4FCEF')

bob.color('#DDA0DD','#9370DB') 

bob.begin_fill()

while True:
    bob.forward(length)
    bob.left(angle)
    if abs(bob.pos()) < 1:
        break

bob.end_fill()

turtle.done()