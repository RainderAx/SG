from constantes import noir, taille_case,case_max_x,case_max_y,   pygame, random

class Ennemi:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.temps_ecoule = 0
        self.temps_update = 500

    def deplacer(self, touche):
        if touche == pygame.K_LEFT:
            self.x += random.randint(-1, 1)       
   
        elif touche == pygame.K_RIGHT:
            self.x += random.randint(-1, 1)       
 
        elif touche == pygame.K_UP:
            self.x += random.randint(-1, 1)       

        elif touche == pygame.K_DOWN:
            self.x += random.randint(-1, 1)       
        
        elif touche == pygame.K_q:
            self.y += random.randint(-1, 1) 

        elif touche == pygame.K_d:
    
            self.y += random.randint(-1, 1)
        elif touche == pygame.K_z:
   
            self.y += random.randint(-1, 1)
        elif touche == pygame.K_s:
     
            self.y += random.randint(-1, 1)

    def dessiner(self, fenetre):
     
        pygame.draw.rect(fenetre, noir, (self.x * taille_case, self.y * taille_case, taille_case, taille_case))

    def collision(self, personnage):
        if (personnage.x == self.x) and (personnage.y == self.y):
            personnage.score -= 10
                      
    def collision_mur(self):
        if self.x < 0 or self.x >= case_max_x:
            self.x = self.x % (case_max_x)

        elif self.y < 0 or self.y >= case_max_y:
            self.y = self.y % (case_max_y)