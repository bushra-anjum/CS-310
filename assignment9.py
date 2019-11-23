print("Chapter 5:")
print(" ")
print("Q#40:")
if ((1==1)or(2==2)or(3==3)):
	print("Good")
else:
	print("Bad")

print(" ")
print("Q#41:")
x=1
y=2
z=3
if ((x==y)or(y==z)or(z==2)):
	print("YES")
else:
	print("NO")

print(" ")
print("Q#42:")
if (1==2):
	print("Hello")
elif(2==1):
	cout("World")

print(" ")
print("Q#43:")
ang=input("Enter Angle:")
angle=int(ang)
if(angle>5):
	angle=angle+5
elif(angle>2):
	angle=angle+10
else:
	angle=angle+15
print(angle)

print(" ")
print("Q#44:")
p=10
q=3
r=-2
if (p+ q)<14 and r< (q-3):
	print (r)
else:
	print (p)

print(" ")
print("Q#45:")
if (('A'=='A')and('B'=='B')and('C'=='c')):
	print("Equal")
else:
	print("Not Equal")

print(" ")
print("Q#46:")
if(9<5):
	print("x")
elif(5==6):
	print("#")
else:
	print("@")

print(" ")
print("Q#47:")
aa=input("Enter a: ")
a=int(aa)
bb=input("Enter b: ")
b=int(bb)
cc=input("Enter c: ")
c=int(cc)
if(a>b and a>c):
	m=a
elif (b>c):
	m=b
else:
	m=c
print(m)

print(" ")
print("Q#48:")
aa=input("Enter a: ")
a=int(aa)
bb=input("Enter b: ")
b=int(bb)
cc=input("Enter c: ")
c=int(cc)
dd=input("Enter d: ")
d=int(dd)
if (a>b or a>c and c!=d):
	m=a
elif(b>d):
	m=b
else:
	m=c
print(m)


print("_____")
print("Chapter 6:")
print(" ")
print("Q#1: ")
n=1
print("a	","b")
while (n>0) and (n<=5):
	print(n,"	",6-n)
	n=n+1


print(" ")
print("Q#2:")
n=1
sum=0
print("num	","sum")
while (n>0) and (n<=5):
	sum=sum+n
	print(n,"	",sum)
	n=n+1


print(" ")
print("Q#3:")
n=4
sum=1
while n<=100:
	sum=sum+(1/n)
	n=n+4
print (sum)


print(" ")
print("Q#4:")
for c in range(65, 91):
        print(chr(c), end = " ");


print(" ")
print("Q#5:")
sum=0
smallest = None
largest= None
for value in[20,21,22,30,40]:
	if smallest is None or value < smallest:
		smallest = value
	if largest is None or value> largest:
		largest=value
	sum=sum+value
print('Smallest:', smallest)
print('Largest: ', largest)
average=sum/5
print(average)
