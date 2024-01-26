from graphics import *


class MyPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        output = f"MyPoint({self.x}, {self.y})"
        return output
    


class Square():

    def __init__(self, p1, side):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.getX() + side, p1.getY() + side)
        self.fillColour = "black"
        # New
        self.outlineColour = "black"

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def getSide(self):
        return self.side

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def __str__(self):
        output = f"Square({self.p1}, {self.p2})"
        return output

    def setFillColour(self, colour):
        colours = ["red", "green", "blue", "yellow", "purple"]
        if colour in colours:
            self.fillColour = colour
    
    def setOutlineColour(self, colour: str) -> None:
        colours = ["red", "green", "blue", "yellow", "purple"]
        if colour in colours:
            self.outlineColour = colour

    def getPerimeter(self) -> int:
        return self.side * 4
    
    def getArea(self) -> int:
        return self.side ** 2
    
    def getCenter(self) -> MyPoint:
        x = self.p1.getX() + self.side // 2
        y = self.p1.getY() + self.side // 2
        return MyPoint(x, y)
    
    def scale(self, factor: int) -> None:
        new_side_length = self.side * factor
        point_move_length = (self.side - new_side_length) / 2
        self.side = new_side_length
        # self.p1.move(-point_move_length, -point_move_length)
        self.p2.move(point_move_length, point_move_length)


square = Square(MyPoint(30, 30), 15)
print(square.getCenter())
square.scale(2)
print(square.getCenter())