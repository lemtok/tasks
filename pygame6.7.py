import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 500, 500
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


class Upstairs(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.Surface((10, 50))
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect(topleft=(x, y))
        
        
class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 50

    def update(self, *args):
        self.rect.y += self.speed / FPS
        if pygame.sprite.spritecollideany(self, platforms) or pygame.sprite.spritecollideany(self, upstairs):
            self.rect.y -= self.speed / FPS

    def move(self, dx, dy=0):
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, platforms):
            self.rect.x -= dx

        if pygame.sprite.spritecollideany(self, upstairs):
            self.rect.y += dy
            

if __name__ == '__main__':

    cube = None
    platforms = pygame.sprite.Group()
    upstairs = pygame.sprite.Group()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        upstairs.add(Upstairs(*event.pos))
                    else:
                        platforms.add(Platform(*event.pos))
                elif event.button == 3:
                    cube = Cube(*event.pos)
            elif event.type == pygame.KEYDOWN and cube:
                if event.key == pygame.K_LEFT:
                    cube.move(-10)
                elif event.key == pygame.K_UP:
                    cube.move(0, -10)
                elif event.key == pygame.K_RIGHT:
                    cube.move(10)
                elif event.key == pygame.K_DOWN:
                    cube.move(0, 10)
        screen.fill((0, 0, 0))
        if cube:
            cube.update()
            screen.blit(cube.image, cube.rect)

        upstairs.draw(screen)
        platforms.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
