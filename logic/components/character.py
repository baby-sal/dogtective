from entity import Entity


# class for NPC and player entities
class Character(Entity):

    def __init__(self, name, health=100):
        super().__init__(name)
        self.health = health

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