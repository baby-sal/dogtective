# 3. Inheritance - Hero class inheriting from Character
# super()
# Subclass own attribute and methods
# create new NPC class with role attribute, and speak method

from encapsulation_example import Character

#UPDATE ME

class Hero(Character):
    def __init__(self, name, health, special_power):
        super().__init__(name, health)
        self._special_power = special_power

    def use_special_power(self):
        return f"{self.name} uses {self._special_power}!"


class NPC(Character):
    def __init__(self, name, health, role):
        super().__init__(name, health)  # Inherit name and health from Character
        self.role = role  # Additional attribute for NPC

    def speak(self):
        return f"{self.name} the {self.role} says: 'Welcome Stranger!'"
