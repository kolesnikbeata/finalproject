# coding=utf-8
import random
import sys

print("Encryption machine is starting...")
print("Select the option for text for encryption input:")



whattodo = str(input("Do you want to encrypt text from file or to write your own text into cmnd line? (File/CMND/Q - quit) "))
print(whattodo)

while whattodo.upper() not in ("Q","FILE","CMND"):
    print("Input was not recognised!!! ")
    whattodo = input("Do you want to encrypt text from file or to write your own text into cmnd line? (File/CMND/Q - quit) ")


if whattodo.upper() == "FILE":
    # import text from file
    filename = "texttoencrypt.txt"
    openedfile = open(filename, "r")
    t2e = openedfile.read()
elif whattodo.upper() == "CMND":
    t2e = input("Input the text you want to be encrypted: ") 
else: 
    print("Exiting....")
    exit()

open("Output.txt", "w").close()
outputfile = open("Output.txt","w")

al = " §±!@#$%^&*()_+-={[]}\?/.>,<~`;:\'|ABCDEFGHIJKLMNOPRSTUVWabcdefghijklmnoprstuvwxyz0123456789\n\""
allist = []
for i in al:
    allist.append(i)
# print(allist)
alphasize = len(allist)
# print(alphasize)


print("tekstas kodavimui: ",t2e)
key = []
for i in t2e:
    key.append(random.randrange(0,len(allist)+1))
# print("key", key)

# def alphacalculator(list,number):

t2eindexed = [] 
for c in t2e:
    t2eindexed.append(allist.index(c))
# print("t2eindexed", t2eindexed)


encryptedindexes = []
withkey = zip(t2eindexed,key)
for a,b in  withkey:
    encryptedindexes.append(a-b)
# print("indexes for cypher", encryptedindexes)

encriptedtext = []
for i in encryptedindexes:
    encriptedtext.append(allist[i])

for b,element in enumerate(encriptedtext):
    if element == ' ':
        # print("found")
        encriptedtext[b] = "kodiniszodis"

# print("encryptedtext", encriptedtext)
encriptedtext2 = ' '.join(encriptedtext)

encriptedtext2 = encriptedtext2.replace(" ","").replace("kodiniszodis"," ")
print("encriptedtext2",encriptedtext2)


# DECRIPTION

for i in t2e:
    key.append(random.randrange(0,len(allist)+1))
# print("key", key)

# def alphacalculator(list,number):

t2deindexed = [] 
for c in encriptedtext2:
    t2deindexed.append(allist.index(c))
# print("t2deindexed", t2deindexed)


dencryptedindexes = []
withkey = zip(t2deindexed,key)
for a,b in  withkey:
    dencryptedindexes.append(a+b-len(allist))
# print("indexes for dcypher", dencryptedindexes)

dencriptedtext = []
for i in dencryptedindexes:
    dencriptedtext.append(allist[i])

for b,element in enumerate(dencriptedtext):
    if element == ' ':
        # print("found")
        dencriptedtext[b] = "kodiniszodis"

# print("dencryptedtext", dencriptedtext)
dencriptedtext2 = ' '.join(dencriptedtext)

dencriptedtext2 = dencriptedtext2.replace(" ","").replace("kodiniszodis"," ")
print("dencriptedtext2",dencriptedtext2)

outputfile.write(dencriptedtext2)

if whattodo.upper() == "FILE":
    openedfile.close()

outputfile.close()