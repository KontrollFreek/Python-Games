import turtle
import winsound
import time

# Draw Screen
win = turtle.Screen()
win.title('PyONG')
win.bgcolor('black')
win.setup(width=1000, height=600)
win.tracer(0)

# Menu
menu1 = turtle.Turtle()
menu1.speed(0)
menu1.color('black')
menu1.penup()
menu1.hideturtle()
menu1.goto(0, 180)
menu1.write('PyONG', align='center', font=('Courier', 90, 'bold'))

menu2 = turtle.Turtle()
menu2.speed(0)
menu2.color('black')
menu2.penup()
menu2.hideturtle()
menu2.goto(0, -90)
menu2.write('Press Space to start', align='center', font=('Courier', 45, 'bold'))

while True:
    time.sleep(2)
    menu1.clear()
    menu2.clear()
    menu1.color('white')
    menu2.color('white')
    menu1.write('PyONG', align='center', font=('Courier', 90, 'bold'))
    menu2.write('Press Space to start', align='center', font=('Courier', 45, 'bold'))
    break


# Varables
p = True
score1 = 0
score2 = 0

# Paddle 1
pad1 = turtle.Turtle()
pad1.speed(0)
pad1.shape('square')
pad1.shapesize(stretch_wid=5, stretch_len=1)
pad1.color('black')
pad1.penup()
pad1.goto(-400, 0)

# Paddle 2
pad2 = turtle.Turtle()
pad2.speed(0)
pad2.shape('square')
pad2.shapesize(stretch_wid=5, stretch_len=1)
pad2.color('black')
pad2.penup()
pad2.goto(400, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('black')
ball.penup()
ball.goto(0, 0)
ball.dx = 0
ball.dy = 0

# Pen
score = turtle.Turtle()
score.speed(0)
score.color('black')
score.penup()
score.hideturtle()
score.goto(0, 160)
score.write('Player 1: 0  Player 2: 0', align='center', font=('Courier', 24, 'bold'))

# Paddle 1 Movement
def pad1_up():
    y = pad1.ycor()
    y += 20
    pad1.sety(y)

def pad1_dwn():
    y = pad1.ycor()
    y -= 20
    pad1.sety(y)

# Paddle 2 Movement
def pad2_up():
    y = pad2.ycor()
    y += 20
    pad2.sety(y)

def pad2_dwn():
    y = pad2.ycor()
    y -= 20
    pad2.sety(y)

# Game start
def gamestart():
    if (p = False):
        pad1.sety(0)
        pad1.color('white')

        pad2.sety(0)
        pad2.color('white')

        ball.dx = 0.14
        ball.dy = 0.14
        ball.color('white')

        score.clear()
        score.color('white')
        score.goto(0,260)
        score.write('Player 1: 0  Player 2: 0', align='center', font=('Courier', 24, 'bold'))

        menu1.clear()
        menu2.clear()

        p = True
    
    else if (p = True):
        return

# Keyboard Binding

win.onkeyrelease(gamestart, 'space')

win.listen()

win.onkeypress(pad1_up, 'w')
win.onkeypress(pad1_dwn, 's')

win.onkeypress(pad2_up, 'i')
win.onkeypress(pad2_dwn, 'k')

# Game Loop
while True:
    win.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball Border Check
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 480:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        winsound.PlaySound("offscreen.wav", winsound.SND_ASYNC)
        score.clear()
        score.write('Player 1: {}  Player 2: {}'.format(score1, score2), align='center', font=('Courier', 24, 'bold'))
    if ball.xcor() < -480:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        winsound.PlaySound("offscreen.wav", winsound.SND_ASYNC)
        score.clear()
        score.write('Player 1: {}  Player 2: {}'.format(score1, score2), align='center', font=('Courier', 24, 'bold'))

    # Paddle Border Check
    if pad1.ycor() > 240:
        pad1.sety(240)

    if pad1.ycor() < -240:
        pad1.sety(-240)

    if pad2.ycor() > 240:
        pad2.sety(240)

    if pad2.ycor() < -240:
        pad2.sety(-240)

    # Paddle & Ball Collision
    if (ball.xcor() > 380 and ball.xcor() < 410) and (ball.ycor() < pad2.ycor() + 40 and ball.ycor() > pad2.ycor() -40):
        ball.setx(380)
        ball.dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -380 and ball.xcor() > -410) and (ball.ycor() < pad1.ycor() + 40 and ball.ycor() > pad1.ycor() -40):
        ball.setx(-380)
        ball.dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    # Score Detector
    if (score2 == 7):
        score.clear()
        score.goto(0,-40)
        pad1.goto(0,-500)
        pad2.goto(0,500)
        ball.goto(0,100)
        ball.color('black')
        ball.dx = 0
        ball.dy = 0
        score.write('Player 2 Wins!', align='center', font=('Courier', 72, 'bold'))

    if (score1 == 7):
        score.clear()
        score.goto(0,-40)
        pad1.goto(0,-500)
        pad2.goto(0,500)
        ball.goto(0,100)
        ball.color('black')
        ball.dx = 0
        ball.dy = 0
        score.write('Player 2 Wins!', align='center', font=('Courier', 72, 'bold'))