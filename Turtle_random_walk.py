import turtle as t
import random

trtl = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
trtl.pensize(15)
trtl.speed("fastest")

for _ in range(200):
    trtl.color(random.choice(colours))
    trtl.forward(30)
    trtl.setheading(random.choice(directions))
