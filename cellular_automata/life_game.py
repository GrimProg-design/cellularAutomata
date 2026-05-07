import pygame
import sys
import os

pygame.init()
clock = pygame.time.Clock()

ROWS = 30
COLS = 50
CELL_SIZE = 20
FPS = 10

class Factory:
    def create_glider(grid, start_row=1, start_col=1):
        pattern = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ]

        for r in range(3):
            for c in range(3):
                if pattern[r][c] == 1:
                    if 0 <= start_row + r < grid.rows and 0 <= start_col + c < grid.cols:
                        grid.cells[start_row + r][start_col + c] = True
    
    def create_blinker(grid, start_row=1, start_col=1):
        pattern = [
            [0,0,0],
            [1,1,1],
            [0,0,0]
        ]

        for r in range(3):
            for c in range(3):
                if pattern[r][c] == 1:
                    if 0 <= start_row + r < grid.rows and 0 <= start_col + c < grid.cols:
                        grid.cells[start_row + r][start_col + c] =True
    
    def create_pulsar(grid, start_row=1, start_col=1):
        pattern = [
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0,0,1,1,1,0,0]
        ]

        for r in range(13):
            for c in range(13):
                if pattern[r][c] == 1:
                    if 0 <= start_row + r < grid.rows and 0 <= start_col + c < grid.cols:
                        grid.cells[start_row + r][start_col + c] = True
    
    def create_gosper_glider_gun(grid, start_row=1, start_col=1):
        pattern = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]

        for r in range(9):
            for c in range(36):
                if pattern[r][c] == 1:
                    if 0 <= start_row + r < grid.rows and 0 <= start_col + c < grid.cols:
                        grid.cells[start_row + r][start_col + c] = True
    
class Observer:
    def __init__(self, path='data.txt', stats_path='stats.txt'):
        base_path = os.path.dirname(os.path.abspath(__file__))
        
        self.path = os.path.join(base_path, path)
        self.stats_path = os.path.join(base_path, stats_path)

    def FileLogger(self, text):
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(text + '\n')

    def StatsLogger(self, generation, born, died):
        with open(self.stats_path, "w", encoding="utf-8") as file:
            file.write(
                f"Поколение: {generation} | Родилось: {born} | Умерло: {died}\n"
            )

class Grid:
    def __init__(self, rows, cols, cell_size=20):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.cells = []
        for row in range(rows):
            row_list = []
            for col in range(cols):
                row_list.append(False)
            self.cells.append(row_list)
        self.screen = pygame.display.set_mode((cols*cell_size, rows*cell_size))
        pygame.display.set_caption("My Game of Life")

    def draw_grid(self):
        self.screen.fill((255, 255, 255))
        for r in range(self.rows):
            for c in range(self.cols):
                if self.cells[r][c]:
                    x = c * self.cell_size
                    y = r * self.cell_size
                    pygame.draw.rect(self.screen, (0, 0, 0), 
                                     (x+1, y+1, self.cell_size-1, self.cell_size-1))
                    
        for c in range(self.cols + 1):
            x = c * self.cell_size
            pygame.draw.line(self.screen, (0, 0, 0), (x, 0), (x, self.rows*self.cell_size))
        for r in range(self.rows + 1):
            y = r * self.cell_size
            pygame.draw.line(self.screen, (0, 0, 0), (0, y), (self.cols*self.cell_size, y))

    def toggle_cell_at_pixel(self, x, y):
        col = x // self.cell_size
        row = y // self.cell_size
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.cells[row][col] = not self.cells[row][col]

    def next_generation(self):
        new_cells = []
        born = 0
        died = 0

        for row in range(self.rows):
            new_row = []
            for col in range(self.cols):
                new_row.append(False)
            new_cells.append(new_row)

        for r in range(self.rows):
            for c in range(self.cols):
                alive_neighbors = self.count_alive_neighbors(r, c)

                if self.cells[r][c]:
                    if alive_neighbors == 2 or alive_neighbors == 3:
                        new_cells[r][c] = True
                    else:
                        died+=1
                else:
                    if alive_neighbors == 3:
                        new_cells[r][c] = True
                        born+=1

        changed = new_cells != self.cells
        self.cells = new_cells
        return changed, born, died


    def count_alive_neighbors(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r = row + dr
                c = col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols and self.cells[r][c]:
                    count += 1
        return count


board = Grid(ROWS, COLS, CELL_SIZE)
running = True
paused = True
generation = 0
logger = Observer()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            board.toggle_cell_at_pixel(x, y)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_r:
                new_cells = []
                for row in range(ROWS):
                    row_list = []
                    for col in range(COLS):
                        row_list.append(False)
                    new_cells.append(row_list)
                board.cells = new_cells
            elif event.key == pygame.K_1:
                Factory.create_glider(board, 5, 5)
            elif event.key == pygame.K_2:
                Factory.create_blinker(board, 5,5)
            elif event.key == pygame.K_3:
                Factory.create_pulsar(board, 10,10)
            elif event.key == pygame.K_4:
                Factory.create_gosper_glider_gun(board, 5,5)
            

    if not paused:
        changed, born, died = board.next_generation()

        if changed:
            generation += 1

            logger.FileLogger("Поколение: " + str(generation))
            logger.StatsLogger(generation, born, died)


    board.draw_grid()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
