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
                if h[i] == 0:
                    pygame.draw.rect(screen, pygame.Color('white'), (left, top, self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, pygame.Color('white'), (left, top, self.cell_size, self.cell_size))
                left += self.cell_size
            top += self.cell_size
            left = self.left

    def change(self, x_pos, y_pos):
        for row in range(len(self.board)):
            if row != y_pos:
                if self.board[row][x_pos] == 0:
                    self.board[row][x_pos] = 1
                else:
                    self.board[row][x_pos] = 0
            else:
                print(1)
                for i in range(len(self.board[row])):
                    if self.board[row][i] == 0:
                        self.board[row][i] = 1
                    else:
                        self.board[row][i] = 0



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