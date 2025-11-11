#Write a program to create a face using OOPs Concepts and Python Turtle, consisting of the following - Face Outline, Mouth, Eyes, and Nose. Keep the turtle pen at a fixed location and keep that as a center and draw all the parts.
from turtle import *
class face:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.position=(self.x,self.y)
    def draw(self):
        penup()
        goto(self.position)
        pensize(3)
        speed(0)
        forward(80)
        pendown()
        left(90)
        circle(100)
        penup()
        goto(self.position)
        forward(30)
        pendown()
        dot(20)
        penup()
        left(90)
        forward(40)
        pendown()
        dot(20)
        penup()
        left(110)
        forward(50)
        pendown()
        dot(30)


        
obj=face(0,0)
obj.draw() 
showturtle()
done()      

           
        