from turtle import Turtle, Screen
from pong_paddle import Paddle
from pong_ball import Ball
import time
from pong_scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "Left")
screen.onkey(l_paddle.go_down, "Right")


game_is_on = True

while game_is_on:
	time.sleep(0.1)
	screen.update()
	ball.move()
	
	#Detect collision with the wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		# need to bounce
		ball.bounce_y()
	
	#Detect collision with the r_paddle
	if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -350:
		ball.bounce_x()
		
	#Detect R paddle misses
	if ball.xcor() > 380:
		ball.reset_position()
		scoreboard.l_score_up()
		
	#Detect L paddle misses
	if ball.xcor() < -380:
		ball.reset_position()
		scoreboard.r_score_up()
		

screen.exitonclick()
