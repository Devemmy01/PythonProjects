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

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = .1

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
        
    if ball.ycor() < -290:
        ball.sety(-290) 
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1