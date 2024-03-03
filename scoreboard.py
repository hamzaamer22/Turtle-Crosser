from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.current_level = 1

    def print_level(self):
        self.goto(-240, 260)
        self.write(f"Level: {self.current_level}", align="center", font=("Arial", 18))

    def increment_level(self):
        self.clear()
        self.current_level += 1
        self.print_level()

    def print_game_over(self):
        self.goto(0, -10)
        self.write(f"Game Over", align="center", font=("Arial", 40))

    def user_wins(self):
        self.goto(0, -50)
        self.write(f"How the heck did you do it.\nUnreal\nYOU WINNNNNNN\n SUIIIIIIIII", align="center", font=("Arial", 36))

