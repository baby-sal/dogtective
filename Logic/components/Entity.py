from abc import ABC, abstractmethod

# abstract class to be inherited by game objects like Player and Obstacle classes
class Entity(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass
