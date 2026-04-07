#sum and average calculate
'''sum = 0
count = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    sum = sum+num
    count = count + 1
avarage = (sum/COUNT)
print("average =",avarage)
print("sum =",sum)'''
from sympy.codegen.cnodes import union

#fraction divider
'''from fractions import Fraction
a,b = input("Enter two numbers: ").split(" ")
result = Fraction(int(a),int(b))
print("answer =",result)'''

#Length counting without using len()
'''s = input("Enter a string: ")
count = 0
for i in s:
    count = count + 1
print("length of string =",count)'''

# username creating
'''mail = input("Enter a mail: ")
# for m in mail:
#     if m == "@":
#         break
#     print(m, end="")
or
# pop =  mail.index("@")
# print(mail.split("@")[0])'''

#frequency count
# s = "kya kar rhi ho qty ."
# ch = input("Enter charactor: ")
# count = 0
# for i in s:
#     if ch == i:
#         count = count + 1
# print("frequancy =",count)
#particuler index
'''s1 = input("Enter 1st string: ")
s2 = input("Enter 2nd string: ")
for i,s in zip(s1,s2):
    if i==s:
        print(s1.index(i),s2.index(s),"\n",(i,s),sep="")
'''
#vowel count
'''ster = input("Enter a string: ")
for i in ster:
    if i in("a","e","i","o","u"):
        print(i,end=",")'''

#particuler charactor remove
'''st= input("Enter a string: ")
for i in st:
    if i == i:
        st.split(i)
        print(i,end="")'''


#list reverse
'''List = input("Enter a list: ").split(" ")
reverse =List.reverse()
print(List)'''

#search in list
'''List = input("Enter a list: ").split(",")
search = List.index(input("Enter a string: "))
print(search)'''

#1st list item append another list ]
import math
'''list1 = input("Enter a list: ").split(" ")
list1 = list(map(int,list1))
list2 = []
for i in list1:
    list2.append(i**2)
print("squared list =",list2)'''

# reverse the word
'''str1 = input("Enter a sentence: ")
str = " ".join(str1)
str2 = str1[::-1]
str2 = " ".join(str2)
print(str1,'\n'"reverse = ",str2,sep="")
# or
rev = " "
for i in str1:
    rev = rev+i
print(rev)'''

# count the word in a sentence
'''sent = input("Enter a sentence: ").split(" ")
count = 0
for i in sent:
    count = count + 1
print(count)'''

#check ascending order
'''List1 = list(map(int,input("Enter a number : ").split(",")))
if List1 == sorted(List1):
    print("List in Ascending order")
else :
    print("List in Descending order")'''

# marge 2 list without (+)
'''list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
for i in list1:
        list2.append(i)
print(list2)'''

# replace item in list
'''list1 = ["apple", "banana", "mango", "orange"]
new_item = (input("Enter new item: "))
old_item = (input("Enter find item: "))
for i in range(len(list1)):
    if list1[i] == old_item:
        list1[i]= new_item
print(list1)'''

# convert 2d to 1d list

'''List = [[]]
print(List)
List2 = []
for o in List:
    for i in o:
        List2.append(i)
print(List2)'''

# union and intersection in list
'''list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
Union = []
inter = []
# Union = list( set(list1)|set(list2))
# print("Union =",Union)
# intersection = list( set(list1) & set(list2))
# print("intersection =",intersection)

# or

for i in list1:
    Union.append(i)
for j in list2:
    if j not in Union:
        Union.append(j)
print("Union =",Union)

for i in list1:
    if i in list2:
        inter.append(i)
print("intersection =",inter)'''

# find max in matrix
'''

#matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in matrix:
    print("max in row =",max(i))
# or
# for i in matrix :
#     maximum = i[0]
#     for j in i:
#         if j > maximum:
#             maximum = j
# print("maximum =",maximum)'''

#convert int to str
'''Int = 13
Int = str (Int)
print(type(Int))'''

# find shape of a matrix
'''matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rows = len(matrix)
cols = len(matrix[0])
print("shape of matrix =",(rows,cols))'''

#check multiplication of matrix
'''import numpy as np
a = np.array([
    [1,2,],
    [4,5,],
])
b = np.array([
    [7,8,9],
    [10,11,12],
])
mult = np.matmul(a,b)
print(a)
print(b)
print("multiplication =",mult,end= "\n")
'''
# list shorting
'''
list1 = [1,0,7,6,5]
sort_list = sorted(list1)
print(sort_list)'''

