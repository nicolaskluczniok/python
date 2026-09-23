class mobilephone():
    def __init__(self,battery,storage,model,price):
        self.battery = battery
        self.storage = storage
        self.model = model
        self.price = price
    def display(self):
        print(self.battery,self.storage,self.model,self.price)

mobilephone1 = mobilephone(50%,"1tb","iphone 11",500)
mobilephone1.display()