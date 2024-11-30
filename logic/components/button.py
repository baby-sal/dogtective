class Button:
	def __init__(self, pos_x, pos_y, font, colour, click_colour, text):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.font = font
		self.colour = colour
		self.click_colour = click_colour
		self.text = text
		self.rect = self.text.get_rect(center=(self.pos_x, self.pos_y))

	def update_button(self, screen):
		screen.blit(self.text, self.rect)

	def check_input(self, pos):
		if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	# def click_colour(self,pos):
	# 	if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
	# 		self.text = self.font.render(self.text, True, self.click_colour)
	# 	else:
	# 		self.text = self.font.render(self.text, True, self.colour)