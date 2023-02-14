import pygame
import copy
import random
from settings import s_var
from cell_class import Cell

vec = pygame.math.Vector2

# Game window class
class Game_window:
    def __init__(self, screen, x, y, g_width, g_height, rows, cols, theme, c_s):
        global b_w, b_h, border_rect

        self.screen = screen
        self.pos = vec(x, y)
        self.width, self.height = g_width, g_height
        self.window = pygame.Surface((self.width, self.height))
        self.rect = self.window.get_rect()
        b_w, b_h = g_width + s_var["g_border"], g_height + s_var["g_border"]
        self.border = pygame.Rect((x - s_var["g_border"]//2, 
            y - s_var["g_border"]//2), (b_w, b_h))

        self.rows = rows
        self.cols = cols
        self.c_s = c_s
        self.grid = [[Cell(self.window, x, y, c_s) for x in range(self.rows)] for y in range(self.cols)]

        # Get cells' neighbours
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)
        self.theme = theme


    # Update game window
    def update(self):
        self.rect.topleft = self.pos

        # Update cells
        for row in self.grid:
            for cell in row:
                cell.update()


    # Draw objects to the screen
    def draw(self, theme):

        # Draw border
        pygame.draw.rect(self.screen, theme["border"], self.border)

        # Draw main filling
        self.window.fill(theme["game_window"])
        
        # Draw cells
        for row in self.grid:
            for cell in row:
                cell.draw(theme)
        
        self.screen.blit(self.window, (self.pos.x, self.pos.y))
    

    # Clean game window
    def reset_grid(self):

        # Redraw grid
        self.grid = [[Cell(self.window, x, y, self.c_s) for x in range(self.rows)] for y in range(self.cols)]
        
        # Get cells' neighbours
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)
    

    # Apply The Game Of Life's rules
    def game_rules(self):
        new_grid = copy.copy(self.grid)

        # Get living neighbours
        for row in self.grid:
            for cell in row:
                cell.live_neighbours()

        # Apply rules
        for y, row in enumerate(new_grid):
            for x, cell in enumerate(row):
                if cell.alive:

                    # "Any live cell with two or three live neighbours lives on to the next generation"
                    if cell.alive_neighbours == 2 or cell.alive_neighbours == 3:
                        new_grid[y][x].alive = True
                    
                    # "Any live cell with fewer than two or more than three live neighbours dies, 
                    # as if by underpopulation or overpopulation, respectively"
                    elif cell.alive_neighbours < 2 or cell.alive_neighbours > 3:
                        new_grid[y][x].alive = False
                    
                    else:
                        new_grid[y][x].alive = False
                
                elif not cell.alive:

                    # "Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction"
                    if cell.alive_neighbours == 3:
                        new_grid[y][x].alive = True

                    else:
                        new_grid[y][x].alive = False

        self.grid = new_grid


    # Create random generation
    def random_gen(self):
        for row in self.grid:
            for cell in row:
                cell.alive = random.choice([True, False, False, False, False])
    