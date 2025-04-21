from turtle import Screen
from player import Player
from board import Board
from ball import Ball
import time


# ---------------------- Setup Functions ----------------------
def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Pong Game")
    screen.tracer(0)
    return screen


# ---------------------- Main ----------------------
def main():
    screen = setup_screen()
    screen.listen()
    game_is_on = True
    board = Board()

    player1 = Player(-280, 20)
    screen.onkey(player1.up, "w")
    screen.onkey(player1.down, "s")

    player2 = Player(280, 20)
    screen.onkey(player2.up, "Up")
    screen.onkey(player2.down, "Down")

    ball = Ball()
    board.write(player1.score)
    while game_is_on:
        screen.update()
        time.sleep(0.01)
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.dy *= -1
        if ball.distance(player1) < 50 and ball.xcor() < -260:
            ball.dx *= -1
        if ball.distance(player2) < 50 and ball.xcor() > 260:
            ball.dx *= -1

        # Right player missed
        if ball.xcor() > 300:
            player1.score += 1
            board.write(player1.score, player2.score)
            ball.goto(0, 0)
            ball.dx *= -1

        # Left player missed
        if ball.xcor() < -300:
            player2.score += 1
            board.write(player1.score, player2.score)
            ball.goto(0, 0)
            ball.dx *= -1

        if board.end_game(player1.score,player2.score):
            game_is_on = False
    screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
