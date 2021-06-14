class Director:
    def __init__(self, builder):
        self._builder = builder
    def constructCar(self):
        self._builder.addModel()
        self._builder.addTyre()
        self._builder.addEngine()
    def getCar(self):
        return self._builder.car

class Car:
    def __init__(self):
        self.model = None
        self.tires = None
        self.engines = None

    def __str__(self):
        return "Car : {} | {} | {}".format(self.model, self.tires, self.engines)



class Builder:
    def __init__(self):
        self._car = None

    def createNewCar(self):
        self.car = Car()

class SkylerBuilder(Builder):
    def addModel(self):
        self.car.model = "Skylark"
    def addTyre(self):
        self.car.tires = 4
    def addEngine(self):
        self.car.engines = "Turbo"


builder = SkylerBuilder()
builder.createNewCar()
director = Director(builder)
director.constructCar()
print(director.getCar())