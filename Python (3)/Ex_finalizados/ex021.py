'''Tocando um MP3
Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

import pygame
pygame.init()
pygame.mixer.music.load('Sunshine.mp3')
pygame.mixer.music.play()
pygame.event.wait()
