import pygame

pygame.init()
pygame.display.set_caption('Перетаскивание')
size = (300, 300)

if __name__ == '__main__':
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    flag = False
    x, y = 0, 0
    prev_x, prev_y, next_x, next_y = 0, 0, 0, 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x < event.pos[0] < x + 100 and y < event.pos[1] < y + 100:
                    flag = True

            if event.type == pygame.MOUSEBUTTONUP:
                flag = False

            if event.type == pygame.MOUSEMOTION:
                if flag:
                    next_x, next_y = event.rel
                    x += next_x
                    y += next_y

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, 'green', (x, y, 100, 100))
        pygame.display.flip()
    pygame.quit()