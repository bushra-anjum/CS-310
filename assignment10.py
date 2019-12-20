cheeses=['cheddar','Edem','Gouda']
numbers=[3,24,1997]
empty=[]
print(cheeses,numbers,empty) 

print(numbers[1])
#Accessing element/item in list
numbers[1]=23
print(numbers)
#The in operator also works on lists.
print('Edem' in cheeses)
print('Cherrie' in cheeses)

#Traversing in lists
number=[1,2,3,4,5,6,7,8,9]
for i in range(len(number)):
    number[i]=number[i]*2
print(number)

#List operations

a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
print(a*3)

#The slice operator also works on lists:
t=['a','b','c','d','e','f','g','h','i','j']
print(t[:5])
#The slice operator also works on lists:
t[1:4]=['x','y','z']
print(t)
#List methods
#append adds a new element to the end of a list:
t.append('B')
print(t)
#extend takes a list as an argument and appends all of the elements:
t1=['a','b','c']
t2=['d','e']
t1.extend(t2)
print(t1)
#sort arranges the elements of the list from low to high:
t=['j','f','d','c','i','b','h','g','e','a']
t.sort()
print(t)
#Deleting elements
B=[1,2,3]
x=B.pop(2)
print(B)
print(x)
#If you don’t need the removed value, you can use the del operator:
del B[1]
print(B)
h=[1,2,3,4,5,6]
h.remove(2)
print(h)

#Lists and functions
Numbers=[11,8,1995,3,24,1997]
print(len(Numbers))
print(max(Numbers))
print(min(Numbers))
print(sum(Numbers))
print(sum(Numbers)/(len(Numbers)))


#the program to compute an average without a list:
total=0
count=0
while (True):
    inp=input('Enter a number: ')
    if inp== 'done' : break
    value=float(inp)
    total=total+value
    count=count+1
average=total/count
print('Average: ',average)

#We could simply remember each number as the user entered it and use built-in functions to compute the sum and count at the end.
num=list()
while (True):
    inp=input('Enter a number: ')
    if inp=='done' : break
    value=float(inp)
    num.append(value)
average=(sum(num))/(len(num))
print(average)

#Lists and strings
s='spam'
t=list(s)
print(t)
#You can call split with an optional argument called a delimiter
s='spam-spam-spam'
delimiter='m'
print(s.split(delimiter))

#join is the inverse of split.
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
print(delimiter.join(t))

#Parsin
fhand = open('Romeo.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('Oh'): continue
    words = line.split()
    print(words[2])

#List arguments
def delete_head(t):
    del t[0]

letters=['a','b','c']
delete_head(letters)
print(letters)

#EXERCISE 1
def chop(lst):
    del lst[0]
    del lst[-1]
def middle(lst):
    
    del new[-1]
mylist=[1,2,3,4,5,6]
mylist2=[1,2,3,4,5,6]
chop_list=chop(mylist)
print(mylist)
print(chop_list)
middle_list=(len(mylist2))//2
print(mylist2)
print((mylist2)[middle_list])

#Exercise 2

mylist=[]
fhand=open('romeo.txt')
for line in fhand:
    words=line.split()
    for word in words:
        if word in mylist:
            continue
        mylist.append(word)
print(sorted(mylist))

#Exercise 3

fhand=open('mbox-short.txt')
count=0
for line in fhand:
    words=line.split()
    if len(words)>3 or words[0]!='From':
        continue 
    print(words[1])
    count+=1
print('there were %d lines in the file with From as the first word' %count)

#Exercise 4

my_list=[]
while True:
    number=0.0
    inp_number=input('Enter a number: ')
    if inp_number=='done': break
    try:
        number=float(inp_number)
    except ValueError:
        print('invalid input')
    my_list.append(inp_number)
print('Maximum: ', max(my_list))
print('Minimum: ', min(my_list))


