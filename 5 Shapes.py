import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((240, 240, 240))

rect_color = (120, 220, 190)
ellipse_color = (100, 200, 170)
outline_color = (0, 0, 0)

count = 1
x = 0
while count <= 5:

    rect = pygame.Rect(count * 80 - 60, 100, 40, 200)

    pygame.draw.rect(window, rect_color, rect)
    x += 1
    pygame.draw.rect(window, outline_color, rect, x)

    pygame.draw.ellipse(window, ellipse_color, rect)
    pygame.draw.ellipse(window, outline_color, rect, x)

    pygame.display.flip()
    pygame.time.wait(1000)
    count += 1
