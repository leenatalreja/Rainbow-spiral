import turtle
from turtle import *

turtle.title("Rainbow spiral")
speed(18)
bgcolor("black")
r, g, p = 255, 0, 0

for i in range(255*2):
    colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        p+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        p-=3
    fd(50 + i)
    rt(91)
    pencolor(r,g,p)

done()
