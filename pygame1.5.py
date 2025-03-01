import pygame


def draw():
    step = 150 // n
    screen.fill(pygame.Color('black'))
    for i in range(0, n):
        pygame.draw.ellipse(screen, (255, 255, 255), (i * step, 0, 300 - i * 2 * step, 300), 1)
        pygame.draw.ellipse(screen, (255, 255, 255), (0, i * step, 300, 300 - i * 2 * step), 1)


if __name__ == '__main__':
    pygame.init()
    try:
        n = int(input())
    except ValueError:
        raise ValueError('Неправильный формат ввода')

    size = (300, 300)
    screen = pygame.display.set_mode(size)
    draw()
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()