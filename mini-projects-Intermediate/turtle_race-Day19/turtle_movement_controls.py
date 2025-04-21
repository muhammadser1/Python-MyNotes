from turtle import Turtle, Screen, colormode
import random


# ---------------------- Setup ----------------------
def setup_screen():
    screen = Screen()
    colormode(255)
    screen.listen()
    return screen


def create_turtle():
    tim = Turtle()
    tim.shape("turtle")
    tim.color("red", "green")
    tim.pensize(1)
    tim.speed("fastest")
    return tim


# ---------------------- Constants ----------------------
COLOURS = [
    "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
    "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
]
DIRECTIONS = [0, 90, 180, 270]
STEP_SIZE = 10


# ---------------------- Utilities ----------------------
def select_color(rgb=True):
    """
    Selects a random color.
    If rgb is True, returns a random RGB tuple.
    If False, returns a random color name from COLOURS.
    """
    if rgb:
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return random.choice(COLOURS)


# ---------------------- Controls ----------------------
def bind_controls(screen, turtle, step):
    def move_forward():
        turtle.forward(step)

    def move_backward():
        turtle.backward(step)

    def turn_left():
        turtle.setheading(turtle.heading() + step)

    def turn_right():
        turtle.setheading(turtle.heading() - step)

    def clear_and_reset():
        turtle.clear()
        turtle.home()

    screen.onkey(move_forward, "w")
    screen.onkey(move_backward, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(clear_and_reset, "c")


# ---------------------- Main ----------------------
def main():
    screen = setup_screen()
    timmy = create_turtle()
    bind_controls(screen, timmy, STEP_SIZE)
    screen.exitonclick()


if __name__ == "__main__":
    main()
