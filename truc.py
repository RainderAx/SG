import pygame

def jouer_musique(fichier):
    pygame.mixer.init()
    pygame.mixer.music.load(fichier)
    pygame.mixer.music.play()

fichier_mp3 = "chemin/vers/ton/fichier.mp3"
jouer_musique(fichier_mp3)
