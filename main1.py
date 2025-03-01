import pygame

pygame.init()
size = WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode(size)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 50

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        top = self.top
        left = self.left
        for h in self.board:
            for i in range(len(h)):
                pygame.draw.rect(screen, pygame.Color('white'), (left, top, self.cell_size, self.cell_size), 1)
                left += self.cell_size
            top += self.cell_size
            left = self.left


if __name__ == '__main__':
    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()