# find most used word in song
'''song = input("Enter a lyrics: ").lower()
word = song.split()
count = {}
for i in word:
    if i in count:count[i]+=1
    else:
        count[i] = 1
max_word =""
max_count = 0

for i in count:
    if count[i] > max_count:
        max_word = i
        max_count = count[i]

print("most used word =",max_word)
print("frequency =",max_count)'''

#convert list into dict

'''list1 = list(map(int,input("Enter a number : ").split(",")))
list2 = []
for i in list1:
    list2.append(i**2)

dictionary = dict(zip(list1,list2))
print(dictionary)'''

#marge two dictionary

'''dct = {
    "name": "vishal",
    "age": "19",
}
dct2 = {
    "hight": "167",
    "waight": "55",
}
dct.update(dct2)
print(dct)
    # or
dic3 = dct | dct2
print(dic3)'''

# swap key and value another dict

'''d = {'vishal':7,'kusum':2,'rakhi':8}
min_value = min(d.values())
max_value = max(d.values())
for key, value in d.items():
    if value == min_value:
        min_value = key
    if value == max_value:
        max_value = key
d[max_value], d[min_value] = d[min_value], d[max_value]
print(d)'''

#histogram find in sets
import matplotlib.pyplot as pl
# st = set(map(int,input("Enter a number : ").split(",")))
# count = 0
# hist = {}
# for i in st:
#     hist[i] = 0
#     if i ==i in hist:
#         hist[i] = count + 1
#     else :
#         hist[i] = 1
# print(hist)
'''nums = list(map(int, input("Enter numbers separated by space: ").split(",")))
bin_size = 1

hist = {}

min_val = min(nums)
max_val = max(nums)

start = min_val

while start <= max_val:
    end = start + bin_size - 1
    count = 0

    for n in nums:
        if start <= n <= end:
            count += 1

    hist[start] = count
    start = end + 1

print(hist)
pl.hist(nums)
pl.show()'''

#function
'''def vishal(a):
    result = {"upper":0,"lower":0}

    for i in a:
        if i.isupper():
            result["upper"]+=1
        elif i.islower():
            result["lower"]+=1
    return result
text = input("Enter a string: ")
print(vishal(text))'''

#
# def bag_of_words(sentences):
#     # Step 1: vocabulary banana
#     vocab = set()
#     for s in sentences:
#         for word in s.split():
#             vocab.add(word)
#
#     vocab = list(vocab)
#
#     # Step 2: vectors banana
#     vectors = []
#
#     for s in sentences:
#         words = s.split()
#         vector = []
#
#         for v in vocab:
#             vector.append(words.count(v))
#
#         vectors.append(vector)
#
#     return vocab, vectors
#
#
# data = [
#     "I love python",
#     "I love coding",
#     "python coding is fun"
# ]
#
# vocab, vectors = bag_of_words(data)
#
# print("Vocabulary:", vocab)
# print("Vectors:", vectors)

'''import numpy as np


def bag_of_words_numpy(sentences):

    # Step 1: vocabulary banana
    vocab = sorted(set(word for s in sentences for word in s.split()))

    # Step 2: zero matrix banana
    matrix = np.zeros((len(sentences), len(vocab)), dtype=int)

    # Step 3: matrix fill karna
    for i, s in enumerate(sentences):
        for word in s.split():
            j = vocab.index(word)
            matrix[i][j] += 1

    return vocab, matrix


data = [
"I love python",
"I love coding",
"python coding is fun"
]

vocab, matrix = bag_of_words_numpy(data)

print("Vocabulary:", vocab)
print("Matrix:\n", matrix)'''

# factorial
'''import math
def factorial(n):
    result = math.factorial(n)
    return result
num = int(input("Enter a number: "))
print(factorial(num))'''

'''login and registration
user = {}

while True:
    print("1. register","\n","2. login","\n","3. exit",sep="")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        if name in user:
            print("User already exists")
        else:
            print("registration successful")
    elif choice == 2:
        name = input("Enter your username: ")
        password = input("Enter your password: ")
        if name in user and user[name] == password:
            print("login successful")
        else:
            print("invalid username or password")
    elif choice == 3:
        print("thank you ")
        break
    else:
        print("invalid choice")

#or


users = {}

while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users:
            print("User already exists!")
        else:
            users[username] = password
            print("Registration successful!")

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print("Login successful!")
        else:
            print("Invalid username or password")

    elif choice == "3":
        print("Program ended")
        break

    else:
        print("Invalid choice")'''


