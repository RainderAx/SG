from broly import *

class Gojo(Ennemi):

    def deplacer(self, touche):
        if touche == pygame.K_LEFT:
            self.y += random.randint(-1, 1)       
   
        elif touche == pygame.K_RIGHT:
            self.y += random.randint(-1, 1)       
 
        elif touche == pygame.K_UP:
            self.y += random.randint(-1, 1)       

        elif touche == pygame.K_DOWN:
            self.y += random.randint(-1, 1)       
        
        elif touche == pygame.K_q:
            self.x += random.randint(-1, 1) 

        elif touche == pygame.K_d:
            self.x += random.randint(-1, 1)

        elif touche == pygame.K_z:
            self.x += random.randint(-1, 1)

        elif touche == pygame.K_s:     
            self.x += random.randint(-1, 1)