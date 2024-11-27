from entity import Entity
from user_interface.game_config import HEIGHT

# class for NPC and player entities
class Character(Entity):

    def __init__(self, name, health=100):
        super().__init__(name)
        self.health = health
        self.x = 50
        self.y = HEIGHT / 2
        self.vel = 4
        self.width = 100
        self.height = 50

    def draw(self):
        pass

    def collision_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. Remaining health: {self.health}")

    def __str__(self):
        return f"{self.name}: Health ({self.health})"


# sample outputs for testing only:
if __name__ == "__main__":
    a = Character("Kharma Chameleon")
    print(a)
    a.collision_damage(10)