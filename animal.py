class animal():
    def __init__(self,name,type,sound):
        self.name = name
        self.type = type
        self.sound = sound
    def display(self):
        print(self.name,self.type,self.sound)
animal1 = animal("bob","lion","roar")
animal1.display()