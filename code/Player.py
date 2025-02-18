#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.jump = False
        self.velocity = 0
        self.gravity = 1
        self.jump_strength = 15
        self.initial_y = position[1]  # Guarda a posição inicial no eixo Y

    def move(self):
        pressed_key = pygame.key.get_pressed()

        # Movimento para frente/tráz
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= ENTITY_SPEED[self.name]  # Move para trás
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.x += ENTITY_SPEED[self.name]  # Move para frente

        # Salto ao pressionar a barra de espaço
        if pressed_key[pygame.K_SPACE] and not self.jump:
            self.jump = True
            self.velocity = -self.jump_strength  # Impulso para cima

        # Aplicação da gravidade e retorno ao solo
        if self.jump:
            self.rect.y += self.velocity
            self.velocity += self.gravity  # Aceleração para baixo

            # Se atingir o solo, para o salto
            if self.rect.y >= self.initial_y:
                self.rect.y = self.initial_y
                self.jump = False
                self.velocity = 0