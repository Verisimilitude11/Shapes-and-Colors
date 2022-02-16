import pygame

pygame.init()

window = pygame.display.set_mode([400, 300])

gray = (175, 175, 175)

purple = (120, 120, 240)

left = pygame.Rect(0, 0, 200, 300)

pygame.draw.rect(window, gray, left)

right = pygame.Rect(200, 0, 200, 300)

pygame.draw.rect(window, purple, right)

mid  = (150, 150, 200)

pygame.draw.circle(window, mid, (100, 150), 20)

pygame.draw.circle(window, mid, (300, 150), 20)

pygame.display.flip()

input("Press enter to pause the program")

white = (255, 255, 255)
window.fill(white)

pygame.draw.circle(window, mid, (300, 150), 20)
pygame.draw.circle(window, mid, (100, 150), 20)

pygame.display.flip()

input()
