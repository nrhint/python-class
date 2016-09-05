import turtle
from time import sleep

t = turtle
t.pen()

def rectangle(size):
    t.reset()
    for x in range(2):
        t.forward(size + (size/2))
        t.left(90)
        t.forward(size)
        t.left(90)
def triangle(size):
    t.reset()
    for x in range(3):
        t.forward(size)
        t.left(120)
def rect_without_corners(sizea):
    t.reset()
    size = sizea/8
    for x in range(2):
        t.up()
        t.forward(size*2)
        t.down()
        t.forward(size*4)
        t.up()
        t.forward(size*2)
        t.left(90)
        t.forward(size)
        t.down()
        t.forward(size*2)
        t.up()
        t.forward(size)
        t.left(90)

rectangle(200)
sleep(1)
triangle(200)
sleep(1)
rect_without_corners(200)
