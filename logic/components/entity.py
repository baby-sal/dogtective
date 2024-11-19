from abc import ABC, abstractmethod


# abstract class to be inherited by game objects like Player and Obstacle classes
class Entity(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def collision_damage(self, damage):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Character(Entity):
    def __init__(self, name, health=100):
        super().__init__(name)
        self.health = health

    # not sure what this is used for?
    def draw(self):
        pass

    def collision_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. Remaining health: {self.health}")

    def __str__(self):
        return f"{self.name}: Health ({self.health})"


# sample outputs for testing only:
a = Character("Kharma Chameleon")
print(a)
a.collision_damage(10)
