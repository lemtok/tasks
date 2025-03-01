import pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption('Я слежу за тобой!')
size = (200, 200)

if __name__ == '__main__':
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    count = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if  event.type == pygame.ACTIVEEVENT and event.state == pygame.APPACTIVE and event.gain == 0:
                count += 1

        out = pygame.font.Font(None, 100).render(str(count), True, 'red')
        screen.blit(out, (100 - out.get_rect().width / 2, 100 - out.get_rect().height / 2))

        pygame.display.update()
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.quit()