from turtle import Turtle


class Car(Turtle):
    def __init__(self, car_part_positions):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.all_parts = []
        self.car_center = 0
        self.create_car(car_part_positions)


    def create_car(self, part_positions):
        """Positions come as middle, middle, middle, top, tyre, tyre"""
        part_number = 0
        for i in range(3):
            car_middle = Turtle()
            car_middle.color("midnight blue")
            car_middle.penup()
            car_middle.shape("square")
            car_middle.goto(part_positions[part_number])
            self.all_parts.append(car_middle)
            if i == 1:
                self.car_center = car_middle
            part_number += 1

        car_top = Turtle()
        car_top.shape("square")
        car_top.color("olive drab")
        car_top.penup()
        car_top.goto(part_positions[part_number])
        self.all_parts.append(car_top)
        part_number += 1

        car_tyre1 = Turtle()
        car_tyre1.shape("circle")
        car_tyre1.color("dark slate gray")
        car_tyre1.penup()
        car_tyre1.goto(part_positions[part_number])
        self.all_parts.append(car_tyre1)
        part_number += 1

        car_tyre2 = Turtle()
        car_tyre2.shape("circle")
        car_tyre2.color("dark slate gray")
        car_tyre2.penup()
        car_tyre2.goto(part_positions[part_number])
        self.all_parts.append(car_tyre2)
        part_number += 1


    def move_car(self, move_distance):
        for parts in self.all_parts:
            parts.setheading(0)
            parts.forward(move_distance)


    def refresh_car_position(self, refreshed_position):
        count = 0
        for parts in self.all_parts:
            parts.goto(refreshed_position[count])
            count += 1
