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
    tenSecElement = DisplayElement(100,0)

    oneMinElement = DisplayElement(-100,0)
    tenMinElement = DisplayElement(-300,0)

    oneSecund = 5
    tenSec = 5
    oneMin = 9
    tenMin = 0
    fistSecElement.drawNumber(oneSecund)
    tenSecElement.drawNumber(tenSec)
    oneMinElement.drawNumber(oneMin)
    tenMinElement.drawNumber(tenMin)

    while True:
        if oneSecund == 9:
            oneSecund = 0
            tenSec = tenSec + 1
        else:
             oneSecund = oneSecund +1

        if oneMin == 9 and oneSecund == 9 and tenSec == 5:
            oneMin = 0
            oneSecund = 0
            tenSec = 0
            tenMin = tenMin +1

        if oneSecund == 9 and tenSec == 5:
            oneSecund = 0
            tenSec = 0
            oneMin = oneMin +1



        window.update()
        print ("Time" , tenMin ,":",oneMin)
        fistSecElement.drawNumber(oneSecund)
        tenSecElement.drawNumber(tenSec)
        oneMinElement.drawNumber(oneMin)
        tenMinElement.drawNumber(tenMin)

        ball.color("#000000")
        ball_1.color("#000000")
        time.sleep(1)
        window.update()
        ball.color("#FFFFFF")
        ball_1.color("#FFFFFF")
        time.sleep(1)

if __name__ == "__main__":


    createBackground()
