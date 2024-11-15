from abc import ABC, abstractmethod

class Entity(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass
