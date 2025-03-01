import os
import sys
import pygame
import random

pygame.init()
all_sprites = pygame.sprite.Group()
size = 1000, 1000
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Boom them all")
clock = pygame.time.Clock()
FPS = 60


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Bomb(pygame.sprite.Sprite):
    bomb_image = load_image("bomb1.png")
    boom_image = load_image("bomb2.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.bomb_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(size[0] - self.rect.size[0])
        self.rect.y = random.randrange(size[1] - self.rect.size[1])

    def update(self, *args):
        if args:
            if args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                self.image = self.boom_image


if __name__ == '__main__':
    for i in range(20):
        Bomb(all_sprites)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)

        screen.fill('black')
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()