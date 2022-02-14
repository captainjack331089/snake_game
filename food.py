from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.65, stretch_len=0.65)
        self.penup()
        self.color("yellow")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280,280), random.randint(-280,280))

