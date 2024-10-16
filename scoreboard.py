from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
    def update_scoreboard(self):
        with open("data.txt",mode="r") as file:
            self.content = file.read()

        self.write(f"Score = {self.score} Hight Score = {self.content}",align = ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            print(f"the high score is {self.high_score}")
            with open("data.txt", mode="w") as file:
                str_highscore = str(self.high_score)
                file.write(str_highscore)
        self.score = 0
        self.update_scoreboard()
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

