import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def maybe_create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def check_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False

    def reset(self):
        for car in self.cars:
            if car.xcor() < -280:
                car.goto(300, random.randint(-260, 260))

