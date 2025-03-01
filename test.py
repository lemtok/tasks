import pygame
from random import randint


class Board:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.grid = [[0] * cols for _ in range(rows)]
        self.offset_x = 10
        self.offset_y = 10
        self.cell_size = 30

    def set_view(self, offset_x, offset_y, cell_size):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.cell_size = cell_size

    def render(self, screen):
        colors = [(0, 0, 0), (255, 0, 0), (0, 0, 255)]
        border_color = (255, 255, 255)
        for row in range(self.rows):
            for col in range(self.cols):
                x = self.offset_x + self.cell_size * col
                y = self.offset_y + self.cell_size * row
                pygame.draw.rect(screen, colors[self.grid[row][col]], (x, y, self.cell_size, self.cell_size))
                pygame.draw.rect(screen, border_color, (x, y, self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        x_rel = mouse_pos[0] - self.offset_x
        y_rel = mouse_pos[1] - self.offset_y
        if x_rel < 0 or y_rel < 0:
            return None
        col = x_rel // self.cell_size
        row = y_rel // self.cell_size
        if row >= self.rows or col >= self.cols:
            return None
        return col, row

    def on_click(self, position):
        if position:
            col, row = position
            self.grid[row][col] = (self.grid[row][col] + 1) % 3

    def handle_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Minesweeper(Board):
    def __init__(self, cols, rows, mine_count):
        super().__init__(cols, rows)
        self.grid = [[-1] * cols for _ in range(rows)]
        self.place_mines(mine_count)

    def place_mines(self, mine_count):
        for _ in range(mine_count):
            row, col = randint(0, self.rows - 1), randint(0, self.cols - 1)
            while self.grid[row][col] == 10:
                row, col = randint(0, self.rows - 1), randint(0, self.cols - 1)
            self.grid[row][col] = 10

    def render(self, screen):
        colors = [(0, 0, 0), (255, 0, 0)]
        border_color = (255, 255, 255)
        for row in range(self.rows):
            for col in range(self.cols):
                x = self.offset_x + self.cell_size * col
                y = self.offset_y + self.cell_size * row
                pygame.draw.rect(screen, colors[1 if self.grid[row][col] == 10 else 0],
                                 (x, y, self.cell_size, self.cell_size))
                pygame.draw.rect(screen, border_color, (x, y, self.cell_size, self.cell_size), 1)
                if 0 <= self.grid[row][col] <= 8:
                    font = pygame.font.Font(None, (self.cell_size * 2) // 3)
                    text = font.render(str(self.grid[row][col]), True, (0, 255, 0))
                    screen.blit(text, (x + self.cell_size // 15, y + self.cell_size // 15))

    def on_click(self, position):
        if position:
            col, row = position
            if self.grid[row][col] == -1:
                self.open_cell(position)

    def open_cell(self, position):
        col, row = position
        mine_count = sum(
            1 for i in range(-1, 2) for j in range(-1, 2)
            if 0 <= row + i < self.rows and 0 <= col + j < self.cols and self.grid[row + i][col + j] == 10
        )
        self.grid[row][col] = mine_count


if __name__ == '__main__':
    pygame.init()
    screen_size = (620, 620)
    screen = pygame.display.set_mode(screen_size)
    game = Minesweeper(10, 10, 10)
    game.set_view(10, 10, 60)

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(event.pos)
        game.render(screen)
        pygame.display.flip()
    pygame.quit()
