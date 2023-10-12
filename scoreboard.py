from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGNMENT = "left"
GAME_OVER_ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align=GAME_OVER_ALIGNMENT, font=FONT)