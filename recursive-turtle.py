import turtle

bob = turtle.Turtle()

bob.speed(5) # Speed ranges from 0 - 10. Change value to fasten the process.

bob.color('#ffb3ff', 'blue') 

def draw_star(turt, length):

    if length < 15 : # set as 15 after several test runs
        return

    else:
        bob.begin_fill()
        for i in range(5):
            turt.forward(length)
            draw_star(turt, length/3) # set as 3 after several test runs
            turt.right(144) # or turt.left(216)
        bob.end_fill()
    
draw_star(bob, 400)

bob.hideturtle()

turtle.done()