from constantes import vert, taille_case,case_max_x,case_max_y,   pygame

class Personnage:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.score = 0

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

        if self.x < 0 or self.x >= case_max_x:
            self.x = self.x % (case_max_x)

        elif self.y < 0 or self.y >= case_max_y:
            self.y = self.y % (case_max_y)

