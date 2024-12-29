import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Пример 1')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    screen.fill("black")

    image = load_image("arrow.png")

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_focused():
                screen.fill((0, 0, 0))
                screen.blit(image, event.pos)
                pygame.mouse.set_visible(False)
            if not pygame.mouse.get_focused():
                screen.fill((0, 0, 0))
                pygame.mouse.set_visible(True)
        pygame.display.flip()
        clock.tick(100)


    pygame.quit()
