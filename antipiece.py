from piece import *
from constantes import anti

class anti(Piece): 
    def __init__(self, x, y, anti):
        self.x = x
        self.y = y
        self.anti = pygame.transform.scale(anti, (taille_case, taille_case))


    def dessiner(self, fenetre):
        fenetre.blit(self.anti (self.x * taille_case, self.y * taille_case, taille_case, taille_case))