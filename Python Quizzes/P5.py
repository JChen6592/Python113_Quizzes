import random

#Create file
test_1 = open("Whatever.txt","r")
a1 = test_1.read()
len_string = len(a1)
string_2 = ""

#random key generator
key1=random.randint(-1,25)
letter_key = str(random.choice('abcdefghijklmmnopqrstuvwxyz'))
#print(letter_key, letter_key.upper(), letter_key.lower())

#encryption file
for i in range (len_string):
   # print(chr(ord(a1[i]) + 1),end = " ")
   if a1[i] == letter_key.lower() or a1[i] == letter_key.upper() or a1[i] == " ":
       string_2 += a1[i]
   elif ord(a1[i].lower())-96 >= key1:
        reset = (ord(a1[i].lower()) - (96 + 26)+key1) + 96
        string_2 += chr(reset)
   else:
        string_2 += (chr(ord(a1[i]) + key1))
#print(string_2)
test_1.close()

#store keys
with open('Whatever_key.txt', 'w') as f:
  f.write('%d' % key1+"\n")
  f.write(str(letter_key))

#write string_2 in new file
test_2 = open("Whatever2.txt", "w")
test_2.write(string_2)
#print(string_2, file=test_2)
test_2.close()

#decryption part
test_4 = open("Whatever2.txt","r")
x = test_4.read()
test_4.close()

test_key = open("Whatever_key.txt", "r")
key2 =int( test_key.readline() )
letter_key2=str(test_key.readline())

test_key.close()

string_3 = ""
for i in range (len_string):
   # print(chr(ord(a1[i]) + 1),end = " ")
   if x[i] == letter_key2.lower() or x[i] == letter_key2.upper() or x[i] == " ":
       string_3 += x[i]
   elif ord(x[i].lower())+96 <= key2:
        reset_2 = (ord(x[i].lower()) + (96 - 26)- key2) - 96
        string_3 += chr(reset_2)
   else:
        string_3 += (chr(ord(x[i]) - key2))

print(string_3)



