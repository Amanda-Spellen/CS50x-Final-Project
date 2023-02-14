import pygame
import textwrap
from button import Button
from settings import s_var, i_t_list, i_t_key, i_h_list, key, theme_list, cell_size

vec = pygame.math.Vector2

# Theme window class
class ThemeWindow:
    def __init__(self, screen, posx, posy, size_x):
        self.screen = screen
        self.pos = vec(posx, posy)
        self.size_x = size_x[2] - size_x[0] + s_var["small_button_size_x"]
        self.size_y = s_var["g_height"]
        self.size = vec(self.size_x, self.size_y)
        self.area = pygame.Rect(posx, posy, self.size.x, self.size.y)
        self.button_list = []
        self.theme_names = []
        self.t = {}
        self.size_x_list = size_x


    # Draw window
    def draw(self, color):
        pygame.draw.rect(self.screen, color, self.area)


    # Create theme buttons
    def make_buttons(self):
        pos1 = self.pos.x + s_var["t_space"]
        pos2 = self.pos.y + s_var["t_space"]
        for a, theme in enumerate(theme_list):
            self.theme_names.append(theme[0])
            self.button_list.append(Button(self.theme_names[a], self.screen, pos1, 
            pos2, s_var["t_w"], s_var["t_h"], theme[7], self.theme_names[a], s_var["header_font"], 
            s_var["t_txt"], theme[8], self.theme_switching, "setting", theme, light=True, theme_c=theme[6], font_c=theme[8]))

            pos1 += s_var["t_w"] + s_var["t_space"]
            if pos1 > (self.size_x_list[2] + s_var["small_button_size_x"] - s_var["t_space"]):
                pos1 = self.pos.x + s_var["t_space"]
                pos2 += s_var["t_h"] + s_var["t_space"]
        
        return self.button_list
    

    # Switch current theme
    def theme_switching(self, theme):
        for button in self.button_list:
            if button.clicked:
                t = dict(zip(key, theme))
                self.t = t

# Initial theme
t = dict(zip(key, theme_list[0]))

# Initial cell size
cs = cell_size[0]


# Info window class
class InfoWindow:
    def __init__(self, screen):
        self.screen = screen
        self.pos_x = s_var["i_x"]
        self.pos_y = s_var["i_y"]
        self.pos = vec(self.pos_x, self.pos_y)
        self.size_x = s_var["i_w"]
        self.size_y = s_var["i_h"]
        self.size = vec(self.size_x, self.size_y)
        self.area = pygame.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)
    
    
    # Draw window to the screen
    def draw(self, theme):

        # Background filling
        self.screen.fill(theme["window"])

        # Foreground filling
        pygame.draw.rect(self.screen, theme["dead_cell"], self.area)
    

    # Make close button
    def make_buttons(self, theme):
        close_b = Button("close", self.screen, s_var["i_close_x"], 
            s_var["i_close_y"], s_var["i_close_w"], s_var["i_close_h"], 
            theme["light_button"], "x", s_var["header_font"], s_var["i_close_font_size"], 
            theme["header_font"], function=close, state="info")

        return close_b
    

    # Print text to window
    def print_text(self, theme):
        posx = s_var["i_text_x_margin"]
        h_posy = self.pos.y + s_var["i_x"]

        # Initiate fonts
        init_text = pygame.font.SysFont(s_var["i_font"], s_var["i_font_size"]) 
        init_header = pygame.font.SysFont(s_var["header_font"], s_var["header2_size"], bold=True)
        init_title = pygame.font.SysFont(s_var["title_font"], s_var["title_size"])

        # Print title
        title = init_title.render(s_var["title_text"], 1, theme["live_cell"])
        self.screen.blit(title, (s_var["i_x"], s_var["title_y"]))


        # Topics
        for a, topic in enumerate(i_t_list):
            wrapper = textwrap.TextWrapper(width=s_var["i_text_wrap"])
            txt = dict(zip(i_t_key, topic))
            posy = self.pos.y + s_var["i_text_y_margin"] + s_var["header2_size"]
            
            # Header 
            text = init_header.render(i_h_list[a], 1, theme["light_button"]) 
            self.screen.blit(text, (posx, h_posy))

            # Paragraphs
            for a, b in enumerate(txt):
                word_list = wrapper.wrap(text=txt[b])
                
                # Lines
                for a, c in enumerate(word_list):
                    text = init_text.render(c, 1, theme["live_cell"]) 
                    self.screen.blit(text, (posx, posy))

                    # Jump to next line
                    posy += s_var["i_text_y_margin"]
            
            # Jump to next column
            posx += ((s_var["i_text_wrap"]) * 5.65) + s_var["i_text_x_margin"]

        # Footnote
        footnote = init_text.render(s_var["footnote"], 1, theme["light_button"]) 
        f_posx = s_var["i_x"]
        f_posy = s_var["height"] - s_var["i_font_size"] - s_var["i_text_y_margin"]

        self.screen.blit(footnote, (f_posx, f_posy))


# Close button function
def close():
    return False
