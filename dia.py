import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur_fenetre = 600
hauteur_fenetre = 600
taille_case = 50

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Personnage sur une carte")

# Position initiale du personnage
x_personnage = 0
y_personnage = 0

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gestion des touches pour le déplacement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_personnage > 0:
                x_personnage -= 1
            elif event.key == pygame.K_RIGHT and x_personnage < (largeur_fenetre // taille_case) - 1:
                x_personnage += 1
            elif event.key == pygame.K_UP and y_personnage > 0:
                y_personnage -= 1
            elif event.key == pygame.K_DOWN and y_personnage < (hauteur_fenetre // taille_case) - 1:
                y_personnage += 1

    # Effacer l'écran
    fenetre.fill(blanc)

    # Dessiner la carte
    for y in range(0, hauteur_fenetre, taille_case):
        for x in range(0, largeur_fenetre, taille_case):
            pygame.draw.rect(fenetre, noir, (x, y, taille_case, taille_case), 1)

    # Dessiner le personnage
    pygame.draw.rect(fenetre, noir, (x_personnage * taille_case, y_personnage * taille_case, taille_case, taille_case))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    pygame.time.Clock().tick(10)
