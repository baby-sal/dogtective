import pygame

class Lost_toy(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ball_img = pygame.image.load(
                    '../logic/assets/images/objects/ball.png').convert_alpha()
                ball = Environmental("ball", ball_img, self.dis_width * 0.96,
                                     self.dis_height * 0.95, 0.1)
                self.final_screen_ball_group = pygame.sprite.Group()
                self.final_screen_ball_group.add(ball)


def render_final_screen_ball(self, ball):
    self.final_screen_ball_group.draw(self.game_display)
    self.final_screen_ball_group.update(ball)


ball_active = False

self.render_final_screen_ball(self.final_screen_ball_group)