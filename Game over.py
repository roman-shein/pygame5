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
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)

    running = True
    screen.fill("blue")

    image = load_image("gameover.png")

    clock = pygame.time.Clock()
    v = 200
    x_pos = 0

    while running:
        screen.fill("blue")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        t = clock.tick()
        if x_pos <= 600:
            x_pos += v / 1000 * t
            screen.blit(image, (x_pos - image.get_width(), 0))
            pygame.display.flip()

    pygame.quit()
