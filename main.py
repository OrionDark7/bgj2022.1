import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))

running = True
screen = "game"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if screen == "game":
        pass
    pygame.display.flip()
pygame.quit()