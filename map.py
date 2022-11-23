import pygame

# 0 is fill_dirt

grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [],
    [],
    [0, 0, 0, 0, 0, 0, 0],
    [],
    [],
    [],
    [0, 0, 0, 0, 0, 0, 0]
]

TILE_SIZE = 18

dirt_fill = pygame.image.load('images/Tiles/fill_dirt.png')

tiles = [dirt_fill]


def draw_background(bg_size):
    bg = pygame.Surface(bg_size)
    # draw each tile in the bg

    for r, grid_list in enumerate(grid):
        for t, grid_element in enumerate(grid_list):
    # blit the correct tile on the screen
            bg.blit(tiles[grid_element], (t*TILE_SIZE, r*TILE_SIZE))
    return bg