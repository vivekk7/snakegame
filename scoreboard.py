from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Shonar Bangla', 20, 'normal')
"""Creates and keeps track of score."""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Writes score to the screen."""
        self.write(f"Score : {self.score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Writes game over on screen."""

        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=('Courier', 25, "bold"))

    def increase_score(self):
        """Increaments score everytime food is refreshed."""
        self.score += 1
        self.clear()
        self.update_scoreboard()