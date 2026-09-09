
class square():
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        self.length = length
    def display(self):
        print(self.x,self.y,self.length)
    def area(self):
        print(self.length*self.length)
        
square1 = square(50,40,100)
square1.area()
square1.display()