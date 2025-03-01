import pygame


def zoom(center, value):
    points_n = []
    x_center, y_center = center
    for x, y in points:
        new_y = (y - y_center) * value + y_center
        new_x = (x - x_center) * value + x_center
        points_n.append((new_x, new_y))
    return points_n


pygame.init()
size = 501, 501
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zoom")
clock = pygame.time.Clock()
FPS = 60


if __name__ == '__main__':
    with open("points.txt", "r") as file:
        text = map(lambda x: str.replace(x, ",", "."), file.read().split(", "))
        points = list(map(lambda x: list(map(float, x[1:-1].split(";"))), text))

    points = list(map(lambda x: [x[0] + size[0] // 2, (-x[1]) + size[1] // 2], points))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    points = zoom((size[0] // 2, size[1] // 2), 1.1)
                elif event.y < 0:
                    points = zoom((size[0] // 2, size[1] // 2), 0.9)

        screen.fill((0, 0, 0))
        pygame.draw.polygon(screen, pygame.Color('white'), points, 1)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()