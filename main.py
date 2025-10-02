import pygame
import os
import time
import random


#creating_window
width, height = 750, 750
win= pygame.display.set_mode((width,height))
pygame.display.set_caption("Space Invaders Shootout")

#loading_images
red_space_ship= pygame.image.load("pics/pixel_ship_red_small.png")
green_space_ship= pygame.image.load("pics/pixel_ship_green_small.png")
blue_space_ship= pygame.image.load("pics/pixel_ship_blue_small.png")

#player_ship
yellow_space_ship= pygame.image.load("pics/pixel_ship_yellow.png")

#lasers
red_laser= pygame.image.load("pics/pixel_laser_red.png")
green_laser= pygame.image.load("pics/pixel_laser_green.png")
blue_laser= pygame.image.load("pics/pixel_laser_blue.png")
yellow_laser= pygame.image.load("pics/pixel_laser_yellow.png")

#background
bg= pygame.image.load("pics/background-black.png")


def main():
    run=True
    fps=60
    clock= pygame.time.Clock()

    def redraw_window():
        win.blit(bg,(0,0))
        pygame.display.update()

    while run:
        clock.tick(fps)
        redraw_window()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run= False





main()