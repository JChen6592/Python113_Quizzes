#John Chen CSC 11300 Section 2L Morning Class
#Question A
def minutes_to_milliseconds(min_float):
    return min_float * 60000
print("Minutes to milliseconds. ")
min_float = float(input("Please enter an integer less than 61: "))
milli_float = minutes_to_milliseconds(min_float)
print(min_float," minutes converts to",milli_float," milliseconds")
#Minutes to milliseconds. Please enter an integer less than 61: 30 30.0  minutes converts to 1800000.0  milliseconds

#Question B
def get_grades():
    t1 = float(input("Please enter a grade for test 1: "))
    t2 = float(input("Please enter a grade for test 2: "))
    return t1,t2
def get_avg(t1,t2):
    total_avg = (t1 + t2)/2
    return total_avg
t1, t2 = get_grades()
avg = get_avg(t1,t2)
print("The test score average was: ",avg)
#Please enter a grade for test 1: 80 Please enter a grade for test 2: 14 The test score average was:  47.0

#Question C
import math
def get_var():
    a = float(input("Enter an integer for a: "))
    b = float(input("Enter an integer for b: "))
    c = float(input("Enter an integer for c: "))
    return a,b,c
def neg_root(a, b, c):
    k = (b * b) - (4 * a * c)
    neg_quad = (-b - math.sqrt(k)) / (2 * a)
    return neg_quad
def pos_root(a, b, c):
    k = (b * b) - (4 * a * c)
    pos_quad = (-b + math.sqrt(k)) / (2 * a)
    return pos_quad
a, b, c = get_var()
quad1 = neg_root(a, b, c)
quad2 = pos_root(a, b, c)
print("The quadratic formula is: ", quad1," and ",quad2)

#Question D
import math
def speed():
    """Converting km/h to m/s"""
    s1 = 40
    s2 = 60
    return s1 * (math.pow(10, 3)) * (1 / 60) * (1 / 60), s2 * (math.pow(10, 3)) * (1 / 60) * (1 / 60)
def get_avg(s1,s2):
    total_avg = (s1 + s2)/2
    return total_avg
s1, s2 = speed()
avg = get_avg(s1,s2)
print("The average speed in m/s is: ",avg)
#The average speed in m/s is 13.88888888888889

#Question E
def get_value():
    F = float(input("Enter an integer for Farenheit: "))
    re_float = 0
    return F, re_float
def farenheit_to_reaumer(F):
    re_float = (F - 32)/ 2.25
    return re_float
def reaumer_to_celsius(re_float):
    C_float = re_float * 1.25
    return C_float
F, re_float = get_value()
r_to_c = reaumer_to_celsius(re_float)
f_to_r = farenheit_to_reaumer(F)
print("Farenheit to Reaumer is ", f_to_r, " and Reaumer to Celsius is ", r_to_c)

#Question F
#Confused with this question, shouldn't a cube only have 6 sides?
def sided_square():
    n = float(input("Enter an integer with nth sides"))
    return n
def radius():
    n = sided_square()
    r = n / 4
    return r

#Question G
def row():
    print("^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^")
def col():
    print("i        i        i        i        i")
def grid():
    row()
    col()
    col()
    col()
    col()
grid()
grid()
grid()
grid()
row()






