import sys

from snake2 import NvPers
from snake import Personnage
from map import Carte
from piece import Piece
from constantes import *
from antipiece import anticoin
from broly import Ennemi
from gojo  import Gojo
import constantes
from data import *


def main():
    pygame.init()

    constantes.jouer_musique("logobi.mp3")

    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Personnage sur une carte")

    personnage = Personnage(1, 1)
    pers2 = NvPers(10,10)

    pieces = []
    
    piece = Piece(random.randint(0, case_max_x -1), random.randint(0, case_max_y -1),coin_image)
    pieces.append(piece)

    antipieces = []

    antipiece = anticoin(random.randint(0, case_max_x -1), random.randint(0, case_max_y -1), anti)
    antipieces.append(antipiece)
    
    broly = Ennemi(random.randint(0, case_max_x -1), random.randint(0, case_max_y -1))
    gojo = Gojo(random.randint(0, case_max_x -1), random.randint(0, case_max_y -1))


    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            elif event.type == pygame.KEYDOWN:
                personnage.deplacer(event.key)
                pers2.deplacer(event.key)
                broly.deplacer(event.key)
                gojo.deplacer(event.key)

        donnees = collecter_donnees(personnage, pers2, gojo,broly)

        ecrire_donnees_csv(donnees, 'donnees_partie.csv')

        fenetre.fill(blanc)
   
        Carte.dessiner(fenetre)
     
        personnage.dessiner(fenetre)
        pers2.dessiner(fenetre)
       
        for piece in pieces:
            piece.dessiner(fenetre)

        if pers2.score + personnage.score >= 50 :        
           antipiece.dessiner_antipieces(fenetre, antipieces, personnage, pers2)

        if personnage.score + pers2.score >= 70:
            
            broly.dessiner(fenetre)
            broly.collision(personnage)
            broly.collision(pers2)
            broly.collision_mur()

            gojo.dessiner(fenetre)
            gojo.collision(personnage)
            gojo.collision(pers2)
            gojo.collision_mur()
                       
        personnage.collision()
        pers2.collision()
        piece.collision(personnage)
        piece.collision(pers2)

        piece.dessiner(fenetre)
        
        font = pygame.font.Font(None, 36)
        texte_score = font.render("Score:" + str(personnage.score), True, vert)
        fenetre.blit(texte_score, (10, 10))

        texte_score = font.render("Score:" + str(pers2.score), True, violet)
        fenetre.blit(texte_score, (10, 100))



        if personnage.score > 150:
            font = pygame.font.Font(None, 36)
            texte_score = font.render("Vous avez gagné", True, vert)
            fenetre.blit(texte_score, (largeur_fenetre // 2 - texte_score.get_width() // 2, hauteur_fenetre // 2 - texte_score.get_height() // 2))
            pygame.display.flip()
            pygame.time.Clock().tick(10)
            pygame.quit()
            sys.exit()

        if pers2.score > 150:
            font = pygame.font.Font(None, 36)
            texte_score = font.render("Vous avez gagné", True, violet)
            fenetre.blit(texte_score, (largeur_fenetre // 2 - texte_score.get_width() // 2, hauteur_fenetre // 2 - texte_score.get_height() // 2))
            pygame.display.flip()
            pygame.time.Clock().tick(10)
            pygame.quit()
            sys.exit()
      
        pygame.display.flip()

        
        pygame.time.Clock().tick(10)
       
if __name__ == "__main__":
    main()