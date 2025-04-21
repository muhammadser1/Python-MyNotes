import random
from time import sleep
from turtle import Turtle

width = 600
height = 600


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.goto(random.randint(-width // 2 + 20, width // 2 - 20),
                  random.randint(-height // 2 + 20, height // 2 - 20))
        self.speed("fastest")

    def move_random(self):
        new_x = random.randint(-width // 2 + 20, width // 2 - 20)
        new_y = random.randint(-height // 2 + 20, height // 2 - 20)
        self.goto(new_x, new_y)
