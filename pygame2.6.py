import pygame
import math

change_v = 50 / 60
pygame.init()
size = 201, 201
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Вентилятор")
clock = pygame.time.Clock()
angle = -90
FPS = 60

if __name__ == '__main__':
    running = True
    v = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    v -= change_v
                elif event.button == 3:
                    v += change_v

        screen.fill('black')
        angle += v

        for b in range(0, 360, 120):
            left = (angle - 15 + b) * math.pi / 180
            right = (angle + 15 + b) * math.pi / 180
            x_left = size[0] // 2 + 70 * math.cos(left)
            y_left = size[1] // 2 + 70 * math.sin(left)
            x_right = size[0] // 2 + 70 * math.cos(right)
            y_right = size[1] // 2 + 70 * math.sin(right)

            pygame.draw.polygon(screen, pygame.Color('white'),
                                ((size[0] // 2, size[1] // 2), (x_left, y_left), (x_right, y_right)))

        pygame.draw.circle(screen, pygame.Color('white'), (size[0] // 2, size[1] // 2), 10)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()