from tkinter import *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("HI HI HI.")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width = 500, height = 500,
                             highlightthickness = 0)
        #num =  random.randint(0, 4)
        #self.bg = PhotoImage(file = "bg" + str(num) + ".png")
        self.bg = PhotoImage(file = "bg2.png")
        w = self.bg.width()
        h = self.bg.height()
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x *w, y*h, image = self.bg,
                                         anchor = 'nw')
        self.sprites = []
        self.running = True
    def mainLoop(self):
        while 1:
            if self.running == True:
                Sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)

class Coords:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def withinX(co1, co2):
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
            or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
            or (co2.x2 > co1.x1 and co2.x2 < co1.x2):
        return True
    else:
        return False

def withinY(co1, co2):
    if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
            or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
            or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
            or (co2.y2 > co1.y1 and co2.y2 < co1.y2):
        return True
    else:
        return False

def colided_left(co1, co2):
    if withinY(co1, co2):
        if co1.x1 <=co2.x2 and co1.x1 >=co2.x1:
            return True
    return False

def colided_right(co1, co2):
    if withinY(co1, co2):
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
            return True
    return False

def colided_top(co1, co2):
    if withinX(co1, co2):
        if co1.y1 <=co2.y2 and co1.y1 >=co2.y1:
            return True
    return False

def colided_bottom(y, co1, co2):
    y_calc = co1.y2 + y
    if y_calc >= co2.y1 and y_calc <= co2.y2:
        return True
    return False

class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = False
    def move(self):
        pass
    def coords(self):
        return self.coordinates

class PlatSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image = self.photo_image, anchor = 'nw')
        self.coordinates = Coords(x, y, x+width, y+height)
        
g = Game()
#load sprites
plat1 = PlatSprite(g, PhotoImage(file = "plat1.png"), random.randint(0, 400), 480, 100, 10)
plat2 = PlatSprite(g, PhotoImage(file = "plat1.png"), random.randint(0, 400), random.randint(0, 500), 100, 10)
plat3 = PlatSprite(g, PhotoImage(file = "plat1.png"), random.randint(0, 400), random.randint(0, 500), 100, 10)
plat4 = PlatSprite(g, PhotoImage(file = "plat1.png"), random.randint(0, 400), random.randint(0, 500), 100, 10)
plat5 = PlatSprite(g, PhotoImage(file = "plat2.png"), random.randint(0, 400), 100, 100, 10)
plat6 = PlatSprite(g, PhotoImage(file = "plat2.png"), random.randint(0, 400), random.randint(0, 500), 100, 10)
plat10 = PlatSprite(g, PhotoImage(file = "plat2.png"), random.randint(0, 400), random.randint(0, 500), 100, 10)
plat7 = PlatSprite(g, PhotoImage(file = "plat2.png"), random.randint(0, 400), random.randint(0, 500), 100, 10)
plat8 = PlatSprite(g, PhotoImage(file = "plat3.png"), random.randint(0, 400), random.randint(0, 500), 100, 10)
plat9 = PlatSprite(g, PhotoImage(file = "plat3.png"), random.randint(0, 400), random.randint(0, 500), 100, 10)
#add sprites
g.sprites.append(plat1)
g.sprites.append(plat2)
g.sprites.append(plat3)
g.sprites.append(plat4)
g.sprites.append(plat5)
g.sprites.append(plat6)
g.sprites.append(plat7)
g.sprites.append(plat8)
g.sprites.append(plat9)
g.sprites.append(plat10)
#init game
g.mainLoop()
