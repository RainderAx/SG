from snake import *

class NvPers(Personnage):  
        
    def deplacer(self, touche):
        if touche == pygame.K_q:
            self.x -= 1
        elif touche == pygame.K_d:
            self.x += 1
        elif touche == pygame.K_z:
            self.y -= 1
        elif touche == pygame.K_s:
            self.y += 1

    def dessiner(self, fenetre):
        pygame.draw.rect(fenetre, violet, (self.x * taille_case, self.y * taille_case, taille_case, taille_case))
