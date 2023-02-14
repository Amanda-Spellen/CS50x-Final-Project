import pygame

vec = pygame.math.Vector2

# Button class
class Button:
    def __init__(self, name, surface, pos_x, pos_y, size_x, size_y, color, text, 
                font, font_size, font_color, function=0, state='', argument=None, 
                light=False, theme_c=0, font_c=0):
        self.name = name
        self.surface = surface
        self.pos = vec(pos_x, pos_y)
        self.size = vec(size_x, size_y)
        self.color = color
        self.text = text
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.function = function
        self.state = state
        self.arg = argument

        self.area = pygame.Rect((pos_x, pos_y), (self.size.x, self.size.y))
        self.rect = pygame.draw.rect(surface, color, self.area)
        self.rect.topleft = self.pos
        
        self.hover = (125, 125, 125)
        self.locked = (255,255,255)
        
        
        self.hovered = False
        self.show = True
        self.clicked = False
        self.light = light
        self.theme_c = theme_c
        self.font_c = font_c
    

    # Update button
    def update(self, pos, game_state=''):

        # Manage hovering
        if self.hovering(pos):
            self.hovered = True
        else:
            self.hovered = False
        
        # Manage locking
        if self.state == '' or game_state == '' or self.state == game_state:
            self.show = True
        elif self.state == "setting" and game_state == "stopping":
            self.show = True
        else:
            self.show = False


    # Draw button
    def draw(self, l_color, d_color, theme):
        color = ()
        color1 = ()

        # For light colored buttons
        if self.light:

            # Custom color
            if self.theme_c != 0:
                color1 = self.theme_c
            
            # Theme color
            else:
                color1 = theme["light_button"]
                self.color = l_color
        
        # For dark colored buttons
        else:
            # Custom color
            if self.theme_c != 0:
                color1 = self.theme_c

            # Theme color
            else:
                color1 = theme["dark_button"]
                self.color = d_color

        # Get hovering and locking colors
        self.hover, self.locked = self.change_color(color1)

        if self.show:
            if self.hovered:
                color = self.hover
            else:
                color = self.color
        else:
            color = self.locked

        pygame.draw.rect(self.surface, color, self.area)

        # Show text
        if len(self.text) > 0:
            self.show_text(theme)


    # Print text
    def show_text(self, theme):

        # Ininitiate font
        init_font = pygame.font.SysFont(self.font, self.font_size) 

        txt = 0

        # Custom font color
        if self.font_c != 0:
            txt = init_font.render(self.text, 1, self.font_c)

        # Theme font color
        else:
            txt = init_font.render(self.text, 1, theme["header_font"])   

        # Centralize text
        size = txt.get_size()
        x = self.pos.x + (self.size.x - size[0]) / 2
        y = self.pos.y + (self.size.y - size[1]) / 2
        pos = vec(x, y)

        self.surface.blit(txt, pos)
    

    # Generating hovering and locking colors
    def change_color(self, color):

        # Hovering color
        color1 = [0,0,0]

        # Locking color
        color2 = [0,0,0]

        smallest = min(color)
        greatest = max(color)

        for a, c in enumerate(color):
            if c == smallest:
                if smallest < 50:
                    color1[a] = 25
                    color2[a] = 35
                else:
                    color1[a] = c - 50
                    color2[a] = c - 30

            elif c == greatest:
                if greatest > 184:
                    color1[a] = 209
                    color2[a] = 220
                else:
                    color1[a] = c + 50
                    color2[a] = c + 30

            else:
                color1[a] = c
                color2[a] = c

        return color1, color2


    # Detect mouse hovering
    def hovering(self, pos):
        if pos[0] > self.pos.x and pos[0] < self.pos.x + self.size.x:
            if pos[1] > self.pos.y and pos[1] < self.pos.y + self.size.y:
                return True


    # Detect mouse clicking
    def click(self, game_state):
        if self.state == game_state or self.state == "setting" and game_state == "stopping":
            if self.hovered:

                # Apply function
                if self.function != 0:
                    if self.arg != None:
                        self.function(self.arg)
                    else:
                        self.function()
                        
                if self.clicked:
                    self.clicked = False
                else:
                    self.clicked = True
        