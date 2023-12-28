from constantes import hauteur_fenetre,pygame


largeur_fenetre = 600
hauteur_fenetre = 600
taille_case = 50

blanc = (255, 255, 255)
noir = (0, 0, 0)


class Carte:

    @staticmethod
    def dessiner(fenetre):
        for y in range(0, hauteur_fenetre, taille_case):
            for x in range(0, largeur_fenetre, taille_case):
                pygame.draw.rect(fenetre, noir, (x, y, taille_case, taille_case), 1)
