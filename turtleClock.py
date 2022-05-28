import turtle
import time


def createSeparator(color,x,y):
    separatorBall = turtle.Turtle()
    separatorBall.penup()
    separatorBall.speed(0)
    separatorBall.shape("circle")
    separatorBall.color(color)
    separatorBall.goto(x,y)

    return separatorBall


def createBackground():
    #Dispaly window og the game
    window = turtle.Screen()
    window.title("Tutrle clock")
    window.bgcolor("#000000")
    window.setup(width=800,height=600)
    window.tracer(0)

    ball = createSeparator("#FFFFFF",0,0)

    ball_1 = createSeparator("#FFFFFF",0,30)

    while True:
        window.update()
        ball.color("#000000")
        ball_1.color("#000000")
        time.sleep(1)
        window.update()
        ball.color("#FFFFFF")
        ball_1.color("#FFFFFF")
        time.sleep(1)

if __name__ == "__main__":
    createBackground()
