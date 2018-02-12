from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y
    B = x - x1
    #OcTanT I:
    if (A > 0 and abs(B) > A):
        d = 2 * A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A
    #OcTanT II:
    if (A > 0 and abs(B) < A):
        d = A + 2 * B
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B
    #OcTanT VIII:
    if (A < 0 and abs(B) < abs(A)):
        d = 2 * A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y += 1
                d -= 2 * B
            x += 1
            d += 2 * A
    #OcTanT VII:
    if (A < 0 and abs(A) > abs(B)):
        d = 2 * B - A
        while (y <= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d -= 2 * A
            y += 1
            d += 2 * B
