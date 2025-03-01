import pygame

SIZE = 500, 500
FPS = 60

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Платформы")
clock = pygame.time.Clock()


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.Surface((50, 10))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))
        
        
class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.Surface((20, 20))
        self.image.fill(pygame.Color('blue'))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.v = 50

    def update(self, *args):
        self.rect.y += self.v / FPS
        if pygame.sprite.spritecollideany(self, platforms):
            self.rect.y -= self.v / FPS

    def move(self, dx):
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, platforms):
            self.rect.x -= dx


if __name__ == '__main__':
    pygame.init()

    cube = None
    platforms = pygame.sprite.Group()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    platforms.add(Platform(*event.pos))
                elif event.button == 3:
                    cube = Cube(*event.pos)
            elif event.type == pygame.KEYDOWN and cube:
                if event.key == pygame.K_LEFT:
                    cube.move(-10)
                elif event.key == pygame.K_RIGHT:
                    cube.move(10)

        screen.fill((0, 0, 0))
        if cube:
            cube.update()
            screen.blit(cube.image, cube.rect)
        platforms.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
