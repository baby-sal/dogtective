from abc import ABC, abstractmethod

# abstract class to be inhereted by game objects like Player and Obstacle
class Entity(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass
