class Button:
	def __init__(self, image, pos_x, pos_y, font, colour, click_colour, text_in):
		self.image = image
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.font = font
		self.colour = colour
		self.click_colour = click_colour
		self.text_in = text_in
		self.text = self.font.render(self.text_in, True, self.colour)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
		self.rect_text = self.text.get_rect(center=(self.pos_x, self.pos_y))

	def update_button(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.rect_text)

	def check_input(self, pos):
		if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False
	#
	# def click_colour(self,pos):
	# 	if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
	# 		self.text = self.font.render(self.text, True, self.click_colour)
	# 	else:
	# 		self.text = self.font.render(self.text, True, self.colour)