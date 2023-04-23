import sys
import pygame
pygame.Surface.set_colorkey
import game_functions as gf

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (0,0,255)
    image = pygame.image.load('images/ship.bmp')
    image_rect = image.get_rect()
    screen_rect = screen.get_rect()
    centerx = screen_rect.centerx
    centery = screen_rect.centery
    image_rect.centerx = centerx
    image_rect.centery = centery

    while True:

        screen.fill(bg_color)
        screen.blit(image, image_rect)
        pygame.display.flip()

        gf.check_events()

        
        

run_game()