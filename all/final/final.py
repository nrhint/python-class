#final assingment

from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width = 1200, height = 200)
run = True

tk.title("Final Assingment")

canvas.pack()
tk.update_idletasks()
tk.update()

def coords(sprite):
    pos = sprite.canvas.coords(sprite.id)
    return pos
class Player:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_polygon((190, 190), (190, 200), (200, 200), (200, 190),  fill = color)
        self.canvas.move(self.id, -190, 0)
        self.canvasWidth = 1200
        self.canvasHeight = 200
        self.x = 1
        self.y = 0
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        #pass
class Plat:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.id = self.canvas.create_polygon((x,y), (x+25, y), (x+25, y+3), (x, y+3),  fill = 'green')
        #self.canvas.move(self.id, 50, 50)
        self.canvasWidth = 1200
        self.canvasHeight = 200
class Pit:
    def __init__(self, canvas, x):
        self.canvas = canvas
        y = 199
        self.id = self.canvas.create_polygon((x, y), (x+15, y), (x+15, y+10), (x, y+10), fill = 'purple')

#create sprites
player = Player(canvas, 'red')
#level 1
plat1 = Plat(canvas, 100, 100)
pit1 = Pit(canvas, 100)
endCoords = 200

tk.update_idletasks()
tk.update()
time.sleep(1)
for x in range(300):
    #update sprites/main loop
    player.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
