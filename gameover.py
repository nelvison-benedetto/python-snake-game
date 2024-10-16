from turtle import Turtle
import random

ALIGNMENT = "center"
FONT = ("Arial",24,"normal")

class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()

    #def gameover(self):
     #   self.write(f"Game Over!", align=ALIGNMENT, font=FONT)

