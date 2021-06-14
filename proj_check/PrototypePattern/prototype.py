import copy

class Prototype:
    def __init__(self):
        self.object = {}

    def register_obj(self, name, obj):
        self.object[name] = obj

    def unregister_obj(self, name):
        del self.object[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self.object[name])
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.model = "Skylark"
        self.colour = "red"
        self.option = "AC"

    def __str__(self):
        return "Car : {} | {} | {}".format(self.model, self.colour, self.option)

c = Car()
prototype = Prototype()
prototype.register_obj("Car", c)
c1 = prototype.clone("Car")
print(c1)