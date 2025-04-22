import time
from turtle import Screen
from player import Player
from carManager import CarManager
from board import Scoreboard


def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("white")
    screen.title("Crossing Game")
    screen.tracer(0)
    return screen


# ---------------------- Main ----------------------
def main():
    screen = setup_screen()
    screen.listen()

    player = Player()
    car_manager = CarManager()

    board = Scoreboard()
    screen.onkey(player.up, "w")

    game_is_on = True
    while game_is_on:
        time.sleep(0.05)
        screen.update()

        car_manager.maybe_create_car()
        car_manager.move()
        car_manager.reset()

        if car_manager.check_collision(player):
            board.game_over()
            game_is_on = False

        if player.is_winner():
            board.increase_level()
            player.goto(0, -280)
            car_manager.increase_speed()

    screen.exitonclick()


if __name__ == "__main__":
    main()
