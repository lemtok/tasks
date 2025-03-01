import os
import sys
import pygame

pygame.init()
size = 600, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game over")
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    game_over_image = load_image("gameover.png")
    game_over_rect = game_over_image.get_rect(topright=(0, 0))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color('blue'))
        if game_over_rect.x < 0:
            game_over_rect.x += 200 // 60
        screen.blit(game_over_image, game_over_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()