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
    
    # New
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
    
def testSquare():
    p1 = MyPoint(100, 50)
    square = Square(p1, 50)
    print("square's side length is", square.getSide())  # 50
    print("square's p1 is", square.getP1())  # MyPoint(100, 50)
    print("square's p2 is", square.getP2())  # MyPoint(150, 100)

    square.move(10, -20)
    print("After the move ...")
    print("square's side length is", square.getSide())  # 50
    print("square's p1 is", square.getP1())  # MyPoint(110, 30)
    print("square's p2 is", square.getP2())  # MyPoint(160, 80)

    print(square)  # Square(MyPoint(110, 30), MyPoint(160, 80))

    print("Changing square's fill colour to red")
    square.setFillColour("red")
    print("square's fill colour is", square.fillColour)  # red
    print("Changing square's fill colour to leopard print!")
    square.setFillColour("leopard print")
    print("square's fill colour is", square.fillColour)  # red

    square.setOutlineColour("blue")
    print(square.outlineColour)
    square.setOutlineColour("gay")
    print(square.outlineColour)

    print(square.getPerimeter())
    print(square.getArea())

    print(square.getCenter())

testSquare()