import pygame
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:  #evenement d appui de la souris
        print pygame.mouse.get_pos()
