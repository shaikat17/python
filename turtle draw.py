from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def moveForwards():
  tim.forward(10)

def movebackwards():
  tim.backward(10)

def turnLeft():
  newHeading = tim.heading() + 10
  tim.setheading(newHeading)

def turnRight():
  newHeading = tim.heading() - 10
  tim.setheading(newHeading)

def clear():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()


screen.listen()
#screen.onkey(key='space', fun=moveForwards)
screen.onkey(moveForwards, 'w')
screen.onkey(movebackwards, 's')
screen.onkey(turnLeft, 'a')
screen.onkey(turnRight, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()
