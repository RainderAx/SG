from constantes import noir, taille_case,case_max_x,case_max_y,   pygame, random
from time import sleep as wait

class Ennemi:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.temps_ecoule = 0
        self.temps_update = 500

    def deplacer(self):
        for i in range(0, 500):
            new_x = self.x + random.randint(-1, 1)
            new_y = self.y + random.randint(-1, 1)
            self.x = new_x
            self.y = new_y
            

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