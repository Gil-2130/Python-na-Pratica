"""
Faça um programa em python que abra e reproduza O AUDIO DE UM ARQUIVO MP3
"""
# Importando a biblioteca necessária
import pygame
# Inicializando a biblioteca
pygame.init()
# carregando o áudio + localização do mesmo
pygame.mixer.music.load('musica que você deseja') # obs; precisa estar no mesmo diretório ok?
# Executando o áudio
pygame.mixer.music.play()
# aguarde o player abrir
pygame.event.wait()
