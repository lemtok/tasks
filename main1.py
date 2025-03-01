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
        self.colours = {0: pygame.Color('white'), 1: pygame.Color('red'), 2: pygame.Color('blue')}
        self.step = 1

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
                if h[i] == 1:
                    pygame.draw.line(screen, pygame.Color('blue'), (left + 2, top + 2), (left - 2 + self.cell_size - 2, top - 2 + self.cell_size - 2), 3)
                    pygame.draw.line(screen, pygame.Color('blue'), (left - 2 + self.cell_size - 2, top + 2), (left + 2, top - 2 + self.cell_size - 2), 3)
                elif h[i] == 2:
                    pygame.draw.circle(screen, pygame.Color('red'), (left + self.cell_size // 2, top + self.cell_size // 2), self.cell_size // 2 - 2, 3)
                left += self.cell_size
            top += self.cell_size
            left = self.left

    def change(self, x_pos, y_pos):
        if not self.board[y_pos][x_pos]:
            if self.step % 2 != 0:
                self.board[y_pos][x_pos] = 1
            else:
                self.board[y_pos][x_pos] = 2
            self.step += 1


if __name__ == '__main__':
    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x_pos = (x - board.left) // board.cell_size
                y_pos = (y - board.top) // board.cell_size
                if 0 <= x_pos <= board.width - 1 and 0 <= y_pos <= board.height - 1:
                    print((x_pos, y_pos))
                    board.change(x_pos, y_pos)
                else:
                    print(None)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()