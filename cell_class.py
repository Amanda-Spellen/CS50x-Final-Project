import pygame
from settings import s_var

# Cell class
class Cell:
    def __init__(self, surface, grid_x, grid_y, c_s):
        global c_size
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        c_size = c_s

        self.image = pygame.Surface((c_size, c_size))
        self.rect = self.image.get_rect()
        self.neighbours = []
        self.alive_neighbours = 0


    # Update cell
    def update(self):
        self.rect.topleft = (self.grid_x*c_size, self.grid_y*c_size)
        

    # Draw cells into the game window grid
    def draw(self, theme):
        in_grid = c_size - (s_var["cell_border"])

        # Draw living cells
        if self.alive:
            self.image.fill((theme["live_cell"]))
        
        # Draw dead cells
        else:

            # Draw borders
            self.image.fill((theme["border"]))

            # Draw fillinng
            color = theme["dead_cell"]
            pygame.draw.rect(self.image, color, 
                (s_var["cell_border"], s_var["cell_border"], 
                in_grid, in_grid))
        
        self.surface.blit(self.image, (self.grid_x*c_size, self.grid_y*c_size))


    # Get living neighbours
    def live_neighbours(self):
        alive_n = 0
        for n in self.neighbours:
            if n.alive:
                alive_n += 1 

        self.alive_neighbours = alive_n
    

    # Get cell's neighbours
    def get_neighbours(self, grid):
        cols = s_var["g_width"] // c_size
        rows = s_var["g_height"] // c_size
        neighbour_list = [[1, 1], [-1, -1], [-1, 1], [1, -1], [0, 1], 
            [1, 0], [0, -1], [-1, 0]]

        for neighbour in neighbour_list:
            neighbour[0] += self.grid_x
            neighbour[1] += self.grid_y
        
        # Manage cases of margin cells
        for neighbour in neighbour_list:
            if neighbour[0] < 0:
                neighbour[0] += 1
            if neighbour[0] > cols - 1:
                neighbour[0] -= 1
            if neighbour[1] < 0:
                neighbour[1] += 1
            if neighbour[1] > rows - 1:
                neighbour[1] -= 1
        
        # Add to list
        for neighbour in neighbour_list:
            try:
                self.neighbours.append(grid[neighbour[1]][neighbour[0]])
            
            # Print errors
            except:
                print("missing neighbour on position:", neighbour)
