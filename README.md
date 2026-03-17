Pong Game Description
Here's a description of your Pong implementation:
Overview
A classic two-player Pong game built with Pygame, running at 144 FPS on an 800×600 window.
Players & Controls

Player 1 (left paddle): W / S keys
Player 2 (right paddle): Up / Down arrow keys

Gameplay

Both players control a white paddle and try to deflect the ball past their opponent
The ball bounces off the top and bottom walls, and reverses direction when it hits a paddle
If the ball passes the left edge, Player 2 scores; if it passes the right edge, Player 1 scores
After each point, the ball resets to the center of the screen
The current score is displayed at the top center in the format P1 : P2

Technical Details

Paddles are clamped to the screen so they can't move off-screen
Collision detection uses pygame.Rect.colliderect() with a directional check to prevent the ball from sticking to a paddle
Ball speed is fixed at 3px/frame on both axes, with no acceleration mechanic
