from user_interface.text_loader import Text
from user_interface.image_loader import Image


class Screen:
    def __init__(self, display):
        self.display = display
        self.text = Text(display)
        self.image = Image()
