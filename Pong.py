# Pong game in python

import turtle

wn = turtle.Screen()
wn.title("Pong by @Devemmy")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

# 1st Paddle
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("white")
paddleA.penup()
paddleA.goto(-350, 0)

# 2st Paddle
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("white")
paddleB.penup()
paddleB.goto(350, 0)

# Main loop
while True:
    wn.update()