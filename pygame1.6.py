import pygame


def draw():
    screen.fill(pygame.Color('yellow'))
    for x in range(size[0] // n):
        for y in range(size[1] // n):
            pygame.draw.polygon(screen, pygame.Color('orange'), (
                (x * n + n / 2, y * n), (x * n, y * n + n / 2), (x * n + n / 2, y * n + n),
                (x * n + n, y * n + n / 2)))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Ромбики')

    try:
        n = int(input())
    except ValueError:
        raise ValueError('Неправильный формат ввода')

    size = (300, 300)  # размер окна
    screen = pygame.display.set_mode(size)
    draw()
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()