# Import required library
import turtle
dreisiebzig = 370
 
# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)
 
 
# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)
 
 
# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)
 
 
# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(80)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 6
hit_ball.dy = -6
 
 
# Initialize the score
player1 = 0
player2 = 0
 
 
# Show the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Player 1: 0    Player 2: 0",
             align="center", font=("Courier", 24, "normal"))
 
 
# Functions to move paddle up and down
def paddleaup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)
 
 
def paddleadown():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)
 
 
def paddlebup():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)
 
 
def paddlebdown():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)
 
 
# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")



while True:
    sc.update()

    if player1 < 5 and player2 < 5:
        hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
        hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

        # Checking borders
        if hit_ball.ycor() > 280:
            hit_ball.sety(280)
            hit_ball.dy *= -1

        if hit_ball.ycor() < -280:
            hit_ball.sety(-280)
            hit_ball.dy *= -1

        if hit_ball.xcor() > 500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            player1 += 1
            sketch.clear()
            sketch.write("Player 1 : {}    Player 2: {}".format(
                        player1, player2), align="center",
                        font=("Courier", 24, "normal"))

        if hit_ball.xcor() < -500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            player2 += 1
            sketch.clear()
            sketch.write("Player 1: {}    Player 2: {}".format(
                        player1, player2), align="center",
                        font=("Courier", 24, "normal"))

        # Paddle ball collision
        if (hit_ball.xcor() > 360 and\
                            hit_ball.xcor() < int(dreisiebzig)) and\
                            (hit_ball.ycor() < right_pad.ycor()+80 and\
                            hit_ball.ycor() > right_pad.ycor()-80):
            hit_ball.setx(360)
            hit_ball.dx*=-1
            
        if (hit_ball.xcor()<-360 and\
                        hit_ball.xcor()>-370) and\
                        (hit_ball.ycor()<left_pad.ycor()+80 and\
                            hit_ball.ycor()>left_pad.ycor()-80):
            hit_ball.setx(-360)
            hit_ball.dx*=-1
    else:
        if player1 > 4:
            sketch = turtle.Turtle()
            sketch.speed(0)
            sketch.color("blue")
            sketch.penup()
            sketch.hideturtle()
            sketch.goto(0, 100)
            sketch.write("Player 1 Wins!",
                        align="center", font=("Courier", 30, "normal"))

        elif player2 > 4:
            sketch = turtle.Turtle()
            sketch.speed(0)
            sketch.color("blue")
            sketch.penup()
            sketch.hideturtle()
            sketch.goto(0, 100)
            sketch.write("Player 2 Wins!",
                        align="center", font=("Courier", 30, "normal"))







