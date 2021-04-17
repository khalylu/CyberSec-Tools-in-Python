import math


class Line:

    def __init__(self, coor1=(), coor2=()):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        d = math.sqrt((self.coor1[0] - self.coor2[0])**2 + (self.coor1[1] - self.coor2[1])**2)
        return d

    def slope(self):
        s = (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])
        return s


Li = Line((17, 5), (25, 14))

print(Li.distance())