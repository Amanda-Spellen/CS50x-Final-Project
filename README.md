# CONWAY'S GAME OF LIFE
#### Video Demo:  <https://youtu.be/4W88oMphXxo>
#### Description:

##### What is my project?
It is a Python program that recreates the basic procedures of a cellular automaton.

Its cells follow the simple rules of:
 - _if a live cell has less than 2 or more than 3 live neighbours, it dies._
 - _if a live cell has 2 or 3 live neighbours, it lives._
 - _if a dead cell has exactly 3 neighbours, it lives._

##### The Files:

##### `main.py:`
It is the principal file, and it applies functions and classes from the remaining files.
It initiates the program's window, its title and icon in the title bar, buttons, game window, and info and theme windows.
It runs the overall program.


##### `game_window.py:`
It is responsible for defining the game window’s class. 
Includes traits such as `grid`, `position`, and `size`. These last two proprieties are necessary for drawing and updating the game window in `main.py` - `draw(self, theme)` and `update(self)`.

It applies cells’ functions such as detecting neighbours (`cell.get_neighbours(self.grid)`), updating (`cell.update()`), and drawing (`cell.draw(theme)`) through a series of loops relying on its grid propriety.

This file is in charge of resetting the grid (`reset_grid()`) when the _"Clear"_ button is clicked - it simply creates a brand new grid that overwrites the old one -, as well as applying the necessary cellular automaton rules (`game_rules()`) when the _"Run"_ button is pressed, working loops with a new grid that will soon replace the former.

Lastly, `game_window.py` creates random generations with a 20% chance of cells being alive (`random_gen()`), based on the `random` built-in library.


##### `cell_class.py:`
As a class, it defines an individual cell.
Has proprieties for its grid position, list of neighbours, and the number of living neighbours.

The function to draw (`draw(theme)`) takes the cases of live and dead cells, applying the colors indicated by the current theme variable.

In `live_neighbours()` there’s a dependency on `get_neighbours(grid)` to deliver a list of neighbours so it can compute the amount of living neighbouring cells, while the list is created by iterations through a sequence of standard positions summed by the cell’s grid coordinates, by `get_neighbours(grid)`.


##### `button.py:`
All buttons in the program are defined by this file’s class (`Button`).

It has a lot of proprieties, which give freedom to create buttons with a wide variety of sizes and colors. The most interesting ones are `self.function`, `self.state` and `self.argument`, that automatically apply a given function depending on the given state (`click(game_state)`).

Other functions are `update(pos, game_state=””)`, enabling hovering and locking, and `draw(l_color, d_color, theme)`, applying tones for normal, hovered and locked states.
In `show_text(theme)`, the text on the button is centered and printed.

The colors for hovering and locking are defined in `change_color(color)`, each assuming a value derived from the regular tone, which goes through a series of loops that work quite _mysteriously_. The basic idea is to darken or lighten depending on the individual values and at the same time avoid errors caused by negative numbers.

In `hovering(pos)` is checked if the button is hovered by the mouse.


##### `themes.py:`
This file has two classes, where their only relation is both being applied to small buttons that have no impact on the functioning of the actual game. In addition, `main.py` - and consequently all remaining files -, references the initial values for themes (`t`) and cell size (`cs`).

For `ThemeWindow`, in charge of the _"Theme"_ switching, a simple rectangle area is drawn and filled with buttons from `make_buttons()`, which performs a loop to dynamically generate a button for each theme from `settings.py`.
And ending this class there is `theme_switching(theme)`, which changes the theme of the program to one of the hovered theme buttons by mapping a key list to a colors list in a dict that will be referenced by main.py. Curiously, the hovering feature was not firstly predicted, but somehow it benefited the showcase of themes, yet, at the same time, damaged efficiency -  a fix for this has not been found yet.

In `InfoWindow`, related to the _"Info"_ tab, the whole screen is filled, so a _"Close"_ button was added to allow convenient traffic between functions - but it too suffers from the hovering issue.
To print all the information on the tab, the function `print_text(theme)` adds headers and loops through wrapped paragraphs to organize each topic in neat columns. 
Lastly, out of any class, there is the function to close the _"Info"_ window, `close()`, that simply returns False.


##### `settings.py:`
This file is the library of values that are referenced all throughout the other files. It contains a dict and multiple lists. The dict (`s_var`) keeps almost all proportions, regular colors and miscellaneus values. 
The first lists after `s_var` contain the headers and texts for the _"Info"_ tab, followed by contents for _"Themes"_, which start with the `key` list, proceeded by 20 lists of colors, and finished by a list of these lists.


##### Designing choices:
To make this program, I’ve watched a really helpful tutorial by [A Plus Coding on YouTube](https://www.youtube.com/playlist?list=PLryDJVmh-ww1OZnkZkzlaewDrhHy2Rli2), but tried to keep a balance between efficiency and personality. I tried to make my version of the code as dynamic as possible, so anyone would only need to change one propriety in one file - `settings.py` - and still have a pleasant interface.

For the window, I wondered what size would be best: not too big and inconvenient, nor too small and unpleasant. 
For the grid and cells, there were various initial ideas I was planning to add, like randomly changing colors inside a small range, being able to see a change of color when hovering dead cells, zooming in and out, and more. But I still needed to finish it first, so I had to control myself.

For _"Info"_, I wanted to give a small context to the “player”, something quick but still comprehensive. I wish I could’ve added a gallery of insertable patterns of live cells, things like pulsars and gliders.

For the themes, I decided to keep a relatively small range of colors for each, but still have the overall wide reach of hues, adding at least one theme focused on one of the primary and secondary colors. I had a constant worry with the values, making sure none were too alike and difficult to see. To be honest, the names of the themes are purposefully unusual, because I wanted to make people wonder, search and learn something new, even if it’s not related to the automaton itself.
