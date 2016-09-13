from random import choice, randint

class giraffe:
    def __init__(self):
        comands = ["lFF", "rFF", "lFB", "rFB", "dance", "rdance"]
        print("comands: lFF, rFF, lFB, rFB, dance, rdance")
        print('')
    def lFF(self):
        print("Left foot foward")
    def rFF(self):
        print("Right foot foward")
    def lFB(self):
        print("Left foot back")
    def rFB(self):
        print("Right foot back")
    def dance(self):
        self.lFF()
        self.lFB()
        self.rFF()
        self.rFB()
        self.lFB()
        self.rFB()
        self.rFF()
        self.lFF()

nathan = giraffe()
nathan.dance()
