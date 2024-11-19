# 4. Abstraction -> what ABC means
# @abstractmethod
# example below of Character class inheriting from Entity ABC

from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def interact(self):
        pass

    def get_info(self):
        return f"{self.name}: {self.description}"
