import pygame, sys
from gameobjects import *
from area import *
#init 
TILE_SIDE_SIZE = 64
g_map = game_map
pygame.init()
screen = pygame.display.set_mode((1024, 512), pygame.FULLSCREEN)

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

player = entity(sprite=player_sprite, pos=(1,5))
entity_list.append(player)

#init base items
item_dict = {}
basic_sword = item(name="basic_sword",sprite=basic_sword_sprite)
item_dict[basic_sword.name] = basic_sword
player.eq['wep'] = basic_sword


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    screen.fill('black')
    #render note: the +128 is to move the game window to the center in fullscreen, otherwise it'd be at the top.
    #render area
    for j ,row in enumerate(game_map):
        for i, tileinrow in enumerate(row):
            screen.blit(tileinrow.sprite,(i*TILE_SIDE_SIZE,j*TILE_SIDE_SIZE+128))
    #render entities
    for ent in entity_list:
        entity_pos = (ent.pos[0]*TILE_SIDE_SIZE, ent.pos[1]*TILE_SIDE_SIZE+128)
        screen.blit(ent.sprite,entity_pos)
        if ent.eq['wep'] != '':
            screen.blit(item_dict[ent.eq['wep'].name].sprite, (entity_pos[0]+32,entity_pos[1]+16))

    pygame.display.flip()

