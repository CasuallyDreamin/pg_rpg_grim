import pygame, sys
from gameobjects import *
from area import *
from phyiscshandler import *
#init 
FPS = 60
TILE_SIDE_SIZE = 64
g_map = game_map
pygame.init()
screen = pygame.display.set_mode((1024, 512), pygame.FULLSCREEN)
dt = pygame.time.Clock().tick(FPS)/1000

def img_imp(filename, scale=1.0):
    img = pygame.image.load('images/' + filename).convert_alpha()
    return pygame.transform.scale(img, (TILE_SIDE_SIZE*scale,TILE_SIDE_SIZE*scale))


#import sprites
gt.sprite = img_imp('ground_tile.png')
at.sprite = img_imp('air_tile.png')
player_sprite = img_imp('player.png')
basic_sword_sprite = img_imp('basic_sword.png',0.5)

#init base entities
entity_list = []

player = entity(sprite=player_sprite, pos=(64,448))
entity_list.append(player)

#init base items
item_dict = {}
basic_sword = item(name="basic_sword",sprite=basic_sword_sprite)
item_dict[basic_sword.name] = basic_sword
player.eq['wep'] = basic_sword

#def bools
running = True
pressed_left = False
pressed_right = False
pressed_jump = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pressed_left = True
            if event.key == pygame.K_d:
                pressed_right = True
            if event.key == pygame.K_SPACE:
                pressed_jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                pressed_left = False
            if event.key == pygame.K_d:
                pressed_right = False
            if event.key == pygame.K_SPACE:
                pressed_jump = False
    
    player_physics(pl=player,dt=dt, l=pressed_left, r=pressed_right, j=pressed_jump)
    entity_list = update_pos(entity_list)
    screen.fill('black')

    #render note: the +128 is to move the game window to the center in fullscreen, otherwise it'd be at the top.
    #render area
    for j ,row in enumerate(game_map):
        for i, tileinrow in enumerate(row):
            screen.blit(tileinrow.sprite,(i*TILE_SIDE_SIZE,j*TILE_SIDE_SIZE+128))
    #render entities
    for ent in entity_list:
        screen.blit(ent.sprite,ent.pos)
        ent.wep_to_pos()
        if ent.eq['wep'] != '':
            screen.blit(item_dict[ent.eq['wep'].name].sprite, ent.wep_pos)

    pygame.display.flip()

