class car():
    def __init__(self,brand,cost,rent,model,availibility):
        self.brand = brand
        self.cost = cost
        self.rent = rent
        self.model = model
        self.availibility = availibility
    def display(self):
        print(self.brand,self.cost,self.model,self.availibility)
    def rentcar(self):
        print(self.availibility)
        if self.availibility == True:
            print("availibility")
            self.availibility = False
        else:
            print("not availibility")
    def buycar(self):
        buycar = self.cost
        print(buycar)
        self.availibility = False
    def returncar(self):
        self.availibility = True
    def carrent(self,days):
        rentcost = days*self.rent
        print(rentcost)
        self.availibility = False
    def sellcar(self):
        sell = self.cost*0.85
        print(sell)
         
car1 = car("audi",270000,5000,"r8",True)

car1.display()
car1.rentcar()
car1.display()
car1.returncar()
car1.display()
car1.buycar()
car1.display()
car1.sellcar()
car1.display()