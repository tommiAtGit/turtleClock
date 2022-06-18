
class Segment:
    def __init__(self, pos_x, pos_y,seg_code):
        self.pos_x = pos_x
        self.pos_y = pos_y
        color = "#FFFFFF"
        if seg_code in ['a', 'g', 'd']:
            self.stretch_wid = 1
            self.stretch_len = 5
        elif seg_code in ['b', 'c','e','f']:
            self.stretch_wid = 5
            self.stretch_len = 1
    def getPos_x(self):
        return self.pos_x
    def getPos_y(self):
        return self.pos_y
    def getWid(self):
        return self.stretch_wid
    def getLen(self):
        return self.stretch_len
