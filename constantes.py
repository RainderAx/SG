import pygame 


#taille_carte
taille_case = 50
largeur_fenetre = 600
hauteur_fenetre = 600

case_max_x = largeur_fenetre/taille_case
case_max_y = hauteur_fenetre/taille_case

#couleur 
blanc = (255, 255, 255)
noir = (0, 0, 0)
vert = (107, 142, 35)
violet = (148,113,220)

#skin
coin_image = pygame.image.load("coin.jpg")
anti = pygame.image.load("anti.jpg")