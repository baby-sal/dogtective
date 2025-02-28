from user_interface.text_loader import Text
from user_interface.image_loader import Image


class Screen:
    def __init__(self, display, runner):
        self.display = display
        self.runner = runner
        self.text = Text(display)
        self.image = Image(display)
