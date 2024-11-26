from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))

    def right_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def left_score(self):
        self.l_score += 1
        self.update_scoreboard()
