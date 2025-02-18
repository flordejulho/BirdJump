import pygame

#C
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (71, 254, 255)
COLOR_WHITE = (255, 255,255)


# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_DAMAGE = { 'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Player1' : 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,

}

ENTITY_SCORE = {
'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Player1' : 0,
    'Enemy1': 10,
    'Enemy2': 50,
    'Enemy3': 60,
}

ENTITY_HEALTH = {
'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Player1' : 300,
    'Enemy1': 10,
    'Enemy2': 50,
    'Enemy3': 60,
}
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Player1' : 3,
    'Enemy1': 3,
    'Enemy2': 5,
    'Enemy3': 3,

}

# M

MENU_OPTION = ('NEW PLAYER 1',
               'SCORE',

               'EXIT')


# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
