import pygame
import random


cell_size = [10, 20]

# Proportions, colors, etc.
s_var = {
    # Main window proportions
    "width" : 800,
    "height" : 600,
    "title_size" : 30,
    "title_font" : "impact",
    "title_text" : """Conway's Game Of Life""",
    "title_x" : 20,
    "title_y" : 10,
    
    # Interface proportions
    "big_button_size_x" : 150,
    "big_button_size_y" : 50,
    "small_button_size_x" : 70,
    "small_button_size_y" : 50,

    "start_button_pos_x" : 20,
    "start_button_pos_y" : 50,

    # Game window proportions
    "g_width" : 760,
    "g_height" : 460,
    "g_x" : 20,
    "g_y" : 120,
    "g_border" : 3,
    "cell_size" : 10,
    "cell_border" : 1,

    "fps" : 60,
    "header_font" : "yugothic",
    "header1_size" : 30,
    "header2_size" : 17,

    # Theme window proportions
    "t_w" : 105,
    "t_h" : 30,
    "t_txt" : 15,
    "t_space" : 13,

    # Info window proportions
    "i_w" : 780,
    "i_h" : 500,
    "i_x" : 10,
    "i_y" : 50,
    "i_close_x" : 760,
    "i_close_y" : 10,
    "i_close_w" : 30,
    "i_close_h" : 20,
    "i_close_font_size" : 20,

    "i_font" : "arial",
    "i_font_size" : 15,
    "i_text_wrap" : 42,
    "i_text_x_margin" : 20,
    "i_text_y_margin" : 20,

    # Footnote
    "footnote" : 
"""This program was made by Amanda Spellen as the final project for CS50x, December 2021""",

    # Colors
    # White
    "white" : (255, 255, 255),
    "white1" : (240, 240, 240),
    "white2" : (230, 230, 230),
    "white3" : (220, 220, 220),
    "white4" : (210, 210, 210),
    # Black
    "black" : (0, 0, 0),
    "black1" : (10, 10, 10),
    "black2" : (20, 20, 20),
    "black3" : (30, 30, 30),
    "black4" : (40, 40, 40),
    # Gray
    "gray" : (125, 125, 125),
    "l_gray1" : (200, 200, 200),
    "l_gray2" : (180, 180, 180),
    "l_gray3" : (160, 160, 160),
    "l_gray4" : (140, 140, 140),
    "d_gray1" : (50, 50, 50),
    "d_gray2" : (70, 70, 70),
    "d_gray3" : (90, 90, 90),
    "d_gray4" : (110, 110, 110)
}



# Info headers
i_h_list = ["What is The Game of Life?", "Rules", "John Conway"]

# Info text
# "What is Life?"
i_t1 = [
"""The Game of Life, also known simply as 
Life, is a cellular automaton consisting of a 
regular grid of cells - each in one of a finite number 
of states, such as on and off -, devised by the 
British mathematician John Horton Conway in 1970. 
It is a zero-player game, meaning that its 
evolution is determined by its initial state, 
requiring no further input."""
]

# "Rules"
i_t2 = [
"""The cells act acording the following rules:""",
""" - Any live cell with fewer than two live neighbours dies, 
as if by underpopulation.""",
""" - Any live cell with two or three live neighbours lives on 
to the next generation.""",
""" - Any live cell with more than three live neighbours dies, 
as if by overpopulation.""",
""" - Any dead cell with exactly three live neighbours becomes 
a live cell, as if by reproduction."""
]

# "John Conway"
i_t3 = [
"""John Horton Conway FRS (26/12/1937 – 11/04/2020) was an 
English mathematician active in the theory of finite groups, 
knot theory, number theory, combinatorial game theory and coding 
theory. He also made contributions to many branches of 
recreational mathematics, most notably the invention of the Game 
of Life.""",
"""Conway's invention of the Game of Life was notable for being 
one of the early examples of a cellular automaton. His initial 
experiments in that field were done with pen and paper, long 
before personal computers existed.""",
"""Since the game was introduced by Martin Gardner in Scientific 
American in 1970, it has spawned hundreds of, web sites, articles, 
and computer programs - like this one."""
]

