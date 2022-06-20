'''Código para tocar mp3 utilizando pygame.'''

import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
