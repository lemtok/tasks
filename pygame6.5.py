import os
import sys
import random

import pygame

size = 500, 500
FPS = 60

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Boom them all - 2")
clock = pygame.time.Clock()
bombs = []


def load_image(name, colorkey=None):
    name = os.path.join('data', name)
    if not os.path.isfile(name):
        print(f"Файл с изображением '{name}' не найден")
        sys.exit()
    image = pygame.image.load(name)
    return image


class Bomb(pygame.sprite.Sprite):
    bomb_image = load_image("bomb.png")
    boom_image = load_image("boom.png")

    def __init__(self, bombs, *group):
        super().__init__(*group)
        self.image = Bomb.bomb_image
        self.rect = self.image.get_rect()
        while True:
            self.rect.x = random.randrange(500 - self.rect.width)
            self.rect.y = random.randrange(500 - self.rect.height)
            if not any(self.rect.colliderect(p) for p in bombs):
                bombs.append(self.rect.copy())
                break

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.boom_image


if __name__ == '__main__':
    pygame.init()
    all_sprites = pygame.sprite.Group()
    for _ in range(10):
        Bomb(bombs, all_sprites)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)

        screen.fill((0, 0, 0))

        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
