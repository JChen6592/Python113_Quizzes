#John Chen, 11300 Morning in class assignment

#Question 1
test_1 = open("file.txt","w")
print("Hello",file=test_1)
print("Python",file=test_1)
test_1.close()
test_1 = open("file.txt","r")
a1 = test_1.readline()
a2 = test_1.readline()
a3 = " "
tracer = 0
len_string1 = len(a1)
len_string2 = len(a2)
i = 0
j = 0
for i in range (len_string1):
    for j in range (len_string2):
        if a1[i] != a2[j]:
            tracer+=1
            if tracer == len_string2:
                a3 += a1[i]
                tracer = 0
                j = 0
print(a3)
#Answer is Hell

#Question 2
test_2 = open("file2.txt","w")
print("Ape",file=test_2)
print("Monkey",file=test_2)
test_2.close()
test_2 = open("file2.txt","r")
a1 = test_2.readline()
a2 = test_2.readline()
a3 = " "
tracer = 0
len_string1 = len(a1)
len_string2 = len(a2)
i = 0
j = 0
for i in range (len_string2):
    for j in range (len_string1):
        if a2[i] != a1[j]:
            tracer+=1
            if tracer == len_string1:
                a3 += a2[i]
                tracer = 0
                j = 0
print(a3)
#Answer is Monky

#Question 3
distinct_1 = open("file2.txt","w")
print("TallTZFTZ",file=distinct_1)
print("Ball",file=distinct_1)
distinct_1.close()
distinct_1 = open("file2.txt","r")
a1 = distinct_1.readline()
a2 = distinct_1.readline()
ab = " "
tracer = 0
len_string1 = len(a1)
len_string2 = len(a2)
i = 0
j = 0
for i in range (len_string1):
    for j in range (len_string2):
        if a1[i] != a2[j]:
            tracer+=1
            if tracer == len_string2:
                ab += a1[i]
                tracer = 0
                j = 0
print(''.join(set(ab)))
#Answer is T1FZ

#Question 4
distinct = open("file2.txt","w")
print("Bye",file=distinct)
print("WhyWWWHh",file=distinct)
distinct.close()
distinct = open("file2.txt","r")
a1 = distinct.readline()
a2 = distinct.readline()
ac = " "
tracer = 0
len_string1 = len(a1)
len_string2 = len(a2)
i = 0
j = 0
for i in range (len_string2):
    for j in range (len_string1):
        if a2[i] != a1[j]:
            tracer+=1
            if tracer == len_string1:
                ac += a2[i]
                tracer = 0
                j = 0
print(''.join(set(ac)))
#Answer is ZhHW

#Question 5
word = print("Enter a word to see if it has 'aeiou' in that order: ")
vowels = "aeiou"

for i in range(len(word)):