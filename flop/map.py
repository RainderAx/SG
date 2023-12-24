import pygame

# Paramètres de la fenêtre
largeur_fenetre = 600
hauteur_fenetre = 600
taille_case = 50

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# Paramètres du jeu
WIDTH, HEIGHT = 800, 600
FPS = 10

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

class Map:
    # Dessiner la carte
    for y in range(0, hauteur_fenetre, taille_case):
        for x in range(0, largeur_fenetre, taille_case):
            pygame.draw.rect(fenetre, noir, (x, y, taille_case, taille_case), 1)