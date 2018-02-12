from display import *
from draw import *

screen = new_screen()

#angery eyebrows
color = [ 205, 86, 57 ]
draw_line (100,400,230, 300, screen, color)
draw_line (270,300,400, 400, screen, color)
#angery eyes
color = [ 15, 86, 209 ]
draw_line (150,270,200, 270, screen, color) #SLOPE 0
draw_line (320,270,370, 270, screen, color) #SLOPE 0
#angery nose
color = [ 0, 153, 0]
draw_line (250,200,250, 250, screen, color) #SLOPE UNDEFINED
#angery mouth
color = [ 205, 0, 0 ]
draw_line (150,120, 380, 120, screen, color)
draw_line (120,90, 150, 120, screen, color) #SLOPE 1
draw_line (380,120, 410, 90, screen, color) #SLOPE -1
display(screen)
save_extension(screen, 'img.png')
