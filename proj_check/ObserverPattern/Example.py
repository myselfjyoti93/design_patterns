from abc import ABC, abstractmethod

class Subscriber(metaclass=ABC):

    @abstractmethod
    def update(self, publisher, *args):
        pass

class Publisher:

    def __init__(self):
        self.__subscribers = []

    def add_subsriber(self, subscriber):
        self.__subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify_subscribers(self, args):
        for subscrber in self.__subscribers:
            subscrber.update(self, *args)

class Tweet_User(Publisher):

    def __init__(self, name):
        super.__init__()
        self.__name = name

    def follow(self, user):
        self.add_subsriber()