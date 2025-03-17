#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_image = []
                for i in range(5): # Numero de imagens
                    list_image.append(Background(f'Level1Bg{i}', (0,0)))
                    list_image.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_image
            case 'Level2Bg':
                list_image = []
                for i in range(7): # Numero de imagens
                    list_image.append(Background(f'Level2Bg{i}', (0,0)))
                    list_image.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_image

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT -80))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(150, WIN_HEIGHT -30)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint( 150, WIN_HEIGHT - 35)))
            case 'Enemy3':
                return Enemy('Enemy3', (WIN_WIDTH + 10, random.randint(150, WIN_HEIGHT - 40)))