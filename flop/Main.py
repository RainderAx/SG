import pygame
import sys
from snake import Snake

# Paramètres de la fenêtre
largeur_fenetre = 600
hauteur_fenetre = 600
taille_case = 50

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# Paramètres du jeu
WIDTH, HEIGHT = 800, 600
FPS = 10

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Define the Map class
class Map:

    # Draw the map
    def __init__(self):
        for y in range(0, hauteur_fenetre, taille_case):
            for x in range(0, largeur_fenetre, taille_case):
                pygame.draw.rect(fenetre, noir, (x, y, taille_case, taille_case), 1)

    # Check for collision with map boundaries
    def is_collision(self, x, y):
        # Check if the x-coordinate is out of bounds
        if x < 0 or x >= largeur_fenetre // taille_case:
            return True

        # Check if the y-coordinate is out of bounds
        if y < 0 or y >= hauteur_fenetre // taille_case:
            return True

        # Return False if no collision detected
        return False
    def place_player(self, x, y):
        # Draw a red rectangle at the specified coordinates
        pygame.draw.rect(fenetre, RED, (x * taille_case, y * taille_case, taille_case, taille_case))

pygame.init()

# Game parameters
WIDTH, HEIGHT = 800, 600
FPS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

game_map = Map()  # Create the map object
snake = Snake(WIDTH // 2, HEIGHT // 2, game_map)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.x > 0:
                snake.x -= 1
            elif event.key == pygame.K_RIGHT and snake.x < (largeur_fenetre // taille_case) - 1:
                snake.x += 1
            elif event.key == pygame.K_UP and snake.y > 0:
                snake.y -= 1
            elif event.key == pygame.K_DOWN and snake.y < (hauteur_fenetre // taille_case) - 1:
                snake.y += 1

    head_x, head_y = snake.get_head_position()

    if game_map.is_collision(head_x, head_y) or (head_x, head_y) in snake.get_body()[1:]:
        pygame.quit()
        sys.exit()

    game_map.place_player(head_x, head_y)

    screen.fill(WHITE)
    for x, y in snake.get_body():
        pygame.draw.rect(screen, RED, (x, y, 20, 20))
    pygame.display.flip()

    clock.tick(FPS)
