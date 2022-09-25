from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        self.turtle = Turtle()
        self.ycor = -280

    def start_game(self):
        self.turtle.shape("turtle")
        self.turtle.color("black")
        self.turtle.penup()
        self.turtle.tiltangle(90)
        self.turtle.goto(STARTING_POSITION)

    def move(self):
        self.ycor += MOVE_DISTANCE
        self.turtle.goto(0, self.ycor)

    def loc_check(self):
        if self.ycor > FINISH_LINE_Y:
            self.ycor = -280
            self.turtle.hideturtle()
            self.turtle.goto(STARTING_POSITION)
            self.turtle.showturtle()
            return True


