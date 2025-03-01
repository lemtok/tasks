import pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption('К щелчку')
size = (501, 501)

if __name__ == '__main__':
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    x, y = int(501 / 2), int(501 / 2)
    x_navigation, y_navigation = x, y
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_navigation, y_navigation = event.pos

        s_x, s_y = x - x_navigation, y - y_navigation
        if x != x_navigation or y != y_navigation:
            if s_y < 0:
                y += 1
            elif s_y > 0:
                y -= 1
            if s_x < 0:
                x += 1
            elif s_x > 0:
                x -= 1
        x, y = int(x), int(y)

        pygame.draw.circle(screen, 'red', (x, y), 20)
        pygame.display.flip()
        screen.fill('black')
        clock.tick(60)

    pygame.quit()