# Paragraph keys
i_t_key = ["p.1", "p.2", "p.3", "p.4", "p.5", "p.6"]

# Paragraph list
i_t_list = [i_t1, i_t2, i_t3]


# Themes
# Key list
key = [
    "name",
    "window",
    "game_window",
    "border",
    "dead_cell",
    "live_cell",
    "light_button",
    "dark_button",
    "header_font",
    "color",
    "color1",
    "random"
]

# Mono theme - Standard
mono = [
    "mono",
    s_var["black2"],
    s_var["d_gray2"],
    s_var["l_gray4"],
    s_var["d_gray1"],
    s_var["white4"],
    s_var["white4"],
    s_var["l_gray4"],
    s_var["black2"],
    s_var["gray"],
    s_var["l_gray1"],
    False
]

# Cinnabar theme - Red
cinnabar = [
    "cinnabar",
    (99, 25, 17),
    (115, 57, 50),
    (138, 106, 102),
    (51, 39, 37),
    (161, 137, 133),
    (148, 95, 86),
    (77, 58, 54),
    (161, 137, 133),
    (161, 137, 133),
    (176, 128, 120),
    False
]

# Spessartine theme - Orange
spessartine = [
    "spessartine",
    (232, 187, 121),
    (201, 132, 54),
    (168, 139, 82),
    (87, 48, 10),
    (240, 150, 34),
    (196, 132, 49),
    (166, 97, 28),
    (115, 51, 9),
    (240, 150, 34),
    (209, 150, 40),
    False
]

# Fool's Gold theme - Gold
foolsgold = [
    "fool's gold",
    (156, 124, 58),
    (191, 158, 77),
    (191, 174, 132),
    (128, 107, 57),
    (191, 174, 132),
    (222, 171, 62),
    (143, 109, 39),
    (51, 44, 28),
    (191, 174, 132),
    (194, 170, 110),
    False
]

# Desert Spice - Yellow
dunespice = [
    "dune spice",
    (227, 207, 125),
    (181, 163, 87),
    (120, 56, 19),
    (153, 129, 73),
    (138, 57, 17),
    (166, 79, 28),
    (120, 56, 19),
    (212, 198, 144),
    (196, 113, 49),
    (232, 144, 77),
    False
]

# Meadow theme - Lime
meadow = [
    "meadow",
    (151, 168, 99),
    (161, 179, 111),
    (129, 150, 114),
    (95, 122, 81),
    (141, 184, 144),
    (116, 156, 76),
    (66, 110, 47),
    (191, 209, 142),
    (141, 184, 144),
    (109, 158, 113),
    False
]

# Terrarium theme - Green
terrarium = [
    "terrarium",
    (18, 61, 18),
    (49, 125, 58),
    (95, 156, 95),
    (35, 92, 42),
    (95, 156, 95),
    (26, 46, 27),
    (17, 36, 18),
    (103, 143, 103),
    (29, 97, 29),
    (20, 84, 20),
    False
]

# Dioptase theme - Dark Teal
dioptase = [
    "dioptase",
    (5, 26, 16),
    (13, 69, 42),
    (116, 153, 137),
    (10, 46, 30),
    (116, 153, 137),
    (100, 161, 134),
    (91, 189, 145),
    (5, 26, 16),
    (116, 153, 137),
    (37, 143, 96),
    False
]

# Copper Sulfate theme - Cyan
coppersulfate = [
    "copper sulfate",
    (66, 132, 150),
    (42, 97, 112),
    (212, 151, 102),
    (47, 104, 120),
    (212, 151, 102),
    (148, 85, 34),
    (120, 73, 36),
    (118, 155, 166),
    (118, 155, 166),
    (90, 129, 140),
    False
]

# Jupiter Clouds theme - Light Blue
jupiterclouds = [
    "jupiter clouds",
    (90, 110, 145),
    (82, 101, 135),
    (133, 138, 166),
    (50, 55, 82),
    (133, 138, 166),
    (128, 152, 196),
    (107, 137, 194),
    (10, 19, 36),
    (133, 138, 166),
    (83, 88, 112),
    False
]

