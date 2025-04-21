from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_base_snake()
        self.head = self.segments[0]

    def create_base_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def create_new_snake(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        new_segment.goto(new_x, new_y)
        self.segments.append(new_segment)

    def is_collision_with(self, other_turtle):
        return self.head.distance(other_turtle) < 20

    def has_collided_with_self(self):
        if len(self.segments) < 5:
            return False  # avoid false positives in early game
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def has_hit_wall(self, width=600, height=600):
        x = self.head.xcor()
        y = self.head.ycor()
        return (
                x > width // 2 - 10 or x < -width // 2 + 10 or
                y > height // 2 - 10 or y < -height // 2 + 10
        )

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
