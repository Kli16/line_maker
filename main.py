from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

display(screen)
save_extension(screen, 'img.png')

draw_line (0,0,400, 200, screen, color)