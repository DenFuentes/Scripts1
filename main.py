import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('BTM2D.01')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

stage_surface = pygame.image.load('Graphics/Stage.png').convert()
#ground
score_surface = test_font.render('My Game', False, (64,64,64))
score_rectangle = score_surface.get_rect(center = (400, 50))

tomatoe_surface1 = pygame.image.load('Character/Pixelated tomatoes.v4.xcf').convert_alpha()
tomatoe_rectangle = tomatoe_surface1.get_rect(bottomright = (600, 277))

player_surface = pygame.image.load('Character/Pixelated Q.xcf').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,277))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rectangle.collidepoint(event.pos): print("Collision")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    #Background and screen
    screen.blit(stage_surface,(0,0))
    pygame.draw.rect(screen, '#c0e8ec', score_rectangle)
    pygame.draw.rect(screen, '#c0e8ec', score_rectangle, 4, 2)
    screen.blit(score_surface,score_rectangle)
    #Tomatoe
    tomatoe_rectangle.x -= 5
    if tomatoe_rectangle.right <= 0:tomatoe_rectangle.left = 800
    screen.blit(tomatoe_surface1,tomatoe_rectangle)

    #Player
    player_gravity += 1
    player_rectangle.y += player_gravity
    screen.blit(player_surface,player_rectangle)
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print("Jump")

    #if player_rectangle.colliderect(tomatoe_rectangle):
    #    print("Collision")

    #mouse_position = pygame.mouse.get_pos()
    #if player_rectangle.collidepoint(mouse_position):
    #    print("Hovering Over PLayer")

    pygame.display.update()
    clock.tick(60)
