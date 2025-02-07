#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_image = []
                for i in range(5):
                    list_image.append(Background(f'Level1Bg{i}', (0,0)))
                    list_image.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_image

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT -90))