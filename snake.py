import pygame
from constantes import *




class Personnage:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplacer(self, touche):
        if touche == pygame.K_LEFT:
            self.x -= 1
        elif touche == pygame.K_RIGHT:
            self.x += 1
        elif touche == pygame.K_UP:
            self.y -= 1
        elif touche == pygame.K_DOWN:
            self.y += 1

    def dessiner(self, fenetre):
        pygame.draw.rect(fenetre, vert, (self.x * taille_case, self.y * taille_case, taille_case, taille_case))

    def collision(self):
        # Vérifie si le personnage entre en collision avec un des bords de la map
        if self.x < 0 or self.x >= largeur_fenetre:
            self.x = self.x % largeur_fenetre
        elif self.y < 0 or self.y >= hauteur_fenetre:
            self.y = self.y % hauteur_fenetre