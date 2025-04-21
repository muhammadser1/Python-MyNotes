from turtle import Turtle, Screen, colormode
import random

# ---------------------- Constants ----------------------
COLOURS = ['red', 'yellow', 'blue', 'black', 'gray', 'brown']
DIRECTIONS = [0, 90, 180, 270]
STEP_SIZE = 10
WIDTH = 500
HEIGHT = 400
START_X = -230
START_Y = -70
GAP = 30


# ---------------------- Setup Functions ----------------------
def setup_screen():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    colormode(255)
    screen.listen()
    return screen


def select_color(rgb=True):
    """
    Selects a random color.
    If rgb is True, returns a random RGB tuple.
    If False, returns a random color name from COLOURS and removes it from the list.
    """
    if rgb:
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    color = random.choice(COLOURS)
    COLOURS.remove(color)
    return color


def create_turtle():
    tim = Turtle()
    tim.shape("turtle")
    random_color = select_color(False)
    tim.color(random_color)
    tim.pensize(1)
    tim.speed("fastest")
    tim.penup()
    return tim


# ---------------------- Race Setup ----------------------
def ask_user_for_bet():
    available_colors = COLOURS.copy()
    user_color = Screen().textinput(
        title="Make your bet",
        prompt=f"Who will win the race? Enter a color from this list:\n{', '.join(available_colors)}"
    )
    while user_color not in available_colors:
        user_color = Screen().textinput(
            title="❌ Invalid choice",
            prompt=f"Please choose a valid color from this list:\n{', '.join(available_colors)}"
        )
    return user_color


def position_turtles():
    turtles = []
    for i in range(len(COLOURS)):
        t = create_turtle()
        t.goto(START_X, START_Y + i * GAP)

        turtles.append(t)
    return turtles


def race(turtles):
    while True:
        for i in range(len(turtles)):
            step = random.randint(1, 10)
            turtles[i].forward(step)
            if turtles[i].xcor() >= WIDTH // 2 - 20:
                return i


# ---------------------- Main ----------------------
def main():
    screen = setup_screen()
    user_bet = ask_user_for_bet()
    turtles = position_turtles()
    winner_index = race(turtles)

    winning_color = turtles[winner_index].color()[0]
    print("The winner is:", winning_color)

    if winning_color == user_bet:
        print("You guessed right!")
    else:
        print("Better luck next time!")

    screen.exitonclick()

if __name__ == "__main__":
    main()