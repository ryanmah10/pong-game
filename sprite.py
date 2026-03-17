import pygame


class Art:
    def draw(self):
        self.paddle_left.clamp_ip(self.screen.get_rect())
        self.paddle_right.clamp_ip(self.screen.get_rect())
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen, (255, 255, 255), self.paddle_left)    
        pygame.draw.rect(self.screen, (255, 255, 255), self.paddle_right)
        pygame.draw.circle(self.screen, (255, 255, 255), (self.ball_x, self.ball_y), 10,)
        score_font = pygame.font.SysFont("Arial", 20)
        score = score_font.render(f"{self.scoreP1} : {self.scoreP2}", True, (255, 255, 255))
        self.screen.blit(score, (350, 20))

        pygame.display.update()
        self.clock.tick(144)