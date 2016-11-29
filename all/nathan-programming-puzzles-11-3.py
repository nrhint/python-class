import turtle

t = turtle
t.Pen()

def drawStar(size, points):
    if points % 2 == 0:
        ang = (360/points)*1
        ang2 = (360/points)*2
        for x in range(points):
            t.forward(size)
            t.right(ang)
            t.forward(size)
            t.left(ang2)
    else:
        ang = (360/points)*2
        for x in range(points):
            t.forward(size)
            t.right(ang)

drawStar(50, 10)
