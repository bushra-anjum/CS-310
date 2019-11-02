#Examples of Chapter 3
x=5
if x<10:
    print('smaller')
if x>20:
    print('bigger')
print('Finish')


x=3
if x<10:
    print('Small')

print('Done')


x=9
if x%2==0:
    print('even')
else:
    print('odd')


x=y=36
if x<y:
    print('x is less than y')
elif x>y:
    print('x is greater than y')
else:
    print('x and y are equal')


choice='c'
if choice=='a':
    print('bad guess')
elif choice=='b':
    print('good guess')
elif choice=='c':
    print('close,but not correct')


x=36
y=24
if x==y:
    print('x and y are equal')
else:
    if x<y:
        print('x is less than y')
    else:
        print('x is greater than y')


x=4
if 0<x:
    if x<10:
        print('x is a positive single digit number')



prompt="what is the air velocity of an unladen swallow?\n"
speed=input(prompt)



inp=input('Enter fahrenheit Temperature: ')
fahr=float(inp)
cel=(fahr-32.0)*5.0/9.0
print(cel)



inp=input('Enter fahrenheit Temperature: ')
try:
    fahr=float(inp)
    cel=(fahr-32.0)*5.0/9.0
    print(cel)
except:
    print('please enter a number')



x=6
y=2
if x>=2 and (x/y)>2:
    print('True')

#Exercise Of Chapter 3
#Exercise 1: Rewrite your pay computation to give the employee 1.5
#times the hourly rate for hours worked above 40 hours.

hours=input("Enter hours")
hours=int(hours)
rate=input("Enter rate")
rate=int(rate)
if (hours>0):
    if(hours<=40):
        pay=hours*rate
        print(pay)
    else:
        pay=hours*rate+(hours-40)*15
        print(pay)
else:
    print("program done")
    
#Exercise 2: Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program. The following shows two executions of the
#program:

hours=input('Enter hours')
rate=input('Enter rate')
try:
    hours=int(hours)
    rate=int(rate)
except:
    hours= -1
if(hours>40):
    pay=rate*hours+(hours-40)*15
    print(pay)
elif (hours>0):
    pay=hours*10
    print(pay)
else:
    print('Error,please enter numeric input')

#Exercise 3: Write a program to prompt for a score between 0.0 and
#1.0. If the score is out of range, print an error message. If the score is
#between 0.0 and 1.0, print a grade

score = input("Enter score between 0.0 and 1.0: ")
score=float(score)
if score>1.0 or score<0.0 :
	print ("error")
elif score>=0.9 :
  	print ('A')
elif score>=0.8 :
    print ('B')
elif score>=0.7 :
    print ('C')
elif score>=0.6 :
    print ('D')
else :
    print ('F')


#Examples of Chapter 4

Letter = ('Hello worls')
print(max(Letter))
print(min(Letter))


Number = ('Hello Cruel')
print(len(Number))

convert = ('32')
print(int(convert))

convert_float=32.0
print(int(convert_float))

into_string=345
print(str(into_string))


import math
signal_power=23
noise_power=12
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print(decibels)


import math
radians = 0.7
height = math.sin(radians)
print(height)


degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(radians)


import random
for i in range(10):
    x = random.random()
print(x)

from random import randint
print("Printing random integer ", randint(0, 9))


import random
list  = [111,222,333,444,555]
print("random.choice() to select random item from list - ", random.choice(list))
print("random.choice() to select random item from list - ", random.choice(list))


def print_lyrics():
    print("Dekha Hazaron Daffa apko phir bekaraari kesi hai")
    print('Sanbhaly sanbhalta nahe ye dil,kuch ap main bat aisi hai')
print(print_lyrics())


def print_lyrics():
    print("Dekha Hazaron Daffa apko phir bekaraari kesi hai")
    print('Sanbhaly sanbhalta nahe ye dil,kuch ap main bat aisi hai')
def repeat_lyrics():
    print("Dekha Hazaron Daffa apko phir bekaraari kesi hai")
    print('Sanbhaly sanbhalta nahe ye dil,kuch ap main bat aisi hai')
print(print_lyrics())
print(repeat_lyrics())


def print_twice(bruce):
    print(bruce)
    print(bruce)
print(print_twice('Spam'))
import math
print(print_twice(math.pi))
michael = 'Eric, the half a bee.'
print(print_twice(michael))


def addtwo(a, b):
    added = a + b
return added
x = addtwo(3, 5)
print(x)

#Exercise Chapter 4
#Exercise 6: Rewrite your pay computation with time-and-a-half for over-
#time and create a function called computepay which takes two parameters
#(hours and rate).
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

hours=0
rate=0
def computepay(hours,rate):
    print('in computepay',hours,rate)
    hours=int(hours)
    input('Enter hours: ')
    rate=int(rate)
    input('Enter rate: ')
    if(hours<=40):
        computepay=hours*rate+(hours-40)*15
    else:
        computepay=hours*rate
    
    print('returning ',)
    return computepay
    
x=computepay(hours,rate)
print(x)

#Exercise 7: Rewrite the grade program from the previous chapter using
#a function called computegrade that takes a score as its parameter and
#returns a grade as a string.

score=input("Please type a score between 0.0 and 1.0:")
try:
  def computegrade():
    if float(score) >= 0.9 and float(score) <= 1.0:
      print("A")
    elif float(score) >= 0.8 and float(score) <= 0.9:
      print("B")
    elif float(score) >= 0.7 and float(score) <= 0.8:
      print("C")
    elif float(score) >= 0.6 and float(score) <= 0.7:
      print("D")
    elif float(score) > 0 and float(score) <= 0.6:
      print("F")
    else:
      print("Bad score.  Please run the program again.")  
  computegrade()
except: 
    print("Bad score.  Please run the program again.")