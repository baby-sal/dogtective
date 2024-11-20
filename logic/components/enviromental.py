from entity import Entity


class Environmental(Entity):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Name: {self.name}"

    def draw(self):
        pass