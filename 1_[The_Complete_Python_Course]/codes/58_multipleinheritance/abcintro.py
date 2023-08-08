from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print("It can walk")

    @abstractmethod
    def legs(self):
        return 3


class Dog(Animal):
    def legs(self):  # making this object is necessary
        return 4


# print(Animal.legs())
