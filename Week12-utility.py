# https://github.com/hbenjet/CSCI_102_demo.git 
# Hannah Benjet
# CSCI 102
# Week 12

def PrintOutPut(string):
    return print("OUTPUT ",string)

def LoadFile(filename):
    file=open(filename,'r')
    return file

def UpdateString(word, letter, int:x):
    word=list(word)
    word[x]=letter
    word.pop()
    return word

def FindWordCount(filename, word):
    file=(filename,r)
    file=file.readlines()
    i=0
    file=''.join(file)
    file=file.lower()
    while i < len(file):
        if file[i] == "," or file[i] == "-" or file[i]==".":
        file[i]=''
        i+=1
    file=''.join(file)
    file=file.split()   
    i=0
    while i < len(file):
        if word == dec_ind[i]:
            x+=1
        i+=1
return print(word,"is repeated", x, "times")

def ScoreFinder(name, list:names, list:scores):
    i=0
    while i < len(names):
        if name == names[i]:
            x=i
        i+=1
    score=scores[x]
    return print(name,score)

def Union(list:list1, lis:list2):
    i=0
    while i < len(list2):
        if list2[i] not in list1:
            list1.append(list2[i])
        i+=1
    return list1

def Intersection(list:list1,list:list2):
    i=0
    list3=[]
    while i < len(list1):
        if list1[i] in list2:
            list3.append(list1[i])
        i+=1
    return list3

def NotIn(list:list1,list:list2):
    list3=[]
    i=0
    while i < len(list1):
        if list1[i] not in list2:
            list3.append(list1[i])
        i+=1
    i=0
    while i < len(list2):
        if list2[i] not in list1:
            list3.append(list2[i])
        
    
    
