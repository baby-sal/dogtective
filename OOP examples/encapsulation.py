# 2. encapsulation - updated Character class
# private attributes
# getters
# setters

#UPDATE ME

class Character:

    total_characters = 0

    def __init__(self, name, health):
        self.name = name
        self._health = health  # Encapsulated variable
        Character.total_characters += 1

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def attack(self, target):
        damage = 10
        # Note how I'm using the getter to calculate the new health by retrieving the current health and applying damage
        new_health = target.get_health() - damage
        # Also note here how I'm using the setter to set the new health value
        target.set_health(new_health)
        return f"{self.name} attacks {target.name} for {damage} damage! {target.name} now has {new_health} health."
