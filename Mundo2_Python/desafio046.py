#contagem regressiva para estouro de fogos de artificio com som

from time import sleep
import pygame
import emoji

print('Contagem para o estouro dos fogos de artifício: ')
for c in range(10, 0, -1):
    print(c, '...')
    sleep(1)
print(emoji.emojize('BOOM!!:boom:', use_aliases=True))
pygame.init() #inicia pygame
pygame.mixer.music.load('artificio.mp3') #carrega o mp3
pygame.mixer.music.play() #inicia o mp3
input()
pygame.event.wait()