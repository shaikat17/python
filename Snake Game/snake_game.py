from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
	
game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.2)
	snake.move()
	
	#Detect Collision with food
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend_snake()
		scoreboard.increase_score()
		
	#Detect Collision with wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		game_is_on = False
		
		scoreboard.game_over()
		
	#Detect collision with tail
	for segment in snake.snake_segments[1:]:
		if snake.head.distance(segment) < 10:
			game_is_on = False
			scoreboard.game_over()

screen.exitonclick()
