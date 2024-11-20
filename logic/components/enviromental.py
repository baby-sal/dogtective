from entity import Entity


# this will need more functionality to justify its existence at some point
class Environmental(Entity):

    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        pass

    def __str__(self):
        return f"Name: {self.name}"


class Obstacle(Environmental):

    def __init__(self, name, damage, speed):
        super().__init__(name)
        self.damage = damage
        self.speed = speed

    def draw(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Damage:{self.speed}, Speed: {self.speed}, "


if __name__ == "__main__":
    tree = Environmental("tree")
    print(tree)
    car = Obstacle("car", 10, 2)
    print(car)
