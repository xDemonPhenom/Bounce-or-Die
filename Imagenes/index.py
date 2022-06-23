from turtle import circle
import pygame
import sys
from pygame.locals import *

pygame.init()

Intro = pygame.display.set_mode((622, 1000))
pygame.display.set_caption("Bounce or Die")

width = 1200
height = 870

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)

Intro.fill(White)

Pj01 = pygame.image.load("Imagenes/Pj01.png")
TPj01 = pygame.transform.scale(Pj01, (250, 280))

Pj02 = pygame.image.load("Imagenes/Pj02.png")
TPj02 = pygame.transform.scale(Pj02, (250, 280))

Pj03 = pygame.image.load("Imagenes/Pj03.png")
TPj03 = pygame.transform.scale(Pj03, (250, 280))

Pj04 = pygame.image.load("Imagenes/Pj04.png")
TPj04 = pygame.transform.scale(Pj04, (250, 280))

Select = pygame.image.load("Imagenes/options.png")
TSelect = pygame.transform.scale(Select, (800, 100))

Background = pygame.image.load("Imagenes/inicio.jpg")
SecondScreen = pygame.image.load("Imagenes/second.jpg")

Welcome = pygame.image.load("Imagenes/Welcome.png")
TWelcome = pygame.transform.scale(Welcome, (420, 150))

Skull = pygame.image.load("Imagenes/craneo.png")
TSkull = pygame.transform.scale(Skull, (250, 400))


IntroText = pygame.font.SysFont('comicsans', 35, True)
SelectText = pygame.font.SysFont('Verdana', 55, True)

Music = "Imagenes/inicio.mp3"
MusicBg = pygame.mixer.music.load(Music)
pygame.mixer.music.play(-1)

Intro.blit(Background, (0, 0))
Intro.blit(TWelcome, (100, 200))
Intro.blit(TSkull, (175, 380))
pygame.display.flip


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    Continue = IntroText.render(
        'Presione ENTER para continuar...', 1, (255, 255, 255))
    Intro.blit(Continue, (25, 800))

    Key = pygame.key.get_pressed()
    if Key[pygame.K_RETURN]:
        Screen = pygame.display.set_mode((width, height))
        Screen.blit(SecondScreen, (0, 0))
        Screen.blit(TPj01, (70, 380))
        Screen.blit(TPj02, (300, 400))
        Screen.blit(TPj03, (550, 400))
        Screen.blit(TPj04, (850, 400))
        Screen.blit(TSelect, (180, 180))

    pygame.display.update()
