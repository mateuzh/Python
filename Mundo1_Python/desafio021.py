'''Código para tocar mp3 utilizando pygame.'''

import pygame

pygame.init()
pygame.mixer.music.load('fogos.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
