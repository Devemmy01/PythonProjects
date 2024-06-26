# Pong game in python

import turtle
import os

wn = turtle.Screen()
wn.title("Pong by @Devemmy")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

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

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .13
ball.dy = .13

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Paddle movement (Function)
def paddle_a_up():
    y = paddleA.ycor() #gets the y coordinate of the first paddle
    y += 20 #add 20 to the y coordinate
    paddleA.sety(y) #set y of the paddle to the new y coordinate  

def paddle_a_down():
    y = paddleA.ycor() #gets the y coordinate of the first paddle
    y -= 20 #subtract 20 to the y coordinate
    paddleA.sety(y) #set y of the paddle to the new y coordinate

def paddle_b_up():
    y = paddleB.ycor() #gets the y coordinate of the second paddle
    y += 20 #add 20 to the y coordinate
    paddleB.sety(y) #set y of the paddle to the new y coordinate  

def paddle_b_down():
    y = paddleB.ycor() #gets the y coordinate of the first paddle
    y -= 20 #subtract 20 to the y coordinate
    paddleB.sety(y) #set y of the paddle to the new y coordinate
    
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")    
wn.onkeypress(paddle_a_down, "s")    
wn.onkeypress(paddle_b_up, "Up")    
wn.onkeypress(paddle_b_down, "Down")    

# Main loop
while True:
    wn.update()
    
    # To move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Check for borders
    if ball.ycor() > 290:
        ball.sety(290) 
        ball.dy *= -1 # Reverse the direction of the ball
        os.system("mpg123 sound.mp3&")
        
    if ball.ycor() < -290:
        ball.sety(-290) 
        ball.dy *= -1
        os.system("mpg123 sound.mp3&")
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("mpg123 sound.mp3&")
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1       
        os.system("mpg123 sound.mp3&")   
        