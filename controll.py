import pygame
import sys  

class Controll:
    def controls(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.paddle_left.y -= 5
        if keys[pygame.K_s]:
            self.paddle_left.y += 5

        if keys[pygame.K_UP]:
            self.paddle_right.y -= 5
        if keys[pygame.K_DOWN]:
            self.paddle_right.y += 5