from turtle import Turtle, Screen, colormode
import random
from time import sleep
import colorgram

# ---------------------- Setup ----------------------
screen = Screen()
colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red", "green")
timmy.pensize(1)
timmy.speed("fastest")

# ---------------------- Constants ----------------------
COLOURS = [
    "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
    "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
]
DIRECTIONS = [0, 90, 180, 270]


# ---------------------- Functions ----------------------
def select_color(rgb=True):
    """
    Selects a random color.
    If rgb is True, returns a random RGB tuple.
    If False, returns a random color name from COLOURS.
    """
    if rgb:
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return random.choice(COLOURS)


def draw_random_walk(steps=200, distance=30):
    """
    Draws a random walk using the turtle.
    """
    for _ in range(steps):
        color = select_color(rgb=False)
        timmy.pencolor(color)
        timmy.fillcolor(color)
        timmy.setheading(random.choice(DIRECTIONS))
        timmy.forward(distance)
        sleep(0.05)


def draw_spirograph(circles=36, radius=100):
    """
    Draws a spirograph pattern with the turtle.
    """
    for _ in range(circles):
        timmy.pencolor(select_color(rgb=False))
        timmy.circle(radius)
        timmy.left(360 / circles)


def draw_dots_grid(rows=10, cols=10, distance=30, dots_size=20):
    timmy.penup()
    timmy.hideturtle()
    timmy.speed("fastest")
    start_x = timmy.xcor()
    start_y = timmy.ycor()

    for j in range(rows):
        for i in range(cols):
            random_color = select_color(True)
            timmy.dot(dots_size, random_color)
            timmy.forward(distance)

        timmy.setx(start_x)
        timmy.sety(start_y + (j + 1) * distance)


# ---------------------- Color Extraction ----------------------
colors_in_img = colorgram.extract('images.png', 10)

print("Extracted Colors:")
for color in colors_in_img:
    print(color.rgb)

# ---------------------- Drawing ----------------------
# draw_random_walk()
# draw_spirograph()
draw_dots_grid()
# ---------------------- End Program ----------------------
screen.exitonclick()
