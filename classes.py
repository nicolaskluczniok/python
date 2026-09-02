import pgzrun
import random

HEIGHT = 600
WIDTH = 600

class Circle():
    def __init__(self,radius,x,y,color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
    def drawcircle(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,self.color)

circle1 = Circle(100,150,150, "purple")
def draw():
    circle1.drawcircle()
    
pgzrun.go()