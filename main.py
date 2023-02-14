import pygame
import sys
from themes import ThemeWindow, InfoWindow, t, cs
from settings import s_var
from game_window import Game_window
from button import Button

# Setting functions
# Get events
def get_events():
    global running
    for event in pygame.event.get():

        # Exit program
        if event.type == pygame.QUIT:
            running = False

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Clicking cells
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            
            # Clicking buttons
            else:
                for button in buttons:
                    button.click(state)


# Update functions
def update():

    # Update game window
    game_window.update()

    # Update buttons
    for a, button in enumerate(buttons):
        button.update(mouse_pos, state)


# Draw objects to the screen
def draw():

    # Draw program window
    window.fill(theme["window"])

    # Print title
    title = init_title.render(s_var["title_text"], 1, theme["live_cell"])
    window.blit(title, (s_var["title_x"], s_var["title_y"]))

    # Draw buttons
    for a, button in enumerate(buttons):
        button.draw(theme["light_button"], theme["dark_button"], theme)
    
    # Draw game window
    game_window.draw(theme)
    

# Running functions
# Get events
def run_get_events():
    global running
    for event in pygame.event.get():
        
        # Exit program
        if event.type == pygame.QUIT:
            running = False
        
        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Clicking cells
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            
            # Clicking buttons
            else:
                for button in buttons:
                    button.click(state)


