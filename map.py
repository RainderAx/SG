from constantes import hauteur_fenetre,largeur_fenetre,taille_case,noir,    pygame

class Carte:

    @staticmethod
    def dessiner(fenetre):
        for y in range(0, hauteur_fenetre, taille_case):
            for x in range(0, largeur_fenetre, taille_case):
                pygame.draw.rect(fenetre, noir, (x, y, taille_case, taille_case), 1)
