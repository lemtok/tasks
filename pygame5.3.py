import os
import sys
import pygame

all_sprites = pygame.sprite.Group()
size = 600, 95
FPS = 60


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Car(pygame.sprite.Sprite):
    image = load_image("car2.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Car.image
        self.rect = self.image.get_rect(midleft=(0, size[1] // 2))
        self.v = 2

    def update(self):
        self.rect.x += self.v
        if self.rect.right >= size[0] or self.rect.left <= 0:
            self.v = -self.v
            self.image = pygame.transform.flip(self.image, True, False)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Машинка")
    clock = pygame.time.Clock()
    car = Car(all_sprites)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()