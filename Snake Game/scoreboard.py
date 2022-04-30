from turtle import Turtle

class scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.penup()
		self.goto(0,270)
		self.color("white")
		self.update_score()
		
	def update_score(self):
		self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
		self.hideturtle()
		
	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_score()
		
	def game_over(self):
		self.goto(0,0)
		self.write(f"Game Over!!!: {self.score}", align="center", font=("Arial", 24, "normal"))
		self.hideturtle()
