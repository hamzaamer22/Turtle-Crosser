from turtle import Turtle
FINISH_LINE_Y = 251
START_LINE = (0, -250)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("dark green")
        self.goto(0, -280)
        self.setheading(90)
        self.shapesize(stretch_wid=1.4, stretch_len=1.4)

    def move_up(self):
        self.setheading(90)
        self.forward(10)

    def move_down(self):
        self.setheading(270)
        self.forward(10)

    def move_left(self):
        self.setheading(180)
        self.forward(10)

    def move_right(self):
        self.setheading(0)
        self.forward(10)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.back_to_start_line()
            return True

    def back_to_start_line(self):
        self.goto(START_LINE)
