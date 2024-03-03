from turtle import Screen
from background import Background
from barrier import Barrier
from car import Car
from player import Player
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car6_part_positions = [(0, 130), (20, 130), (40, 130), (20, 150), (5, 110), (35, 110)]
car5_part_positions = [(0, 0), (20, 0), (40, 0), (20, 20), (5, -20), (35, -20)]
car4_part_positions = [(0, -130), (20, -130), (40, -130), (20, -110), (5, -150), (35, -150)]
car3_part_positions = [(0, 130), (20, 130), (40, 130), (20, 150), (5, 110), (35, 110)]
car2_part_positions = [(0, 0), (20, 0), (40, 0), (20, 20), (5, -20), (35, -20)]
car1_part_positions = [(0, -130), (20, -130), (40, -130), (20, -110), (5, -150), (35, -150)]
ROAD1_START_POSITIONS = [(-280, -130), (-260, -130), (-240, -130), (-260, -110), (-275, -150), (-245, -150)]
ROAD1_OPPOSITE_START_POSITIONS = [(280, -130), (260, -130), (240, -130), (260, -110), (275, -150), (245, -150)]
ROAD2_START_POSITIONS = [(-20, 0), (0, 0), (20, 0), (0, 20), (-15, -20), (15, -20)]
ROAD3_START_POSITIONS = [(-20, 130), (0, 130), (20, 130), (0, 150), (-15, 110), (15, 110)]
NEW_BARRIER_POINTS = [(-290, -80), (-290, -60), (-290, -50), (-270, -80), (-270, -60), (-270, -50),
                      (-250, -80), (-250, -60), (-250, -50), (-230, -80), (-230, -60), (-230, -50),
                      (-210, -80), (-210, -60), (-210, -50), (-190, -80), (-190, -60), (-190, -50),
                      (-170, -80), (-170, -60), (-170, -50), (-150, -80), (-150, -60), (-150, -50),
                      (-130, -80), (-130, -60), (-130, -50),
                      (290, -80), (290, -60), (290, -50), (270, -80), (270, -60), (270, -50),
                      (250, -80), (250, -60), (250, -50), (230, -80), (230, -60), (230, -50),
                      (210, -80), (210, -60), (210, -50), (190, -80), (190, -60), (190, -50),
                      (170, -80), (170, -60), (170, -50), (150, -80), (150, -60), (150, -50),
                      (130, -80), (130, -60), (130, -50)]

CAR2_SPEED = 20
CAR5_SPEED = -20
GAME_SPEED = 0.1
VICTORY = False


background = Background()
barrier = Barrier()
player = Player()
car1 = Car(car1_part_positions)
car2 = Car(car2_part_positions)
car3 = Car(car3_part_positions)
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)
screen.onkeypress(key="Down", fun=player.move_down)
screen.onkeypress(key="Left", fun=player.move_left)
screen.onkeypress(key="Right", fun=player.move_right)

# Print starting level
scoreboard.print_level()

game_is_on = True
while game_is_on:

    # Move car1
    car1.move_car(20)
    if car1.car_center.xcor() > 300:
        car1.refresh_car_position(ROAD1_START_POSITIONS)

    # Move car2
    car2.move_car(CAR2_SPEED)
    if car2.car_center.xcor() > 300 or car2.car_center.xcor() < -300:
        car2.refresh_car_position(ROAD2_START_POSITIONS)
        CAR2_SPEED *= -1

    # Move car3
    move_distance = random.randint(-50, 50)
    car3.move_car(move_distance)
    if car3.car_center.xcor() > 300 or car3.car_center.xcor() < -300:
        car3.refresh_car_position(ROAD3_START_POSITIONS)

    # Detect collision with barriers
    for barriers in barrier.all_barriers:
        if barriers.distance(player) < 25:
            game_is_on = False

    # Detect collision with car1
    for parts in car1.all_parts:
        if parts.distance(player) < 25:
            game_is_on = False

    # Detect collision with car2
    for parts in car2.all_parts:
        if parts.distance(player) < 25:
            game_is_on = False

    # Detect collision with car3
    for parts in car3.all_parts:
        if parts.distance(player) < 25:
            game_is_on = False


    # Crossing finish line
    if player.at_finish_line():
        scoreboard.increment_level()
        # Game speed doubles only on reaching level 2 and 4
        if scoreboard.current_level == 2 or scoreboard.current_level == 4:
            GAME_SPEED *= 0.5
        # Car4 made only on level 2
        if scoreboard.current_level == 2:
            car4 = Car(car4_part_positions)
        # Car5 made only on level 3
        if scoreboard.current_level == 3:
            car5 = Car(car5_part_positions)
            car2.refresh_car_position(ROAD2_START_POSITIONS)
            CAR2_SPEED = 20
        # New barriers made only on level 4
        if scoreboard.current_level == 4:
            for new_barriers in NEW_BARRIER_POINTS:
                barrier.create_barrier(new_barriers)
        # Car6 made only on level 5
        if scoreboard.current_level == 5:
            car6 = Car(car6_part_positions)
        # Victory on completing level 5
        if scoreboard.current_level == 6:
            scoreboard.user_wins()
            VICTORY = True
            game_is_on = False


    # Car4 moves on from level 2
    if scoreboard.current_level > 1:
        # Moving car4
        car4.move_car(-20)
        if car4.car_center.xcor() < -300:
            car4.refresh_car_position(ROAD1_OPPOSITE_START_POSITIONS)
        # Detect collision with car4
        for parts in car4.all_parts:
            if parts.distance(player) < 25:
                game_is_on = False

    if scoreboard.current_level > 2:
        # Moving car5
        car5.move_car(CAR5_SPEED)
        if car5.car_center.xcor() > 300 or car5.car_center.xcor() < -300:
            car5.refresh_car_position(ROAD2_START_POSITIONS)
            CAR5_SPEED *= -1
        # Detect collision with car5
        for parts in car5.all_parts:
            if parts.distance(player) < 25:
                game_is_on = False

    if scoreboard.current_level > 4:
        move_distance_2 = random.randint(-50, 50)
        car6.move_car(move_distance_2)
        if car6.car_center.xcor() > 300 or car6.car_center.xcor() < -300:
            car6.refresh_car_position(ROAD3_START_POSITIONS)
        # Detect collision with car6
        for parts in car6.all_parts:
            if parts.distance(player) < 25:
                game_is_on = False


    time.sleep(GAME_SPEED)
    screen.update()

    # Checking game over
    if not game_is_on and VICTORY == False:
        scoreboard.print_game_over()

screen.exitonclick()
