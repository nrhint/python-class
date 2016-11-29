import turtle
import time

t = turtle
t.Pen()

def octogon():
    for x in range(8):
        t.forward(50)
        t.right(45)
def filledOctogon():
    t.begin_fill()
    for x in range(8):
        t.forward(50)
        t.right(45)
    t.end_fill()

octogon()
time.sleep(1)
t.reset()
filledOctogon()
