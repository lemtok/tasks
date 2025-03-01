import pygame

pygame.init()


def draw():
    y = 150 - width / 4
    x = 150 - width * 0.75
    half = width / 2

    color_front = pygame.Color('white')
    color_upper = pygame.Color('white')
    color_side = pygame.Color('white')
    hsv = pygame.Color('white').hsva

    color_front.hsva = (hue, hsv[1] + 100, hsv[2] - 25, hsv[3])
    color_upper.hsva = (hue, hsv[1] + 100, hsv[2], hsv[3])
    color_side.hsva = (hue, hsv[1] + 100, hsv[2] - 50, hsv[3])

    pygame.draw.polygon(screen, color_front, ((x, y), (x + width, y), (x + width, y + width), (x, y + width)))
    pygame.draw.polygon(screen, color_upper, (
        (x + half, y - half), (x + half + width, y - half), (x + width, y), (x, y)))
    pygame.draw.polygon(screen, color_side, (
        (x + width, y), (x + half + width, y - half), (x + half + width, y + half),
        (x + width, y + width)))


if __name__ == '__main__':
    try:
        width, hue = map(int, input().split())
    except ValueError:
        raise ValueError('Неправильный формат ввода')

    if width % 4 != 0 or 0 or hue < 0 or hue > 360 or width > 100:
        raise ValueError('Неправильный формат ввода')

    size = (300, 300)
    screen = pygame.display.set_mode(size)
    draw()
    
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()