#Question 1: Who is the survivor?




#Question 2: Coin Flip Counter
import random
win_1, win_2 = 0,0

games = int(input("How many games?"))
total = games

while games > 0:
    flip = random.randint(1,2)
    #print(flip)
    if flip == 1:
        print("H")
        win_1 += 1
        #print("# of heads landed:",win_1)
    else:
        print("T")
        win_2 += 1
        #print("# of tails landed:",win_2)
    games -= 1

H_loss, T_Loss = total - win_1,total - win_2
print("Max number of consecutive wins - Heads: ", win_1, "Tails: ", win_2)
print("Max number of consecutive losses - Heads:", H_loss, "Tails: ", T_Loss)

#Question 4: Subsets in Set
#Itertools - Functions creating iterators for efficient looping
from itertools import chain, combinations

def subs_in_set(p):
    #Touples with empty set
    #return chain(*map(lambda r: combinations(p, r), range(0, len(p) + 1)))
    #Touples without empty set
    return chain(*map(lambda r: combinations(p, r), range(1, len(p)+1)))

for subsets in subs_in_set([1,2,3,4,5,6,7]):
    print(subsets)

#Question 5: 4 features of Object Oriented Programming
'''The 4 features of object oriented programming are:
1.Encapsulation: It hides design details to make a program more to be modified later and clearer
Example:
class alphabet(object):
    def __init__(self):
        self.1 = abc
        self._2 = abcdef
        self.__3 = abcdefghijk
string = alphabet()
print(obj.1)
print(obj._2)
print(obj.__3) --> wont print this because this is private

2.Modularity: the ability to make objects stand alone so they can be reused
Example:
# add.py
def add(x)
    print('hello' + x)
add("world") 
add("Mother and Father")
add("Neighbor")
       
3.Inheritance: create new objects by inheriting object characteristics/attributes while creating or over-riding for the object
Example:
class Parent(object):
    def eye_col(self):
        print("My eye color is blue")
    def nose(self):
        print("My nose is slim")
    def face(self):
        print("My face is thin")
class Child(Parent):
    pass 

daughter = Child()
daughter.eye_col()   --> "My eye color is blue"

4.Polymorphism: Allows one message to be sent to any object and have it respond based on the type of the object
Example:
class Mom():
    def greet(self):
        print("Good Morning son")
class Dad():
    def greet(self):
        print("Good Morning Kiddo")
class Sister()
    def greet(self):
        print("Good Morning Little Brother")        
'''

#Question 6: 2 Features to view names of functions and variables