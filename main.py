import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car = CarManager()
score = Scoreboard()
end = Turtle()
end.hideturtle()
speed = 0.1

screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.title("Turtle Capstone Game:>")
screen.listen()
screen.onkey(player.move, "Up")

player.start_game()

game_is_on = True
while game_is_on:
    car.car_create()
    time.sleep(speed)
    screen.update()
    car.car_movement()

    if player.loc_check():
        score.new_score()
        speed /= 2
        if car.chance[-1] != 1:
            car.chance.remove(car.chance[-1])

    for each in car.cars_list:
        if each.distance(player.turtle) < 20:
            end.write("Game Over", align="center", font=("Courier", 15, "normal"))
            game_is_on = False

screen.exitonclick()