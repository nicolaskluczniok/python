class rectangle():
    def __init__(self,x,y,length,width):
      self.x = x
      self.y = y
      self.length = length
      self.width = width
    def display(self):
        print(self.x,self.y,self.length,self.width)
    def perimeter(self):
        print(2*(self.length+self.width))
rectangle1 = rectangle(50,50,50,100)
rectangle2 = rectangle(75,75,75,60)
rectangle1.display()
rectangle1.perimeter()
rectangle2.display()
rectangle2.perimeter()