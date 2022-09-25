from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car = None
        self.xloc = 300
        self.cars_list = []
        self.chance = [0, 1, 2, 3, 4, 5, 6]

    def car_create(self):
        num = random.choice(self.chance)
        if num == 1:
            self.car = Turtle()
            self.car.shape("square")
            self.car.turtlesize(stretch_wid=1.5, stretch_len=1)
            self.car.penup()
            self.car.tiltangle(90)
            self.car.color(random.choice(COLORS))
            self.car.hideturtle()
            self.car.goto(300, random.randint(-250, 250))
            self.car.showturtle()
            self.cars_list.append(self.car)

    def car_movement(self):
        for car in self.cars_list:
            car.backward(STARTING_MOVE_DISTANCE)





