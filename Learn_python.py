
# 1) Python basics
# Common data types

a = 10      # interger
b = 3.5 #float
c = True #boolean
d = "Hello" #string

# python is dynamically typed so no need to declare types





# input and output

x = input() # always return string

x = int(input()) # covert input to integer

a,b = map(int, input().split()) #multiple inputs - here 1 5 is typed and its split to give a=1,b=5
a,b = map(int, input().split())

arr = list(map(int, input().split())) #list input same as above but now its a list [1,5]

print(a) #printing output
print(a,b) #printing output

#type casting - used when input is string but we need numbers intergers

x = '5'
y = int(x)
z = float(x)






#OPERATORS - arthematics like - +  -  *  /   //   %

a = 7//2 #integer division returns 3
b = 7%2 #remainder returns 1

# comparisions like - ==  !=  >  <  >=  <=
# returns True or False






#LOGICAL Operators - and  or  not

if a > 0 and b > 0:
    print("both positive")

a = 5
b = 7
c = a + b
print(c) #check if this is CORRECT

a = 75 #find if this is even or odd

if a % 2 == 0:
    print('even')
else:
    print('odd')


if a > 0 and b>0:
    print("both positive")
else:
    print("both not positive")




# conditional statments

#if
x = 10

if x > 10:
    print("positive")


# if-else
x = 10

if x > 10:
    print("positive")
else:
    print("Negative")


# if-elif-else
x = 0

if x > 0:
    print("positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")








# Nested if 
x = 15

if x > 0:
    if x % 2 == 0:
        print("positive even")
    else:
        print("positive odd")







# Multiple conditions in single line
if x > 0 and x < 10:
    print("Single digit positve")


if x == 1 or x == 0:
    print("Binary digit")
else:
    print("non binary")


if not x: #here not x means empty. while x means something.
    print("x is zero")






#Chained comparision
if 1 <= x <= 100:
    print("valid")



#Max of two numbers

if a > b:
    max_val=a
else:
    max_val=b



if a>b:
    max_val = a
else:
    max_val=b










# Range check
n=[1,2,3,4]
l=0
r=arr[n-1]

if l <= x <= r:
    print("inside range")

if not n: #checks if the list is empty
    pass





# Loops in python

#While loop
# while condition:

i = 1
while i > 5:
    print(i)
    i+=1 # this does not run because it false

i=1
while i <=5:
    print(i)
    i+= 1

#or you can don below, same result as above but DSA preffered
for i in range(1,6):
    print (i)

# what does this mean and also learn about the significance(digit processing only)
n = 1234
while n > 0:
    digit = n % 10
    print(digit)
    n//=10

n =1234

while n>0:
    digit = n%10
    print(digit)
    n//=10

#digit counting

n=1234
count=0

while n>0:
    count+=1
    n//=10

#sum of digits

n=1234
sum=0

while n>0:
    sum =+ n%10
    n//=10

#reverse digits
n=1234
rev=0

while n>0:
    rev=rev*10 + n%10
    n//=10

print(rev)


# two pointer pattern, common
l = 0
r = n - 1

while l > r:
    l += 1
    r -= 1


# infinte look so be carefule when running
while True:
    print("Hello")
    break






# Break, continue, pass


# break is to stop loop

while i > 10:
    if i == 5:
        break
    i += 1


# how does continue works

for i in range(5):
    if i == 2:
        continue
    print(i)


# pass - do nothing

if x>0:
    pass






# For loop

for i in range(5):
    print(i)


# looping throught list DSA style

arr= [10,20,30]

for x in arr:
    print(x)

# looping for index for each value in list

arr=[10,20,30]

for i in range(len(arr)):
    print(arr(i))

#Nested loops - high time complexity

for i in range(len(n)):
    for j in range(n):
        print(i,j)



# important dsa loops patterns

# prefix sum style

sum = 0
for x in arr:
    sum += x




#### exercises to remember
# print numbers from 1 to N

n = 5
for i in range(1, n+1):
    print(i)



#count digits of a number

num = 1234
count = 0

while num > 0:
    count += 1
    num//=10
print (count)

# reverse a number

n = 1234
rev = 0

while num>0:
    digit = num % 10
    rev = rev * 10 + digit
    num//= 10
