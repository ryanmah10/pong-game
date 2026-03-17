import pygame
from sprite import Art

class Movement:
    def move(self):
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

            # bounce off top and bottom walls (ball_y, not ball_speed_y)
        if self.ball_y <= 10 or self.ball_y >= 590:
            self.ball_speed_y *= -1
        if self.ball_x <= 0 or self.ball_x >= 800:
            if self.ball_x <= 0:
                    self.scoreP2 += 1  # past left paddle = P2 scores
            else:
                self.scoreP1 += 1   # past right paddle = P1 scores
            self.ball_x = 400
            self.ball_y = 300
            pygame.time.delay(200)
        

                # bounce off paddles: use a rect for the ball and check collision
        ball_rect = pygame.Rect(self.ball_x - 10, self.ball_y - 10, 20, 20)
        if ball_rect.colliderect(self.paddle_left) and self.ball_speed_x < 0:
            self.ball_speed_x *= -1
            self.ball_x = self.paddle_left.right + 10   # nudge out so it doesn't stick
        if ball_rect.colliderect(self.paddle_right) and self.ball_speed_x > 0:
            self.ball_speed_x *= -1
            self.ball_x = self.paddle_right.left - 10