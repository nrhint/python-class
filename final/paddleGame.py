#paddle game
"""
to do:
make a high score list?
"""

from tkinter import *
import time, random, pickle, paddleGameInit

paddleGameInit.run('dontDeleteMe!!!')

tk = Tk()
canvas = Canvas(tk, width = 700, height = 500)

tk.title("Paddle Game")

gameMode = input("high score chalange? (y, n):  ")

def endGame(winner):
    canvas.create_text(350, 250, text = "Player " + str(winner) + " Wins!!!")

class Player0:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_polygon((0, 0), (0, 70), (10, 70), (10, 0), fill = color)
        self.canvas.move(self.id, 650, 250)
        self.x = 0
        self.y = 0
        self.canvas.bind_all("<KeyPress-Up>", self.moveUp)
        self.canvas.bind_all("<KeyPress-Down>", self.moveDown)
        self.canvasHeight = 500
    def move(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvasHeight:
            self.y = 0
    def moveDown(self, evt):
        self.y = 3
    def moveUp(self, evt):
        self.y = -3

class Player1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_polygon((0, 0), (0, 70), (10, 70), (10, 0), fill = color)
        self.canvas.move(self.id, 50, 250)
        self.x = 0
        self.y = 0
        self.canvas.bind_all("<KeyPress-w>", self.moveUp)
        self.canvas.bind_all("<KeyPress-s>", self.moveDown)
        self.canvasHeight = 500
    def move(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvasHeight:
            self.y = 0
    def moveDown(self, evt):
        self.y = 3
    def moveUp(self, evt):
        self.y = -3

class Ball:
    def __init__(self, canvas, player0, player1, mode, color):
        self.canvas = canvas
        self.paddle0 = player0
        self.paddle1 = player1
        self.id = self.canvas.create_oval((0, 0), (25, 25), fill = color)
        self.canvas.move(self.id, 350, 250)
        self.starts = [-2, -1, 0, 1, 2]
        random.shuffle(self.starts)
        self.x = 2
        self.y = self.starts[1]
        self.canvasHeight = 500
        self.canvasWidth = 700
        self.winner = None
        self.leftScore = 0
        self.rightScore = 0
        if mode == "No" or "no" or "N" or "n":
            self.winScore = 9999
        else:
            self.winScore = 3
    def hitPaddle(self, pos):
        paddlePos = self.canvas.coords(self.paddle0.id)
        if pos[2] >= paddlePos[0] and pos[0] <= paddlePos[2]:
            if pos[3] >= paddlePos[1] and pos[3] <= paddlePos[3]:
                return True
        paddlePos = self.canvas.coords(self.paddle1.id)
        if pos[2] >= paddlePos[0] and pos[0] <= paddlePos[2]:
            if pos[3] >= paddlePos[1] and pos[3] <= paddlePos[3]:
                return True
        return False
    def move(self):
        pos = self.canvas.coords(self.id)
        random.shuffle(self.starts)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvasHeight:
            self.y = -2
        if self.hitPaddle(pos) == True:
            self.y = self.starts[1]
            self.x = self.starts[0]
        if pos[0] <= 0:
            self.x = self.starts[0]
            if self.x < 0:
                self.x = self.x * -1
                self.leftScore += 1  #comment this line to make the left side invincible
        if pos[2] >= self.canvasWidth:
            self.x = self.starts[0]
            if self.x > 0:
                self.x = self.x *-1
                self.rightScore += 1  #comment this line to make the right side invincible
        self.canvas.move(self.id, self.x, self.y)
    def end(self):
        if self.rightScore >= self.winScore:
            self.winner = 1
        if self.leftScore >= self.winScore:
            self.winner = 0

#init window

canvas.pack()
tk.update_idletasks()
tk.update()

time.sleep(1)

#init sprites

player0 = Player0(canvas, 'red')
player1 = Player1(canvas, 'blue')
ball = Ball(canvas, player0, player1, str(gameMode), 'yellow')

rightScore = canvas.create_text(75, 50, text = str(ball.rightScore))
leftScore = canvas.create_text(625, 50, text = str(ball.leftScore))

#

def end(evt):
    if ball.rightScore > ball.leftScore:
        ball.winner = 1
    else:
        ball.winner = 0

canvas.bind_all("<KeyPress-Return>", end)

#main loop

while ball.winner == None:
    canvas.itemconfig(rightScore, text = str(ball.rightScore))
    canvas.itemconfig(leftScore, text = str(ball.leftScore))
    ball.end()
    player0.move()
    player1.move()
    ball.move()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


endGame(ball.winner)

if ball.winner == 1:
    score = ball.rightScore
else:
    score = ball.leftScore

x = True
file = open("highScores.dat", mode = 'rb')
scores = pickle.load(file)
file.close()
scores.append(score)
scores.sort(reverse = True)
while x == True:
    if len(scores) >=6:
        scores.pop()
    else:
        x = False
file = open("highScores.dat", mode = 'wb')
pickle.dump(scores, file)
file.close()
print(scores)

