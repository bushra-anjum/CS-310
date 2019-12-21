#Examples Chapter 9
#1
eng2sp=dict()
eng2sp['one']='uno'
print(eng2sp)
#2
Bushra2Chochoo=dict()
Bushra2Chochoo={'Bushra':70,'Busho':1,'Bushi':2,'Bush':50,'Chipkali':2,'Chocha':5,'chochoo':5}
print(Bushra2Chochoo)
#3
print(Bushra2Chochoo['Bushi'])
#4
print('Chocha'in Bushra2Chochoo)
#5
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
#6
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
#7
word = 'brontosaurus'
d=dict()
for c in word:
    d[c]=d.get(c,0)+1
print(d)

#Dictionaries and files

#8
fname=input('Enter File Name: ')
try:
    fhand=open(fname)
except:
    print('File cannot be found',fname)
    exit()
counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1
print(counts)

#Looping in Dictionaries

#9
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    print(key,counts[key])

#10
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key]>10:
        print(key)
#11
import string
fname=input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print('No such file exists in that repositry')
    exit()
counts=dict()
for line in fhand:
    line=line.rstrip()
    line=line.translate(line.maketrans('', '',string.punctuation))
    line=line.lower()
    words=line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1
print (counts)

#Exercise 2
dictionary_days=dict()
filename=input('Enter File Name: ')
try:
    filehand=open(filename)
except:
    print('Such file Does not exist in this directory', filename)
    exit()
for line in filehand:
    words=line.split()
    if len(words)<3 or words[0]!='From': continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]]=1
        else:
            dictionary_days[words[2]]+=1
print(dictionary_days)

#Exercise 3

dictionary_days=dict()
filename=input('Enter File Name: ')
try:
    filehand=open(filename)
except:
    print('Such file Does not exist in this directory', filename)
    exit()
for line in filehand:
    words=line.split()
    if len(words)<3 or words[0]!='From': continue
    else:
        if words[1] not in dictionary_days:
            dictionary_days[words[1]]=1
        else:
            dictionary_days[words[1]]+=1
print(dictionary_days)

#Exercise 4

maximum=0
maximum_addresses=''
dictionary_addresses=dict()
filename=input('Enter File Name: ')
try:
    filehand=open(filename)
except:
    print('Such file Does not exist in this directory', filename)
    exit()
for line in filehand:
    words=line.split()
    if len(words)<2 or words[0]!='From': continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]]=1
        else:
            dictionary_addresses[words[1]]+=1
for address in dictionary_addresses:
    if dictionary_addresses[address]>maximum:
        maximum=dictionary_addresses[address]
        maximum_addresses=address
print(maximum_addresses,maximum)

#Exercise 5

dictionary_domains=dict()
fname=input('Enter the File name: ')
try:
    fhand=open(fname)
except:
    print('File does not exist',fname)
for line in fhand:
    words=line.split()
    if len(words)<2 or words[0]!='From': continue
    else:
        atpos=words[1].find('@')
        domain=words[1][atpos+1:]
        if domain not in dictionary_domains:
            dictionary_domains[domain]=1
        else:
            dictionary_domains[domain]+=1
print(dictionary_domains)
