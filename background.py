from turtle import Turtle
START_LINE = (-290, -250)
FINISH_LINE = (-290, 251)
ROAD_POINTS = [(-300, -170), (-300, -40), (-300, 90)]
ROAD_LINE_POINTS = [(-230, -140), (-30, -140), (170, -140), (-230, -10),
                    (-30, -10), (170, -10), (-230, 120), (-30, 120), (170, 120)]
ROAD_LENGTH = 600
ROAD_WIDTH = 80
LINE_LENGTH = 60
LINE_WIDTH = 20


class Background(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.dotted_line(START_LINE)
        self.dotted_line(FINISH_LINE)
        for points in ROAD_POINTS:
            self.create_road(points)
        for lines in ROAD_LINE_POINTS:
            self.road_lines(lines)



    def dotted_line(self, position):
        self.color("black")
        self.goto(position)
        self.setheading(0)
        for i in range(30):
            if i % 2 == 0:
                self.pendown()
                self.forward(20)
            else:
                self.penup()
                self.forward(20)



    def create_road(self, points):
        self.color("grey")
        self.goto(points)
        self.create_rectangle(road_length=ROAD_LENGTH, road_width=ROAD_WIDTH)


    def create_rectangle(self, road_length, road_width):
        self.setheading(0)
        self.begin_fill()
        self.forward(road_length)
        self.setheading(90)
        self.forward(road_width)
        self.setheading(180)
        self.forward(road_length)
        self.setheading(270)
        self.forward(road_width)
        self.end_fill()

    def road_lines(self, line_points):
        self.color("yellow")
        self.goto(line_points)
        self.create_rectangle(road_length=LINE_LENGTH, road_width=LINE_WIDTH)

