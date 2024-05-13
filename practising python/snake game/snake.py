import turtle as t
import time
STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
WIDTH = 600
HEIGHT = 600


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range((len(self.segments))-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DIST)

    def add_segment(self, position):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def remove_segment(self, segment):
        for seg in range(segment, len(self.segments)):
            self.segments[seg].hideturtle()
        self.segments = self.segments[:segment]

    def blink(self, color):
        for _ in range(2):
            for seg in self.segments:
                seg.color(color)

            t.update()
            time.sleep(0.1)

            for seg in self.segments:
                seg.color("white")

            t.update()
            time.sleep(0.1)

    def reset_position(self):
        self.segments[0].goto(0, 0)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
