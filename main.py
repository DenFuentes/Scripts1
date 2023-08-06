import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('BTM2D.01')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

stage_surface = pygame.image.load('Graphics/Stage.png').convert()
#ground
text_surface = test_font.render('My Game', False, 'White')

tomatoe_Y = 277
tomatoe_surface1 = pygame.image.load('Character/Pixelated tomatoes.v4.xcf').convert_alpha()
tomatoe_rectangle = tomatoe_surface1.get_rect(midbottom = (600, tomatoe_Y))

player_surface = pygame.image.load('Character/Pixelated Q.xcf').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,277))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(stage_surface,(0,0))
    screen.blit(text_surface,(300,50))
    tomatoe_rectangle.left -= 5
    if tomatoe_rectangle.right <= 0:tomatoe_rectangle.left = 800
    screen.blit(tomatoe_surface1,tomatoe_rectangle)
    screen.blit(player_surface, player_rectangle)


    pygame.display.update()
    clock.tick(60)
