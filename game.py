import sys

from snake2 import NvPers
from snake import Personnage
from map import Carte
from piece import Piece
from constantes import *
from antipiece import anticoin


def main():
    pygame.init()

    
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
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            elif event.type == pygame.KEYDOWN:
                personnage.deplacer(event.key)
                pers2.deplacer(event.key)
        
        fenetre.fill(blanc)

       
        Carte.dessiner(fenetre)
     
        personnage.dessiner(fenetre)
        pers2.dessiner(fenetre)
       
        for piece in pieces:
            piece.dessiner(fenetre)

        if pers2.score  + personnage.score >= 30 :        
           antipiece.dessiner_antipieces(fenetre, antipieces, personnage, pers2)
        
                 
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
      
        pygame.display.flip()

        
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    main()