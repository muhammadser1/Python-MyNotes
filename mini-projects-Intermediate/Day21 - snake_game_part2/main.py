from turtle import Turtle, Screen, colormode
from snake import Snake
from board import Board
from food import Food
import time


# ---------------------- Setup Functions ----------------------
def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    return screen


# ---------------------- Main ----------------------
def main():
    board = Board()

    screen = setup_screen()
    snake = Snake()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    game_is_on = True
    food = Food()
    food.move_random()
    board.write()
    while game_is_on:
        if snake.has_collided_with_self():
            game_is_on = False
            board.write_end()
        if snake.has_hit_wall():
            game_is_on = False
            board.write_end()
        if snake.is_collision_with(food):
            board.increase_score()
            food.move_random()
            snake.create_new_snake()
        screen.update()
        time.sleep(0.1)

        snake.move()

    screen.exitonclick()


if __name__ == "__main__":
    main()
