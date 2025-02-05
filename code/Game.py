#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Gevel import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):


        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                leve = Level(self.window, 'Level1', menu_return)
                pass
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()  # quit window fechamento janela
                quit()
            else:
                pass
                # quit pygame







