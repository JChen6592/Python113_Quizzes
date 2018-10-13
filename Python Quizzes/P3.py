#John Chen CSC 11300 Section 2L Morning Class
#Question 1
is_prime = 0
is_prime = int(input("Enter an integer(0 to terminate) >> "))
for is_prime in range(1,is_prime + 1):
    if (is_prime == "1"):
        break
    if (is_prime == 2):
        print(is_prime)
    if (is_prime == 3):
        print(is_prime)
    if (is_prime == 5):
        print(is_prime)
    if (is_prime == 7):
        print(is_prime)
    if (is_prime % 2 != 0):
        if (is_prime % 3 != 0):
            if (is_prime % 5 != 0):
                if (is_prime % 7 != 0):
                    print(is_prime)
is_prime = int(input("Enter an integer(0 to terminate) >> "))

#Question 2
i = 0
while i * i <= n




#Question 3
grades = 0
grades = float(input("Enter in grades(negative to exit) >> "))
while grades >= 0 & grades <= 100:
    if grades >= 90:
        print ("A")
    elif grades >= 80 & grades < 90:
        print("B")
    elif grades >= 70 & grades < 80:
        print("C")
    elif grades >= 65 & grades < 70:
        print("D")
    else:
        print ("F")
    grades = float(input("Enter in grades(negative to exit) >> "))

#Question 4
def Collatz(n):
    if n % 2 == 0:
        even = n / 2
        n = even
        print(even)
        return n/2
    else:
        comp = (3 * n) + 1
        n = comp
        print (comp)
        return (3 * n) + 1

n = int(input("Enter a positive integer >> "))
rep = Collatz(n)


