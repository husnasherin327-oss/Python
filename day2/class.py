class Cars:
    def __init__(self,name,price,colour):
        self.name=name
        self.price=price
        self.colour=colour

    def start(self):
        print(self.name + "engin started")
car1=Cars("maruthi swift",10000,"red")
car2=Cars("toyota innove",30000,"white")
print(car1.name)
print(car2.name)        