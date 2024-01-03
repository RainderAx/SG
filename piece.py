
from constantes import case_max_x, case_max_y, taille_case,pygame, random

class Piece:
    
    def __init__(self, x, y, coin_image):
        self.x = x
        self.y = y
        self.coin_image = pygame.transform.scale(coin_image, (taille_case, taille_case))

    def collision(self, personnage):
        if (personnage.x == self.x) and (personnage.y == self.y):
            personnage.score += 10
            while True:
                new_x = random.choice([random.randint(0, max(0, personnage.x -3 )), random.randint(min(case_max_x - 1, personnage.x + 3), case_max_x - 1)])
                new_y = random.choice([random.randint(0, max(0, personnage.y -3 )), random.randint(min(case_max_y - 1, personnage.y + 3), case_max_y - 1)])

                pieces = []
                pieces.append(Piece(new_x, new_y, self.coin_image))

                if personnage.x == new_x and personnage.y == new_y:
                    break
                else:
                    self.x = new_x
                    self.y = new_y
                    break
        else:
            return False

    def check_position(self, new_x, new_y):
        if new_x < 0 or new_x >= case_max_x:
            return False

        if new_y < 0 or new_y >= case_max_y:
            return False

        return True

    def dessiner(self, fenetre):
        fenetre.blit(self.coin_image, (self.x * taille_case, self.y * taille_case, taille_case, taille_case))
