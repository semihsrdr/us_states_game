
from turtle import Turtle
class Pencil(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self,x,y,city):
        self.goto(x,y)
        self.write(city,align="center",font=("Arial",7,"bold"))
class Score(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(280,255)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 20, "bold"))

class Heart(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.heart = 3
        self.show_heart()


    def show_heart(self):
        x=-320
        self.clear()
        for i in range(self.heart):
            self.goto(x,250)
            self.write("❤️", align="center", font=("Arial", 30, "bold"))
            x+=50
