'''this portion of the program creates a blank screen to eventually house the arena, paddles etc.
the main game loop is also housed here, within the main() function.'''


# importing from/the pygame library, which will be used to implement pong
# pygame contains a number of useful libraries for developing games in python

import sys
import pygame
from pygame.locals import *
from drawing_tools import draw_features as draw


# variables defined and functions in draw_features.py, for drawing paddles, play area, ball etc.

# Global variable to define the frame rate.
# Higher framerates increase the speed, slower decrease the speed

FRAMES_PER_SECOND = 200

# define the dimensions of the display window
W_WIDTH = 500
W_HEIGHT = 400


# main function to handle the initialization of the game. Draws the display window and contains the main game loop

def main():

    pygame.init()  # initialize pygame evironment
    framerate_clock = pygame.time.Clock()  # control the framerate
    global DISPLAY
    DISPLAY = pygame.display.set_mode((W_WIDTH, W_HEIGHT))  # a display surface for pygame to draw on
    # draw the ball in its initial position in the XY grid.
    ball_x_coord = W_WIDTH/2 - draw.LINE_THICKNESS/2  # compensate the center position
    ball_y_coord = W_WIDTH / 2 - draw.LINE_THICKNESS / 2  # w.r.t. the thickness of our lines

    # define the player paddles in their initial positions
    p1_position = (W_HEIGHT - draw.PADDLE_SIZE) / 2
    p2_position = (W_HEIGHT - draw.PADDLE_SIZE) / 2

    # create the ball and player paddles using
    # pygame.Rect((X co-ordinate, Y co-ordinate, Width of Rectangle, Length of Rectangle)

    p1_paddle = pygame.Rect(draw.PADDLE_PADDING, p1_position, draw.LINE_THICKNESS,
                            draw.PADDLE_SIZE)

    p2_paddle = pygame.Rect((W_WIDTH - draw.PADDLE_PADDING - draw.LINE_THICKNESS),
                            p2_position, draw.LINE_THICKNESS, draw.PADDLE_SIZE)

    # the above definition of the ::param:: X in p2_paddle sets the p2_paddle
    # on the opposite side of the x-axis from p1_paddle

    ball = pygame.Rect(ball_x_coord, ball_y_coord, draw.LINE_THICKNESS, draw.LINE_THICKNESS)

    # draw the features
    draw.draw_play_area()
    draw.draw_player_paddles(p1_paddle)
    draw.draw_player_paddles(p2_paddle)
    draw.draw_ball(ball)

    pygame.display.set_caption('Pi Pong')  # title the window

    while True:  # main loop of the game

        # drawing of features should be constantly updated while main loop is running
        # updates occur at every clock tick, as defined below

        draw.draw_play_area()
        draw.draw_player_paddles(p1_paddle)
        draw.draw_player_paddles(p2_paddle)
        draw.draw_ball(ball)

        # for - loop checks registered events for a quit event, allowing the game loop to be exited
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

        framerate_clock.tick(FRAMES_PER_SECOND)  # advance the clock at our desired fps


if __name__ == '__main__':
    main()

