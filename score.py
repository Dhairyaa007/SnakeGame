from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.old_high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update()

    def update(self):
        with open("scoreboard.txt", mode="r") as score_file:
            self.old_high_score = int(score_file.read())
            if self.old_high_score > self.high_score:
                self.high_score = self.old_high_score
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        self.update()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
        self.score_file()

    def score_file(self):
        with open("scoreboard.txt", mode="w") as score_file:
            file_content = str(self.high_score)
            score_file.write(file_content)
