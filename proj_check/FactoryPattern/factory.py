from abc import ABC, abstractmethod


class Pet(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass


class Dog(Pet):

    def speak(self):
        print(f"Dog {self.name} whoops")


class Cat(Pet):

    def speak(self):
        print(f"Cat {self.name} meows")


#tommy = Dog("Tommy")
#tommy.speak()

#pussy = Cat("Pussy")
#pussy.speak()


def get_pet(pet_name):
    pet_dict = dict(Tommy=Dog("Tommy"), Pussy=Cat("Pussy"))
    return pet_dict[pet_name]

pussy = get_pet("Tommy")
pussy.speak()