import random
import pygame
from constantes import case_max_x, case_max_y, violet, taille_case

class Piece:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.score = 0

    def collision(self, personnage):
        if (personnage.x == self.x) and (personnage.y == self.y):

            # Update the score
            personnage.score += 10

            # Change the piece's position
            while True:
                new_x = random.randint(0, case_max_x)
                new_y = random.randint(0, case_max_y)

                # Check if the new position overlaps with any existing pieces
                pieces = []
                pieces.append(Piece(new_x, new_y))

                if personnage.x == new_x and personnage.y == new_y:
                    break
                else:
                    self.x = new_x
                    self.y = new_y
                    break

        else:
            return False

    def check_position(self, new_x, new_y):
        # Check if the new position is within the boundaries of the map
        if new_x < 0 or new_x >= case_max_x:
            return False

        if new_y < 0 or new_y >= case_max_y:
            return False

        return True

    def dessiner(self, fenetre):
        pygame.draw.rect(fenetre, violet, (self.x * taille_case, self.y * taille_case, taille_case, taille_case))
