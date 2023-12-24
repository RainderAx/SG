import pygame
import sys
import random


from snake import *
from map import *
from piece import Piece


def main():
    pygame.init()

    # Initialisation de la fenêtre
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Personnage sur une carte")

    # Création du personnage
    personnage = Personnage(1, 1)

    # Création de la pièce
    pieces = []

    piece = Piece(random.randint(0, case_max_x), random.randint(0, case_max_y))
    pieces.append(piece)


    # Boucle principale
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Gestion des touches pour le déplacement
            elif event.type == pygame.KEYDOWN:
                personnage.deplacer(event.key)

        # Effacement de l'écran
        fenetre.fill(blanc)

        # Dessin de la carte
        Carte.dessiner(fenetre)

        # Dessin du personnage
        personnage.dessiner(fenetre)

        # Dessin de la pièce
        for piece in pieces:
            piece.dessiner(fenetre)

        # Vérification des collisions
        personnage.collision()
        piece.collision(personnage)

        # Dessin de la pièce
        piece.dessiner(fenetre)

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter la vitesse de la boucle
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    main()
