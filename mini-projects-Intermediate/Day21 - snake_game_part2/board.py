from turtle import Turtle

width = 600
height = 600


class Board:
    def __init__(self):
        self.score = 0
        self.writer = Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.color("white")
        y = height // 2 - 30
        self.writer.goto(0, y)

    def write(self):
        self.writer.clear()
        self.writer.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))

    def write_end(self):
        self.writer.clear()
        self.writer.write(f"Your Final score is : {self.score} , You Lose", align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.write()