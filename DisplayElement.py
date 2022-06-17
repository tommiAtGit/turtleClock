import turtle
from Segment import Segment

class DisplayElement:
#           a
#      f          b
#           g
#      e          c
#           d
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.segment_A = Segment(pos_x,pos_y+115,'a')
        self.segment_B = Segment(pos_x+65,pos_y+65,'b')
        self.segment_C = Segment(pos_x+65, pos_y-65,'c')
        self.segment_D = Segment(pos_x,pos_y-115,'d')
        self.segment_E = Segment(pos_x-65, pos_y-65,'e')
        self.segment_F = Segment(pos_x-65, pos_y+65,'f')
        self.segment_G = Segment(pos_x,pos_y,'g')




    def draw_A(self, color):
        segment_a = turtle.Turtle()
        segment_a.shape("square")
        segment_a.color(color)
        segment_a.penup()
        segment_a.goto(self.segment_A.getPos_x(),self.segment_A.getPos_y())
        segment_a.shapesize(stretch_wid=self.segment_A.getWid(),stretch_len=self.segment_A.getLen())

    def draw_G(self, color):
        segment_g = turtle.Turtle()
        segment_g.shape("square")
        segment_g.color(color)
        segment_g.penup()
        segment_g.goto(self.segment_G.getPos_x(),self.segment_G.getPos_y())
        segment_g.shapesize(stretch_wid=self.segment_G.getWid(),stretch_len=self.segment_G.getLen())

    def draw_D(self, color):
        segment_d = turtle.Turtle()
        segment_d.shape("square")
        segment_d.color(color)
        segment_d.penup()
        segment_d.goto(self.segment_D.getPos_x(),self.segment_D.getPos_y())
        segment_d.shapesize(stretch_wid=self.segment_D.getWid(),stretch_len=self.segment_D.getLen())

    def draw_B(self, color):
        segment_b = turtle.Turtle()
        segment_b.shape("square")
        segment_b.color(color)
        segment_b.penup()
        segment_b.goto(self.segment_B.getPos_x(),self.segment_B.getPos_y())
        segment_b.shapesize(stretch_wid=self.segment_B.getWid(),stretch_len=self.segment_B.getLen())

    def draw_C(self, color):
        segment_c = turtle.Turtle()
        segment_c.shape("square")
        segment_c.color(color)
        segment_c.penup()
        segment_c.goto(self.segment_C.getPos_x(),self.segment_C.getPos_y())
        segment_c.shapesize(stretch_wid=self.segment_C.getWid(),stretch_len=self.segment_C.getLen())

    def draw_E(self, color):
        segment_e = turtle.Turtle()
        segment_e.shape("square")
        segment_e.color(color)
        segment_e.penup()
        segment_e.goto(self.segment_E.getPos_x(),self.segment_E.getPos_y())
        segment_e.shapesize(stretch_wid=self.segment_E.getWid(),stretch_len=self.segment_E.getLen())

    def draw_F(self, color):
        segment_f = turtle.Turtle()
        segment_f.shape("square")
        segment_f.color(color)
        segment_f.penup()
        segment_f.goto(self.segment_F.getPos_x(),self.segment_F.getPos_y())
        segment_f.shapesize(stretch_wid=self.segment_F.getWid(),stretch_len=self.segment_F.getLen())

    def drawNumber(self, number):
        if number == 0:
            self.draw_A("#FFFFFF")
            self.draw_B("#FFFFFF")
            self.draw_C("#FFFFFF")
            self.draw_D("#FFFFFF")
            self.draw_E("#FFFFFF")
            self.draw_F("#FFFFFF")

            self.draw_G("#000000")
            
        elif number == 1:
            self.draw_B("#FFFFFF")
            self.draw_C("#FFFFFF")

            self.draw_A("#000000")
            self.draw_D("#000000")
            self.draw_E("#000000")
            self.draw_F("#000000")
            self.draw_G("#000000")

        elif number == 2:
            self.draw_A("#FFFFFF")
            self.draw_B("#FFFFFF")
            self.draw_D("#FFFFFF")
            self.draw_E("#FFFFFF")
            self.draw_G("#FFFFFF")

            self.draw_F("#000000")
            self.draw_C("#000000")

        elif number == 3:
            self.draw_A("#FFFFFF")
            self.draw_B("#FFFFFF")
            self.draw_D("#FFFFFF")
            self.draw_C("#FFFFFF")
            self.draw_G("#FFFFFF")

            self.draw_F("#000000")
            self.draw_E("#000000")

        elif number == 4:
            self.draw_B("#FFFFFF")
            self.draw_F("#FFFFFF")
            self.draw_C("#FFFFFF")
            self.draw_G("#FFFFFF")

            self.draw_A("#000000")
            self.draw_D("#000000")
            self.draw_E("#000000")

        elif number == 5:
            self.draw_F("#FFFFFF")
            self.draw_C("#FFFFFF")
            self.draw_G("#FFFFFF")
            self.draw_A("#FFFFFF")
            self.draw_D("#FFFFFF")

            self.draw_B("#000000")
            self.draw_E("#000000")

        elif number == 6:
            self.draw_F("#FFFFFF")
            self.draw_C("#FFFFFF")
            self.draw_G("#FFFFFF")
            self.draw_A("#FFFFFF")
            self.draw_D("#FFFFFF")
            self.draw_E("#FFFFFF")

            self.draw_B("#000000")


        elif number == 7:
            self.draw_A("#FFFFFF")
            self.draw_B("#FFFFFF")
            self.draw_C("#FFFFFF")

            self.draw_G("#000000")
            self.draw_F("#000000")
            self.draw_D("#000000")
            self.draw_E("#000000")

        elif number == 8:
            self.draw_F("#FFFFFF")
            self.draw_C("#FFFFFF")
            self.draw_G("#FFFFFF")
            self.draw_A("#FFFFFF")
            self.draw_D("#FFFFFF")
            self.draw_B("#FFFFFF")
            self.draw_E("#FFFFFF")

        elif number == 9:
            self.draw_F("#FFFFFF")
            self.draw_C("#FFFFFF")
            self.draw_G("#FFFFFF")
            self.draw_A("#FFFFFF")
            self.draw_D("#FFFFFF")
            self.draw_B("#FFFFFF")

            self.draw_E("#000000")

        else:
            print ('Wrong number', number)

if __name__ == "__main__":
    element = DisplayElement()
