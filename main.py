from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
draw_line (0,0,500, 200, screen, color)
draw_line (0,0,500, 100, screen, color)
draw_line (0,0,200, 500, screen, color)
draw_line (0,0,100, 500, screen, color)
draw_line (0,500,500, 100, screen, color)
#draw_line (0,500, 500, 400, screen, color)
display(screen)
save_extension(screen, 'img.png')
