import pygame
import sys
from ball import PaddleBall
from controll import Controll
from sprite import Art
from movement import Movement


class PongGame(PaddleBall, Controll, Movement, Art):
    def __init__(self):
        PaddleBall.__init__(self)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            self.controls()
            self.move()
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    PongGame().run()