print(rev)


### Functions
#Defining a functions

def function_name(parameters):
    #code block
    return value #optinal

#example
def greet():
    print("hello dsa!")

greet() #calling this functions



#functions with parameters

def add(a,b):
    return a+b

result = add(5,3)
print(result)


#default arguments

def power(x,y=2):
    return x**y

print(power(2))
print(power(2,3))


#return values

def square(n):
    return n**n

print(square(5))

#recursive functions intro

def factorial(n):
    if n==0: # bse case is mandatory if not, infinete recursions
        return 1
    return n*factorial(n-1) #recursions here

print(factorial(5))





#example problem to checkif a number is prime
n=7
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i ==0:
            return False
    return True


#sum of Array
arr=[1,2,3,4]
def array_sum(arr):
    total=0
    for x in arr:
        total+=x
    return total


#even or odd

n = 5
def even_odd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")


#functions to count digits of a number

n=123456

def count_digits(n):
    count=0
    while n>0:
        count+=1
        n//=10
    return count


#recursive functions to compute power(x,n)

def power(x,n):
    if n==0:
        return 1
    if n<0:
        return 1/ power(x,-n)
    return x*power(x,n-1)
    

#functions to reverse a number

def reverse_number(n):
    rev = 0
    while n>0:
        rev=rev*10+n%10
        n//=10
    return rev

#reverse a number but in recursive
def reverse_number_recursive(n):
    if n<0:
        return -reverse_number_recursive(-n)#if negative, reverse its positive part and add - sign
    if n<10:
        return n #if single digits, return it cause its single
    digits = len(str(n))-1 #this is the number of digits to shift
    return(n%10)*(10**digits) + reverse_number_recursive(n//10)


### python built in must know for DSA
#len()
arr=[1,2,4]
print(len(arr)) #3

#min() max()
arr=[1,2,3]
print(min(arr)) #1
print(max(arr)) #3

#sum()
arr=[1,2,3]
print(sum(arr)) #6

#abs()/pow()
print(abs(-5))
print(pow(2,3))

#enumerate()
arr = [10,20,30]
for i, val in enumerate(arr):
    print(i,val)

#zip()
a = [1,2,3]
b=['a','b','c']

for x,y in zip(a,b):
    print(x,y)





#sorted() vs .sort()
#time complexity of sorting is O(n log n)
arr = [3,6,2,5]
print(sorted(arr)) #returns new sorted list
arr.sort() #sorts list in place




#set() - common for removing duplicates, frequency maps etc
arr = [1,2,2,3]

s = set(arr)
print(s) #{1,2,3}


#dict() - key-value map
#core for hashing in DSA - very fast for lookup, frequency, mapping problems
freq = {}
arr = [1,2,2,3,4,4] 
for x in arr:
    freq[x] = freq.get(x,0)+1
print(freq) #{1:1,2:2,3:1,4:2}



#example

arr = [6,6,4,4,2,6,1,2]

freq = {}

for x in arr:
    freq[x] = freq.get(x,0) + 1
print(freq)



#print elements with their indices using enumerate

yo = ["hey","bye","hola"]

for index, yo in enumerate(yo):
    print(index, yo)


#sort a list and remove duplicates
arr=[1,5,5,3,6]

sorted= sorted(set(arr))




#####Stringss

#Strings and indexing

s="DSArocks"

print(s[0]) #D
print(s[-1]) #s ->last charecter
print(s[2:5]) #Aro -> slicing from index 2 to 4



#transversing strings
s= "DSA"

for char in s:
    print(char) #normal transversing

for i in range(len(s)):
    print(i, s[i]) #transversing with index


#common string operations
s= "hello"

print(s.upper()) #HELLO
print(s.lower()) #hello
print(s.replace("h", "H")) #Hello
print(s.strip()) #remove leading/trailing spaces
print("".join(['a','b','c'])) # 'a b c'


#string reversal
s= 'DSA'

rev = s[::-1]
print(rev) #'ASD'


#check palindrom
s= 'level'
if s==s[::-1]:
    print("palindrome")


#frequency counting (extremly common in interview questions)
s='aaabbc'
freq={}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
print(freq) #{'a':3,'b':2,'c':1}


#substrings
s="abc"
print(s[1:4]) #SAr ->slice from index 1-3

#all substring using nested loops
s='abc'
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])




