from turtle import Turtle

ALLIGNMENT = "center"
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.position = position
        self.goto(position)

    def l_current_score(self):
        self.clear()
        self.write(f"{self.l_score}", move=False, align=ALLIGNMENT, font=FONT)

    def r_current_score(self):
        self.clear()
        self.write(f"{self.r_score}", move=False, align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", move=False, align=ALLIGNMENT, font=FONT)
