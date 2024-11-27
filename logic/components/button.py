class Button():
	def __init__(self, image, pos_x, pos_y):
		self.image = image
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

	def update_button(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.image, self.rect)

	def check_input(self, pos):
		if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False