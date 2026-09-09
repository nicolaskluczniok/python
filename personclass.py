
class person():
    def __init__(self,name,age,contact,country):
        self.name = name
        self.age = age 
        self.contact = contact
        self.country = country
    def display(self):
        print(self.name,self.age,self.contact,self.country)
        
person1 = person("hi","1","p","l")
person1.display()
    
person2 = person("bye","2","o","hi")    
person2.display()