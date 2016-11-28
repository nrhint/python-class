#faster ball

from tkinter import *
import random
import time

tk = Tk()
tk.title("Bounce1.0")
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 600, height = 500, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

#create ball class
class Ball:
    #create ball and move it to starting position
    def __init__(self, canvas, paddle,  color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(0, 0, 25, 25, fill = color)
        self.canvas.move(self.id, 300, 100)
        self.starts = [-3, -2, -1, 0, 1, 2, 3]
        random.shuffle(self.starts)
        self.x = self.starts[0]
        self.y = -7
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.endGame = False
    #defines if the ball has hit the paddle
    def hitPaddle(self, pos):
        paddlePos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddlePos[0] and pos[0] <= paddlePos[2]:
            if pos[3] >= paddlePos[1] and pos[3] <= paddlePos[3]:
                return True
        return False
    #update ball position
    def draw(self):
        self.canvas.move(self.id,  self.x, self.y)
        pos = self.canvas.coords(self.id)
        random.shuffle(self.starts)
        if pos[1] <= 0:
            self.y = 7
        if pos[3] >= self.canvas_height:
            self.endGame = True
            #self.y = -3  #uncomment this line to make you invincable.
        if self.hitPaddle(pos) == True:
            self.y = -7
            self.x = self.starts[0]
        if pos[0] <= 0:
            self.x = self.starts[0]
            if self.x < 0:
                self.x = self.x * -1
        if pos[2] >= self.canvas_width:
            self.x = self.starts[0]
            if self.x > 0:
                self.x = self.x *-1

class Paddle:
    #init paddle and move it to starting position
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 300, 450)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas
        self.canvas.bind_all('<KeyPress-Left>', self.turnLeft)
        self.canvas.bind_all('<KeyPress-Right>', self.turnRight)
    #update paddle position
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turnLeft(self, evt):
        self.x = -3
    def turnRight(self, evt):
        self.x = 3

#init sprites
paddle = Paddle(canvas, 'green')
ball = Ball(canvas, paddle, 'pink')

#main loop
go = True

while go == True:
    if ball.endGame == True:
        time.sleep(3)
        tk.destroy()
        go = False
    else:
        ball.draw()
        paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
