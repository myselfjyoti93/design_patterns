from abc import ABC, abstractmethod


class Pet(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass


class Dog(Pet):

    def __init__(self):
        pass

    def speak(self):
        return "Whoops!"

    def __str__(self):
        return "Dog"


class DogFactory:

    def get_dog(self):
        return Dog()

    def get_food(self):
        return "Dog Food!"


class PetStore:

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_dog()
        pet_food = self._pet_factory.get_food()

        print("out pet is '{}' !".format(pet))
        print("Our dog speaks '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))


dog_factory = DogFactory()

pet_shop = PetStore(dog_factory)

pet_shop.show_pet()