# Update functions
def run_update():

    # Update game window
    game_window.update()

    # Update buttons
    for a, button in enumerate(buttons):
        button.update(mouse_pos, state)
    
    # Apply the rules of the cellular automaton
    if frames % (s_var["fps"]//10) == 0:
        game_window.game_rules()


# Draw objects to the screen
def run_draw():

    # Draw program window
    window.fill(theme["window"])

    # Print title
    title = init_title.render(s_var["title_text"], 1, theme["live_cell"])
    window.blit(title, (s_var["title_x"], s_var["title_y"]))

    # Draw buttons
    for a, button in enumerate(buttons):
        button.draw(theme["light_button"], theme["dark_button"], theme)
    
    # Draw game window
    game_window.draw(theme)


# Stopping functions
# Get events
def stop_get_events():
    global running
    for event in pygame.event.get():

        # Exit program
        if event.type == pygame.QUIT:
            running = False
        
        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Clicking cells
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            
            # Clicking buttons
            else:
                for button in buttons:
                    button.click(state)


# Update functions
def stop_update():

    # Update game window
    game_window.update()

    # Update buttons
    for a, button in enumerate(buttons):
        button.update(mouse_pos, state)


# Draw objects to the screen
def stop_draw():

    # Draw window
    window.fill(theme["window"])
    
    # Print title
    title = init_title.render(s_var["title_text"], 1, theme["live_cell"])
    window.blit(title, (s_var["title_x"], s_var["title_y"]))

    # Draw buttons
    for a, button in enumerate(buttons):
        button.draw(theme["light_button"], theme["dark_button"], theme)
    
    # Draw game window
    game_window.draw(theme)


# Check if mouse is on the game window
def mouse_on_grid(pos):
    if pos[0] > s_var["g_x"] and pos[0] < s_var["width"] - s_var["g_x"]:
        if pos[1] > s_var["g_y"] and pos[1] < s_var["g_y"] + s_var["g_height"]:
            return True
    return False


# Click cell
def click_cell(pos):

    # Get overall area
    grid_pos = [pos[0] - s_var["g_x"], pos[1] - s_var["g_y"]]
    grid_pos[0] = grid_pos[0] // c_s
    grid_pos[1] = grid_pos[1] // c_s
    current_cell = game_window.grid[grid_pos[1]][grid_pos[0]]

    # Change state
    if current_cell.alive:
        current_cell.alive = False
    else:
        current_cell.alive = True


# Create buttons
def make_buttons():
    global theme, button_pos
    buttons = []
    big_names = ("Run", "Stop", "Clear")
    big_functions = [run, stop, clear]
    big_states = ("setting", "running", "stopping")
    big_pos = 0
    small_names = ("Info", "Random", "Themes")
    small_functions = (info, random, themes)
    small_states = ("setting", "setting", "setting")
    button_pos = []
    
    # Big buttons - Run, Stop, Clear
    for a in range(len(big_names)):
        pos1 = a * (s_var["start_button_pos_x"] + s_var["big_button_size_x"])
        big_pos = s_var["start_button_pos_x"] + pos1
        buttons.append(Button(big_names[a], window, big_pos, s_var["start_button_pos_y"], 
            s_var["big_button_size_x"], s_var["big_button_size_y"], theme["light_button"], 
            big_names[a], s_var["header_font"], s_var["header1_size"], theme["header_font"], 
            big_functions[a], big_states[a], light=True))
    
    # Small buttons - Info, Random, Themes
    for b in range(len(small_names)):
        pos1 = b * (s_var["start_button_pos_x"] + s_var["small_button_size_x"])
        pos2 = s_var["g_border"] - s_var["cell_border"]
        pos = s_var["start_button_pos_x"] + pos1 + big_pos + s_var["big_button_size_x"] + pos2
        button_pos.append(pos)
        buttons.append(Button(small_names[b], window, pos, s_var["start_button_pos_y"], 
            s_var["small_button_size_x"], s_var["small_button_size_y"], theme["dark_button"], 
            small_names[b], s_var["header_font"], s_var["header2_size"], theme["header_font"], 
            small_functions[b], small_states[b]))

    return buttons


# Change state during run
def run():
    global state
    state = "running"
    state_list.append(state)


# Change state during stop
def stop():
    global state
    state = "stopping"
    state_list.append(state)


# Change state during clear
def clear():
    global state
    state = "setting"

    # Reset grid
    game_window.reset_grid()

    state_list.append(state)


# Open Info window
def info():
    global state
    last_state = state_list[len(state_list)-1]
    if buttons[3].clicked:
        info_window.draw(theme)
        info_window.print_text(theme)
        if state == "info":
            info_buttons.update(mouse_pos, state)
            info_buttons.draw(theme["light_button"], theme["dark_button"], theme)
            info_buttons.click(state)
        state = "info"

        # Close Info window
        if last_state == "setting":
            if info_buttons.clicked:
                buttons[3].clicked = info_buttons.click(state)
                state = "setting"
        
        # Close info window
        elif last_state == "stopping":
            if info_buttons.clicked:
                buttons[3].clicked = info_buttons.click(state)
                state = "stopping"
        
        
# Create random cell generation
def random():
    game_window.random_gen()


# Open Themes window
def themes():
    if buttons[5].clicked:
        theme_window.draw(theme["game_window"])
        for b in theme_buttons:
            b.click(state)
            b.update(mouse_pos, state)
            b.draw(theme["light_button"], theme["dark_button"], theme)
        

# Change current theme
def change_theme():
    global theme
    if theme_window.t != {}:
        theme = theme_window.t
    else:
        theme = t


# Main
def main():
    global window, game_window, clock, running, buttons, mouse_pos, state
    global theme_window, theme_buttons, theme, info_window, info_buttons
    global state_list, c_s, frames, title, init_title

    pygame.init()
    
    # Set title bar icon
    #icon = pygame.image.load(r"C:\Users\AmandaSpellen\Documents\CS\Projects\conwaylife\icon2.png") 
    #pygame.display.set_icon(icon)

    # Set title bar title
    pygame.display.set_caption("Conway's Game Of Life")

    theme = t
    c_s = cs
    rows = s_var["g_width"] // c_s
    cols = s_var["g_height"] // c_s

    # Initiate window
    window = pygame.display.set_mode((s_var["width"], s_var["height"]))

    # Initiate title
    init_title = pygame.font.SysFont(s_var["title_font"], s_var["title_size"])
    title = init_title.render(s_var["title_text"], 1, theme["live_cell"])

    # Initiate game window
    game_window = Game_window(window, s_var["g_x"], s_var["g_y"], 
        s_var["g_width"], s_var["g_height"], rows, cols, theme, c_s)

    clock = pygame.time.Clock()
    frames = 0
    
    buttons = make_buttons()
    state = "setting"
    state_list = []
    state_list.append(state)
    
    t_y = buttons[3].pos.y + s_var["small_button_size_y"] + s_var["t_space"]
    theme_window = ThemeWindow(window, buttons[3].pos.x, t_y, button_pos)
    theme_buttons = theme_window.make_buttons()

    info_window = InfoWindow(window)
    info_buttons = info_window.make_buttons(theme)

    # Run program
    running = True
    while running:
        frames += 1

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        change_theme()

        # Setting game
        if state == "setting":
            get_events()
            update()
            draw()
            themes()
            info()
        
        # Running game
        if state == "running":
            run_get_events()
            run_update()
            run_draw()
            themes()
        
        # Stopped game
        if state == "stopping":
            stop_get_events()
            stop_update()
            stop_draw()
            themes()
            info()

        # Info window state
        if state == "info":
            get_events()
            update()
            draw()
            info()
        
        pygame.display.update()
        clock.tick(s_var["fps"])
    
if __name__ == "__main__":
    main()

pygame.quit()
sys.exit()
