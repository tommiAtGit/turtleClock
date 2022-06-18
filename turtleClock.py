import turtle
import time
from DisplayElement import DisplayElement

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
    window.title("Turtle clock")
    window.bgcolor("#000000")
    window.setup(width=800,height=600)
    window.tracer(0)

    ball = createSeparator("#FFFFFF",0,0)

    ball_1 = createSeparator("#FFFFFF",0,30)

    fistSecElement = DisplayElement(300,0)
    secondSecElement = DisplayElement(100,0)

    firstMinElement = DisplayElement(-100,0)
    secondMinElement = DisplayElement(-300,0)

    firstSec = 0
    secondSec = 0
    firstMin = 0
    secondMin = 0
    fistSecElement.drawNumber(firstSec)
    secondSecElement.drawNumber(secondSec)
    firstMinElement.drawNumber(firstMin)
    secondMinElement.drawNumber(secondMin)

    while True:
        if firstSec == 9:
            firstSec = 0
            secondSec = secondSec + 1
            secondSecElement.drawNumber(secondSec)
        else:
             firstSec = firstSec +1

        window.update()
        fistSecElement.drawNumber(firstSec)

        ball.color("#000000")
        ball_1.color("#000000")
        time.sleep(1)
        window.update()
        ball.color("#FFFFFF")
        ball_1.color("#FFFFFF")
        time.sleep(1)

if __name__ == "__main__":


    createBackground()
