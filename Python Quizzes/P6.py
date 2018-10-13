#John Chen CSC 11300 Section 2L Morning Class
#Question 1
import random

class Game(object):
    def __init__(self,name):
        self.name = name
    def win(self):
        print("The winner is", self.name)
    def lose(self):
        print("The loser is", self.name)
    def choose(self):
        rand = random.randint(1,3)
        return rand

class player1(Game):
    def player1(self):
        pass
    def rock(self):
        print("Player 1, has thrown rock")
    def paper(self):
        print("Player 1, has thrown paper")
    def scissor(self):
        print("Player 1, has thrown scissors")

class player2(Game):
    def player2(self):
        pass
    def rock(self):
        print("Player 2, has thrown rock")
    def paper(self):
        print("Player 2, has thrown paper")
    def scissor(self):
        print("Player 2, has thrown scissors")

w1,w2,l1,l2 = Game("Player 1"),Game("Player 2"),Game("Player 1"),Game("Player 2")
p1 = player1("Player 1")
p2 = player2("Player 2")
hand_1, hand_2 = p1.choose(), p2.choose()

if hand_1 != hand_2:
    if hand_1 == 1 and hand_2 == 3:
        p1.rock(), p2.scissor(), w1.win(),l2.lose()
    elif hand_1 == 3 and hand_2 == 1:
        p1.scissor(),p2.rock(),w2.win(),l1.lose()
    elif (hand_1 > hand_2) and (hand_1 == 3 and hand_2 == 2):
        p1.scissor(), p2.paper(), w1.win(),l2.lose()
    elif (hand_1 > hand_2) and (hand_1 == 2 and hand_2 == 1):
        p1.paper(), p2.rock(), w1.win(),l2.lose()
    if (hand_1 < hand_2) and (hand_1 == 1 and hand_2 == 2):
        p1.rock(), p2. paper(), l1.lose(),w2.win()
    elif (hand_1 < hand_2) and (hand_1 == 2 and hand_2 == 3):
        p1.paper(), p2.scissor(), l1.lose(),w2.win()
else:
    print("Both players throw the same hand, it is a tie... ")

#print(hand_1,hand_2) where 1 = rock, 2 = paper, 3 = scissors
'''Ans:Player 1, has thrown rock
       Player 2, has thrown paper
       The loser is Player 1
       The winner is Player 2'''

#Question #2

from tkinter import *

console = Tk()
Label(console,text="Hello World\n").pack()
Button(console,text="Quit",command =quit).pack()\
console.mainloop()