# Dusk theme - Deep Blue
dusk = [
    "dusk",
    (7, 15, 46),
    (11, 22, 69),
    (3, 6, 15),
    (18, 36, 110),
    (3, 6, 15),
    (58, 76, 148),
    (38, 53, 112),
    (3, 7, 20),
    (78, 83, 102),
    (55, 60, 79),
    False
]

# KMnO4 theme - Violet
kmno4 = [
    "KMnO4",
    (104, 69, 128),
    (77, 52, 94),
    (78, 24, 115),
    (25, 9, 36),
    (78, 24, 115),
    (160, 123, 186),
    (27, 10, 38),
    (78, 24, 115),
    (78, 24, 115),
    (78, 24, 115),
    False
]

# Belt Of Venus theme - Lavender
beltofvenus = [
    "belt of venus",
    (166, 116, 181),
    (133, 86, 148),
    (81, 39, 82),
    (100, 87, 148),
    (81, 39, 82),
    (188, 153, 199),
    (44, 35, 74),
    (122, 61, 156),
    (81, 39, 82),
    (81, 39, 82),
    False
]

# Plasma Globe - Magenta
plasmaglobe = [
    "plasma globe",
    (61, 26, 61),
    (115, 62, 115),
    (113, 62, 181),
    (19, 10, 31),
    (113, 62, 181),
    (125, 41, 125),
    (82, 24, 82),
    (179, 136, 179),
    (113, 62, 181),
    (113, 62, 181),
    False
]

# Lightining Sprite theme - Pink
lightningsprite = [
    "lightning sprite",
    (143, 43, 56),
    (143, 43, 68),
    (191, 136, 163),
    (59, 21, 29),
    (191, 136, 163),
    (194, 95, 143),
    (189, 77, 131),
    (59, 21, 29),
    (191, 136, 163),
    (191, 136, 163),
    False
]

# Rose Quartz theme - Light Pink
rosequartz = [
    "rose quartz",
    (207, 138, 153),
    (173, 116, 129),
    (140, 84, 96),
    (173, 137, 145),
    (140, 84, 96),
    (214, 171, 181),
    (207, 120, 139),
    (140, 84, 96),
    (140, 84, 96),
    (140, 84, 96),
    False
]

# Morpho theme - Brown
morpho = [
    "morpho",
    (69, 55, 45),
    (84, 64, 49),
    (23, 29, 43),
    (84, 75, 68),
    (23, 29, 43),
    (97, 134, 212),
    (63, 104, 191),
    (23, 29, 43),
    (23, 29, 43),
    (23, 29, 43),
    False
]

# Stoneware theme - Gray
stoneware = [
    "stoneware",
    (153, 142, 129),
    (176, 163, 150),
    (94, 90, 86),
    (176, 163, 150),
    (94, 90, 86),
    (212, 198, 184),
    (105, 98, 91),
    (56, 54, 52),
    (94, 90, 86),
    (94, 90, 86),
    False
]

# Jasmin theme - White
jasmin = [
    "jasmin",
    (227, 227, 211),
    (222, 222, 197),
    (186, 186, 166),
    (207, 207, 192),
    (186, 186, 166),
    (186, 186, 143),
    (186, 186, 149),
    (237, 237, 225),
    (186, 186, 166),
    (186, 186, 166),
    False
]

# Corvidae theme - Black
corvidae = [
    "corvidae",
    (9, 10, 10),
    (23, 26, 26),
    (37, 43, 41),
    (16, 20, 19),
    (37, 43, 41),
    (39, 54, 54),
    (31, 43, 43),
    (98, 112, 112),
    (37, 43, 41),
    (37, 43, 41),
    False
]

# Theme list
theme_list = [
    mono, stoneware, corvidae, jasmin, cinnabar, morpho, coppersulfate, 
    dunespice, dioptase, dusk, foolsgold, 
    jupiterclouds, kmno4, lightningsprite, meadow, 
    plasmaglobe, rosequartz, spessartine, beltofvenus, terrarium
]
