#final assingment
"""
fix the end of the game.  Make the player stop when end point is reached
"""

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
def collide(player, spriteList):
    for sprite in spriteList:
        playerPos = coords(player)
        spritePos = coords(sprite)
        if playerPos[2] >= spritePos[0] and playerPos[0] <= spritePos[2]:
            if playerPos[3] >= spritePos[1] and playerPos[3] <= sprite[3]:
                return True
        return False
def endGame(endCoords):
    playerPos = coords(player)
    endPos = endCoords
    if playerPos[0] > endPos:
        return True
    return False
class Player:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_polygon((190, 190), (190, 200), (200, 200), (200, 190),  fill = color)
        self.canvas.move(self.id, -190, 0)
        self.canvasWidth = 1200
        self.canvasHeight = 200
        self.x = 1
        self.y = 0
        self.run = True
        self.canvas.bind_all('<KeyPress-Up>', self.jump)
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        if collide(self, sprites) == True:
            self.run = False
        #pass
    def jump(self, evt):
        self.y = -3
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
sprites = [plat1, pit1]
endCoords = 200

tk.update_idletasks()
tk.update()
time.sleep(1)
while run == True:
    if player.run == False:
        run = False
    if endGame == True:
        run = False
    #update sprites/main loop
    player.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
