import pygame
from constantes import *
from snake import Personnage

class NvPers(Personnage):  

    def __init__(self, x, y):
        super().__init__(x, y)  
        
    def deplacer(self, touche):
        if touche == pygame.K_q:
            self.x -= 1
        elif touche == pygame.K_d:
            self.x += 1
        elif touche == pygame.K_z:
            self.y -= 1
        elif touche == pygame.K_s:
            self.y += 1

    def collision(self):

        if self.x < 0 or self.x >= case_max_x:
            self.x = self.x % (case_max_x)

        elif self.y < 0 or self.y >= case_max_y:
            self.y = self.y % (case_max_y)

    def dessiner(self, fenetre):
        pygame.draw.rect(fenetre, violet, (self.x * taille_case, self.y * taille_case, taille_case, taille_case))
