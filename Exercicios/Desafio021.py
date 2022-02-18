"""
Faça um programa em python que abra e reproduza O AUDIO DE UM ARQUIVO MP3
"""
import pygame
pygame.init()
pygame.mixer.music.load('musica que você deseja') # obs; precisa estar no mesmo diretório ok?
pygame.mixer.music.play()
pygame.event.wait()
