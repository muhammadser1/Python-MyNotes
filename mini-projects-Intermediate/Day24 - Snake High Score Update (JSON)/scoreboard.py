from turtle import Turtle
import json

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


def save_high_score(score):
    data = {
        "high_score": score
    }
    with open("score_data.json", "w") as file:
        json.dump(data, file)


def load_high_score():
    try:
        with open("score_data.json") as file:
            data = json.load(file)
            return data["high_score"]
    except FileNotFoundError:
        return 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.high_score = load_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        print(self.high_score)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        if self.score > self.high_score:
            save_high_score(self.score)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
