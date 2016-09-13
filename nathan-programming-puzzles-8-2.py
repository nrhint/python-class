from time import sleep
import turtle

a = turtle.Pen()
b = turtle.Pen()
c = turtle.Pen()
d = turtle.Pen()

a.speed(1)
b.speed(1)
c.speed(1)
d.speed(1)

a.forward(140)
b.forward(140)
c.forward(150)
d.forward(150)
#first
a.left(90)
b.right(90)
c.left(90)
d.right(90)
#first turn
a.forward(50)
b.forward(50)
c.forward(25)
d.forward(25)
#last turn
a.right(90)
b.left(90)
c.right(90)
d.left(90)
#last
a.forward(70)
b.forward(70)
c.forward(50)
d.forward(50)
sleep(5)
