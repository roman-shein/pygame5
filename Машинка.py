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


class Car(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("car2.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.v = 1

    def update(self):
        self.rect = self.rect.move(self.v, 0)
        if self.rect.x + self.rect.width >= 600:
            self.image = pygame.transform.flip(self.image, True, False)
            self.v = -1
        elif self.rect.x <= 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.v = 1


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Пример 1')
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)

    running = True
    screen.fill("white")

    all_sprites = pygame.sprite.Group()
    Car(all_sprites)

    clock = pygame.time.Clock()
    fps = 30
    x_pos = 0

    while running:
        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(fps)
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()

    pygame.quit()
