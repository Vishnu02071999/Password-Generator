from random import *
Alphabets=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Numbers=["1","2","3","4","5","6","7","8","9","0"]
Symbols=["!","@","#","$","%","^","&","*","(",")","+","_","-","=","{","}","[","]",">","<","\"" "~"]
newA="".join(choice(Alphabets) for x in range(4))
newN="".join(choice(Numbers) for x in range(4))
newS="".join(choice(Symbols) for x in range(3))
TEMP=[]
TEMP.append(newA)
TEMP.append(newN)
TEMP.append(newS)
shuffle(TEMP)
print("Your Password is : ")
print("".join(TEMP))
