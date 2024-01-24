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
    

class MyCircle:

    def __init__(self, center: MyPoint, radius: float) -> None:
        self.center = center
        self.radius = radius
    
    def getCenter(self) -> MyPoint:
        return self.center
    
    def getRadius(self) -> float:
        return self.radius
    
    def move(self, dx: float, dy: float) -> None:
        self.center.move(dx, dy)
    
    def __str__(self):
        return f"MyCircle(Center: {self.center.x}, Radius: {self.radius}"
    
    