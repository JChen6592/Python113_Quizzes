#John Chen CSC 11300 Section 2L Morning Class

'''Question 1
 n = 42 is legal but 42 = n is not because on the lhs it has to be a variable

Question 2
x = y = 1 is a valid code such that it is a statement of declaring that x and y are both
assigned to 1

Question 3
If you were to put a period at the end of a statement (i.e x = 9.) nothing would happen

Question 4
If you put a semi-colon at the end of a statement there would be an error and you would have to remove it

Question 5
Python doesnt not allow xy such that you need a mathematical assignment such as x * y

Question 6
They are known as high level language

Question 7
If you were to print a statement and leave out one ( or both () there would be a syntax error and
nothing would happen

Question 8
If you were to print a statement and leave out one " or both " " there would be a syntax error and nothing
would print

Question 9
A Python script is an executable file that is first translated into C and makes it into an interpreter

Question 10
#Python is considered a higher level language/interpreter language
'''

#1 Given 42 minutes and 42 seconds
min_to_secs = 60 * 42
sec = 42
total = min_to_secs + sec
print("There are:",total)
print(" seconds in 42 minutes and 42 seconds")

#2 The volumes for spheres of two different radii
import math
r1 = 4
vol_sphere = 4/3 * math.pi * math.pow(r1,3)
r2 = 6
vol_sphere2 = 4/3 * math.pi * math.pow(r2,3)

print("The volume in a 4 radius sphere is: ",vol_sphere)
print("The volume in a 4 radius sphere is: ",vol_sphere2)

'''Showing -40 degrees is similar in F and C
 F = 9/5 * C + 32 '''

print("C = 9/5 * C + 32,\nC - 9/5 * C = 32,\n-4/5 * C = 32,\nC = 32 * -(5/4),\nC = -40")
print("\nF = 9/5 * F + 32,\nF - 9/5 * F = 32,\n-4/5 * F = 32,\nF = 32 * -(5/4),\nF = -40")

#3 How many cubes can fit in the rectangle
import math
a = 0
R = (1 * 2 * 3)  #* math.pow(a,3)
C = (1 * 1 * 1)#math.pow(a,3)
fit = R / C
print("The amount of cubes that can fit within the prism is:",fit)