##Lists ARRAYS

arr = [10,20,30,40] #normal list

arr = list(map(int, input().split())) #dynamic input array

#accessing elemnts
print(arr[0])
print(arr[-1])

#transversing an array()list

for x in arr:
    print(x)

#using index

for i in range(len(arr)):
    print(i, arr[i])

#modifying elemnts (in-place)

arr[0] = 100

#common list operators
arr.append(50) #adds at end
arr.pop() #removes last
arr.insert(1,99) #insert at index

#reversing an array
arr.reverse()

#reversing using slice
rev = arr[::-1]







#prefix sum
arr = [1,2,3,4]
prefix= [0]*len(arr)

prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

print(prefix)


#searching in list
target = 30
found = False

for x in arr:
    if x ==target:
        found=True
        break

#sorting
arr.sort()
sorted_arr= sorted(arr)

#####IMPORTANT DSA PATTERNS

#two pointer
l,r = 0, len(arr)-1
while l<r:
    l+=1
    r-+1



#sliding window

l=0
for r in range(len(arr)):
    #expand window
    while condition:
        l+=1


#kadane's algorithm

max_sum = arr[0]
curr = 0

for x in arr:
    curr = max(x, curr+x)
    max_sum= max(max_sum, curr)




#tupless
#immutable, can store mixed types, useful to return multiple values from functions

t= (1,2,3)

#accessing elemnets
print(t[0])
print(t[-1])

#returning multiple values from a functions
def min_max(arr):
    return (min(arr), max(arr))

a,b = min_max([1,2,3])
print(a,b) # 1,3


#sets (uniqueness and fast lookups)

s = {1,2,3,2}
print(s) #{1,2,3}

a ={1,2,3}
b={2,3,4}

print(a | b) #union -> {1,2,3,4}
print(a&b) #intersections {2,3}
print(a-b) #diffrencr {1}

#adding and removing
s.add(4)
s.remove(2)

#sets are important because they remove duplicates, check membership O(1)

#check if array has duplicates
arr = [1,2,3,2]

if len(arr) != len(set(arr)):
    print("duplicates exist")


#count unique elemnets
arr = [1,2,2,3,3,3]
print(len(set(arr))) #3






#######  DICTONARIES in python

#key-value pair

freq = {"a":3,"b":5}
print(freq(a)) #3


#creating dictonaries

dict={}

dict={"a":3,"b":4}

#adding and updating
d["z"]= 3 #add new key
d["x"]= 10 #update value


#accessing keys and values
print(d.keys())    # dict_keys(['x','y','z'])
print(d.values())  # dict_values([10,2,3])
print(d.items())   # dict_items([('x',10),('y',2),('z',3)])


#iterate over dictonary
for key,value in d.items():
    print(key, value)



#### DICTONARY in DSA patterns

arr =[1,2,2,3,3,3]
freq ={}
for x in arr:
    freq[x] = freq.get(x,0)+1

most_freq= max(freq, key=freq.get)
print(most_freq) #3

## TWO SUM PROBLEM
arr = [2,7,11,15]
target = 9
d={}

for i, num in enumerate(arr):
    if target -num in d:
        print(d[target-num], i)
    d[num] = i





#### RECURSIVE in DSA#

#simple counting
def print_n(n):
    if n == 0:
        return
    print(n)
    print_n(n-1)

print_n(5)


#sum of array
def sum_array(arr,n):
    if n == 0:
        return 0
    return arr[n-1] + sum_array(arr, n-1)
print(sum_array([1,2,3,4], 4))


#fibonacci

def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5)) #5


##### Time and space complexity

| Pattern               | Time Complexity | Space Complexity |
| --------------------- | --------------- | ---------------- |
| Single loop           | O(n)            | O(1)             |
| Nested loops          | O(n²)           | O(1)             |
| Binary search         | O(log n)        | O(1)             |
| Recursion (linear)    | O(n)            | O(n) stack       |
| Recursion (tree)      | O(2^n)          | O(n) stack       |
| Sorting (Python sort) | O(n log n)      | O(n)             |


## Always think about worst case




















































