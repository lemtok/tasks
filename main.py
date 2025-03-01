import pygame
import sys
import os

FPS = 30

pygame.init()
size = WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
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


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png'),
    't': load_image('arrow.png')
}
player_image = load_image('mario.png')
tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, group, pos_x, pos_y):
        super().__init__(group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.x = pos_x
        self.y = pos_y
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', tiles_group, x, y)
            elif level[y][x] == '#':
                Tile('wall', wall_group, x, y)
            elif level[y][x] == 't':
                Tile('t', teleport_group, x, y)
            elif level[y][x] == '@':
                Tile('empty', tiles_group, x, y)
                new_player = Player(x, y)
    return new_player, x, y


if __name__ == '__main__':
    running = True
    player = None
    map_number = 1
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    teleport_group = pygame.sprite.Group()
    start_screen()
    player, level_x, level_y = generate_level(load_level('map1.txt'))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                player.rect.x += 50
                if pygame.sprite.spritecollideany(player, wall_group):
                    player.rect.x -= 50
            elif keys[pygame.K_LEFT]:
                player.rect.x -= 50
                if pygame.sprite.spritecollideany(player, wall_group):
                    player.rect.x += 50
            elif keys[pygame.K_UP]:
                player.rect.y -= 50
                if pygame.sprite.spritecollideany(player, wall_group):
                    player.rect.y += 50
            elif keys[pygame.K_DOWN]:
                player.rect.y += 50
                if pygame.sprite.spritecollideany(player, wall_group):
                    player.rect.y -= 50
            if pygame.sprite.spritecollideany(player, teleport_group):
                groups = [all_sprites, player_group,  tiles_group, wall_group, teleport_group]
                for group in groups:
                    for elem in group:
                        group.remove(elem)
                map_number += 1

                player, level_x, level_y = generate_level(load_level(f'map{map_number}.txt'))
        all_sprites.update()
        tiles_group.draw(screen)
        wall_group.draw(screen)
        teleport_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
