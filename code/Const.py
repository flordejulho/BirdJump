import pygame

#C
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (71, 254, 255)
COLOR_WHITE = (255, 255,255)


# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
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
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Player1' : 0,
    'Enemy1': 10,
    'Enemy2': 10,
    'Enemy3': 10,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Level2Bg6': 999,
    'Player1' : 200,
    'Enemy1': 40,
    'Enemy2': 50,
    'Enemy3': 60,
}
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level2Bg5': 1,
    'Level2Bg6': 4,
    'Player1' : 4,
    'Enemy1': 3,
    'Enemy2': 5,
    'Enemy3': 3,
}
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2


# M

MENU_OPTION = ('NEW PLAYER 1',
               'SCORE',
               'EXIT')


# S
SPAWN_TIME = 2000


# T
TIMEOUT_LEVEL = 40000   #20ms
TIMEOUT_STEP = 100 #100ms


# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH /2, 110),
             1: (WIN_WIDTH /2, 130),
             2: (WIN_WIDTH /2, 150),
             3: (WIN_WIDTH /2, 170),
             4: (WIN_WIDTH /2, 190),
             5: (WIN_WIDTH /2, 210),
             6: (WIN_WIDTH /2, 230),
             7: (WIN_WIDTH /2, 250),
             8: (WIN_WIDTH /2, 270),
             9: (WIN_WIDTH /2, 290)
             }
