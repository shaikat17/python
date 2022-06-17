import pygame
from time import sleep

pygame.init()
pygame.mixer.init()


window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.mixer.music.load("sound.wav")
pygame.mixer.music.play()

sleep(5)

pygame.mixer.music.load("ghost_laughing.mp3")
pygame.mixer.music.play()


image = pygame.image.load("ghost.jpeg")

window.blit(image,(0,0))

pygame.display.update()

sleep(5)
