#John Chen CSC 11300 Section 2L Morning Class
#Question 1
anagram = input("Please enter two words with a space in between: ")
a = anagram.split()
a_lower = [a.lower() for a in anagram.split()]

first = []
second = []

for char in a_lower[0]:
    first += char

for chars in a_lower[1]:
    second += chars

len_first = len(a_lower[0])
len_sec = len(a_lower[1])
first.sort()
second.sort()

if len_first == len_sec and first == second:
    print("These two words are anagrams of each other! ")
else:
    print("These two words are not anagrams of each other, try again... ")

#Question 2
LettersLC = "abcdefghijklmnopqrstuvwxyz"
LettersUC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num_list = []
for x in range (0,52):
    num_list.append(x)

Total = LettersLC + LettersUC
for char in Total:
    Total += char
output = dict(zip(Total,num_list))
sorted_list = [(k,v) for v,k in sorted([(v,k) for k,v in output.items()])]
print(sorted_list)