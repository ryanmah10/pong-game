import pygame
import sys


class PaddleBall:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Pong")


        self.paddle_left = pygame.Rect(10, 300, 10, 100)
        self.paddle_right = pygame.Rect(790, 300, 10, 100)


        self.ball_x = 400
        self.ball_y = 300
        self.ball_speed_x = 3
        self.ball_speed_y = 3

        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.scoreP1 = 0
        self.scoreP2 = 0
