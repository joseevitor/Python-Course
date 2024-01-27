import pygame

pygame.init()


music = str(input('Tell wich music you want to listen: '))
pygame.mixer.music.load(music)
pygame.mixer.music.play()
input()
pygame.event.wait()