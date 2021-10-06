"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle


if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    def square(x):
        t=turtle.Turtle()
        window = turtle.Screen()
        window.bgcolor('white')
        for i in range(4):
            t.forward(x)
            t.right(90)
        turtle.done()

    def triangle(x):
        t=turtle.Turtle()
        window = turtle.Screen()
        window.bgcolor('white')
        t.speed(10)
        for i in range(3):
            t.right(120)
            t.forward(x)
        turtle.done()

    def circle(x):
        t=turtle.Turtle()
        window = turtle.Screen()
        window.bgcolor('white')
        t.circle(x,30)
        turtle.done()

    def put():
        shape=input('what shape to draw?')
        if shape=='square':
            x=input('x=')
            x=int(x)
            square(x)
        elif shape=='triangle':
            x=input('x=')
            x=int(x)
            triangle(x)
        elif shape=='circle':
            x=input('x=')
            y=input('y=')
            x=int(x)
            y=int(y)
            circle(x,y)
        else:
            return False
    put()
    
