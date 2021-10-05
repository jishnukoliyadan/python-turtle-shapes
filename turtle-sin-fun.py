import turtle
from math import sin

bob = turtle.Turtle()

bob.speed(5) # Speed ranges from 0 - 10. Change value to fasten the process.

bob.color('#ff00ff') # Hex color code for 'magenta'

for i in range(3310): # Decided 3310 as the range after running couple of 
                      # randomly valued tests
    bob.forward(10)
    bob.left(sin(i/10)*30)
    bob.left(20)

turtle.done()