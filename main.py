import pygame
import os
import time
import random
pygame.font.init()


#creating_window
width, height = 800, 700
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
bg= pygame.transform.scale((pygame.image.load("pics/background-black.png")), (width, height))

class Ship:
    def __init__(self,x,y,health=100):
        self.x = x
        self.y = y
        self.health= health
        self.ship_img= None
        self.laser_img= None
        self.lasers=[]
        self.cool_count= 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def ship_width(self):
        return self.ship_img.get_width()

    def ship_height(self):
        return self.ship_img.get_height()

    

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x,y,health)
        self.ship_img= yellow_space_ship
        self.laser_img= yellow_laser
        self.mask= pygame.mask.from_surface(self.ship_img)
        self.max_health= health

class Enemy(Ship):
    colours={
        "red": (red_space_ship, red_laser)
        "green": (green_space_ship, green_laser)
        "blue": (blue_space_ship, blue_laser)
    }

    def __init__(self,x,y,colour,health=100):
        super().__init__(x,y,health)
        self.ship_img, self.laser_img= self.colours[colour]
        self.mask= pygame.mask.from_surface(self.ship_img)

    def move(self,vel):
        self.y+=vel



def main():
    run=True
    fps=60
    level=0
    lives=5
    player_vel=5
    main_font= pygame.font.SysFont("sans serif", 50)

    player= Player(300, 650)

    enemies = []
    wave_length=5
    enemy_vel=1

    clock= pygame.time.Clock()


    def redraw_window():
        win.blit(bg,(0,0))
        #drawing_text
        lives_label= main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label= main_font.render(f"Level: {level}", 1, (255,255,255))
        
        win.blit(lives_label, (10,10))
        win.blit(level_label, (width-level_label.get_width()-10, 10))

        for enemy in enemies:
            enemy.draw(win)
        
        player.draw(win)
        pygame.display.update()

    while run:
        clock.tick(fps)
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run= False
        
        keys= pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (player.x-player_vel)>0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and (player.x+player_vel+player.ship_width())<width:
            player.x += player_vel
        if keys[pygame.K_UP] and (player.y-player_vel)>0:
            player.y -= player_vel
        if keys[pygame.K_DOWN] and (player.y+player_vel+player.ship_height())<height:
            player.y += player_vel

        redraw_window()

        





main()