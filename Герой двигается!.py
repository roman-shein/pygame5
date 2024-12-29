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
    pygame.display.set_caption('Герой двигается!')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)

    running = True
    screen.fill("white")

    image = load_image("creature.png")

    x, y = 0, 0

    screen.blit(image, (x, y))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                y -= 10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                y += 10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                x += 10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                x -= 10
            screen.fill("white")
            screen.blit(image, (x, y))
        pygame.display.flip()

    pygame.quit()
