def has_internal(self, sprite):
    for group in self.groups.values():
        if sprite in group:
            return True
    return False

def add_internal(self, sprite, group_name):
    if group_name in self.groups:
        self.groups[group_name].add(sprite)
    else:
        print(f"Group {group_name} not found!")

def add_sprite(self, sprite):
    if hasattr(sprite, "_spritegroup"):
        for spr in sprite.sprites():
            if not self.has_internal(spr):
                self.add_internal(spr, spr._spritegroup)
                spr.add_internal(self)
            elif not self.has_internal(sprite):
                self.add_internal(sprite, sprite._spritegroup)
                sprite.add_internal(self)

def render_background_image(self):
    self.game_display.blit(self.background_image, (0, 0))

def render_all(self, *groups):
    for group in groups:
        group.draw(self.game_display)
        group.update()

def render_dog(self, car_group):
    self.dog_group.draw(self.game_display)
    self.dog_group.update(car_group)
