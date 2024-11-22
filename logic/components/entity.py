from abc import ABC, abstractmethod


# abstract class to be inherited by game objects like Player and Obstacle classes
class Entity(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
