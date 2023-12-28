from piece import *
from constantes import anti

class anti(Piece): 
    def __init__(self, x, y, anti):
        self.x = x
        self.y = y
        self.anti = pygame.transform.scale(anti, (taille_case, taille_case))

    def collision(self, personnage):
            if (personnage.x == self.x) and (personnage.y == self.y):
                personnage.score += 10
                while True:
                    new_x = random.randint(personnage.x + 3, case_max_x - 1)
                    new_y = random.randint(personnage.y + 3 , case_max_y - 1)

                    pieces = []
                    pieces.append(Piece(new_x, new_y, self.anti))

                    if personnage.x == new_x and personnage.y == new_y:
                        break
                    else:
                        self.x = new_x
                        self.y = new_y
                        break
            else:
                return False
            
    def dessiner(self, fenetre):
        fenetre.blit(self.anti (self.x * taille_case, self.y * taille_case, taille_case, taille_case))