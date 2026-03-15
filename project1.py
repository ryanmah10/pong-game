import pygame
import sys

class Game:
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

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #controlls for left and right paddles
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.paddle_left.y -= 5
            if keys[pygame.K_s]:
                self.paddle_left.y += 5

            if keys[pygame.K_UP]:
                self.paddle_right.y -= 5
            if keys[pygame.K_DOWN]:
                self.paddle_right.y += 5
            
            # ball movement
            self.ball_x += self.ball_speed_x
            self.ball_y += self.ball_speed_y

            # bounce off top and bottom walls (ball_y, not ball_speed_y)
            if self.ball_y <= 10 or self.ball_y >= 590:
                self.ball_speed_y *= -1
            if self.ball_x <= 0 or self.ball_x >= 800:
                if self.ball_x <= 0:
                    self.scoreP2 += 1   # past left paddle = P2 scores
                else:
                    self.scoreP1 += 1   # past right paddle = P1 scores
                self.ball_x = 400
                self.ball_y = 300
    

            # bounce off paddles: use a rect for the ball and check collision
            ball_rect = pygame.Rect(self.ball_x - 10, self.ball_y - 10, 20, 20)
            if ball_rect.colliderect(self.paddle_left) and self.ball_speed_x < 0:
                self.ball_speed_x *= -1
                self.ball_x = self.paddle_left.right + 10   # nudge out so it doesn't stick
            if ball_rect.colliderect(self.paddle_right) and self.ball_speed_x > 0:
                self.ball_speed_x *= -1
                self.ball_x = self.paddle_right.left - 10

            #drawing for paddle/ball 
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
Game().run()
