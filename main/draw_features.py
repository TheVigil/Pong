''' draw the arena, paddles, and ball'''

import pygame
import sys
from pygame.locals import *

LINE_THICKNESS = 20  # line thickness for drawing
PADDLE_SIZE = 60  # size of the main paddles
PADDLE_PADDING = 30  # padding between arena boundaries and the paddles

W_WIDTH = 500
W_HEIGHT = 400

# color definitions for drawing in the display window:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

CANVAS = pygame.display.set_mode((W_WIDTH, W_HEIGHT))


def draw_play_area():

    # draw the play area in the main display window with the following info:
    # ::param:: main.DISPLAY tells pygame in which display to draw
    # ::param:: WHITE defines the color of the rectangle we are drawing
    # ::param:: (tuple w/(0,0), etc...) define the dimension of the rectangle with (0,0) as upper left corner
    # and (W_WIDTH...) as lower right
    # ::param:: (LINE_THICKNESS * 2) ensures the line thickness isn't cut in half by the borders of the window
    pygame.draw.rect(CANVAS, WHITE, ((0, 0), (W_WIDTH, W_HEIGHT)), (LINE_THICKNESS * 2))

    # use pygame.draw.line(window, color, ((startXY), (endXY)) line_thickness),
    # to draw the center line of our play area - (LINE_THICKNESS/5) ensures the center line is thinner than our borders:

    pygame.draw.line(CANVAS, WHITE, (int(W_WIDTH/2), 0), (int(W_WIDTH/2), (int(W_HEIGHT))), int(LINE_THICKNESS/4))


def draw_player_paddles(paddle):

    # draw the p1 and p2 paddles

    # first, ensure the paddle cannot move too low or too high using pygame's
    # built in .top and .bottom attributes for rectangle objects:
    if paddle.bottom > (W_HEIGHT - LINE_THICKNESS):
        paddle.bottom = (W_HEIGHT - LINE_THICKNESS)
    elif paddle.top < LINE_THICKNESS:
        paddle.top = LINE_THICKNESS

    # create the paddle:
    pygame.draw.rect(CANVAS, WHITE, paddle)


def draw_ball(ball):

    # use draw.rect and our predefined ball from pong.py to create the ball:
    pygame.draw.rect(CANVAS, WHITE, ball)





