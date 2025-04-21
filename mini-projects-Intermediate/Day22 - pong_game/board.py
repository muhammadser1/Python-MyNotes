from turtle import Turtle

width = 600
height = 600


class Board:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.writer = Turtle()
        self.writer.hideturtle()
        self.writer.color("white")
        self.writer.pendown()
        self.writer.goto(-20, 0)

    def write(self, score1, score2=0):
        self.writer.clear()
        self.writer.penup()
        self.writer.goto(-30, 260)
        self.writer.write(f"{score1}", align="center", font=("Courier", 20, "normal"))
        self.writer.penup()
        self.writer.goto(30, 260)
        self.writer.write(f"{score2}", align="center", font=("Courier", 20, "normal"))
        self.writer.penup()
        self.writer.goto(0, 260)
        self.writer.pendown()
        self.writer.goto(0, -260)

    def end_game(self, score1, score2):
        if score1 == 5:
            self.writer.clear()
            self.writer.write(f"The winner is player 1", align="center", font=("Courier", 20, "normal"))
            return True
        elif score2 == 5:
            self.writer.clear()
            self.writer.write(f"The winner is player 2", align="center", font=("Courier", 20, "normal"))
            return True
        return False
