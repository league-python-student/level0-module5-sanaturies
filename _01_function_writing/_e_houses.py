"""
Have the turtle draw a row of houses.
"""
from tkinter import messagebox, simpledialog, Tk

import turtle
t=turtle.Turtle()
import random
if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    t.speed(2)
    t.color('green')
    t.pencolor('blue')
    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.
    def draw_house(h):
       x=turtle.window_width()
       for i in range(4):
           t.forward(h)
           t.left(90)
       t.pencolor('green')
       t.goto(-x/2,0)
       t.forward(x)
    rand=random.randint(0,250)
  #  draw_house(rand)

    def roof():
        t.penup()
        t.goto(0,250)
        t.pendown()
        for i in range(3):
            t.forward(250)
            t.left(120)
        t.penup()

    def draw_house2(size):
        x=turtle.window_width()
        if size=='small':
            for i in range(4):
               t.forward(100)
               t.left(90)
            t.pencolor('green')
            t.goto(-x/2,0)
            t.forward(x)
        elif size=='medium':
            for i in range(4):
                   t.forward(120)
                   t.left(90)
            t.pencolor('green')
            t.goto(-x/2,0)
            t.forward(x)
        elif size=='large':
            for i in range(4):
                   t.forward(250)
                   t.left(90)
            roof()
            t.pencolor('green')
            t.goto(-x/2,0)
            t.pendown()
            t.forward(x)
        else:
            t.write('follow directions')
    draw_house2('large')
    turtle.done()