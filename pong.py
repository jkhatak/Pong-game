import turtle ## module for graphics and display
import winsound ## module for sound
import os

# display
window = turtle.Screen() ## displays screen
window.title = ("Pong project by jaidev khatak") ## title of the window
window.bgcolor("grey") ## color of the background 
window.setup(width = 800, height = 600) ## the width and height of the window
window.tracer(0) ## updates the window as it runs

#score tracker

score_1 = 0
score_2 = 0




#Paddle A
paddle_a = turtle.Turtle() ## creates the first paddle
paddle_a.speed(0) # sets the speed of the paddle animation
paddle_a.shape("square")## sets the shape of the paddle
paddle_a.color("black") ## sets the color of the paddle
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1) ## update the size of the paddle 
paddle_a.penup()
paddle_a.goto(-350,0)## coords for the paddle to start at 


# Paddle B
paddle_b = turtle.Turtle() ## creates the first paddle
paddle_b.speed(0) # sets the speed of the paddle animation
paddle_b.shape("square")## sets the shape of the paddle
paddle_b.color("black") ## sets the color of the paddle
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1) ## update the size of the paddle 
paddle_b.penup()
paddle_b.goto(350,0)## coords for the paddle to start at 

#score

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0  Player 2: 0", align= "center", font =("courier",24,"normal"))




#ball
ball = turtle.Turtle() 
ball.speed(0)
ball.shape("square")
ball.color("black") 
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = 0.15

#function 
def paddle_a_up():
    y = paddle_a.ycor()
    y += 35
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 35
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 35
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 35
    paddle_b.sety(y)


#key binds
window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")

## main game loop ## updates the window everytime game runs
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #check the borders
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1 #reverses the direction
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1,score_2), align= "center", font =("courier",24,"normal"))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1,score_2), align= "center", font =("courier",24,"normal"))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
    
    #paddle and ball collision

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()< paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()< paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

