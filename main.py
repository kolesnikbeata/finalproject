# coding=utf-8
import random


# import text from file
filename = "texttoencrypt.txt"
openedfile = open(filename, "r")
open("Output.txt", "w").close()
outputfile = open("Output.txt","w")





al = " §±!@#$%^&*()_+-={[]}\?/.>,<~`;:\'|ABCDEFGHIJKLMNOPRSTUVWabcdefghijklmnoprstuvwxyz0123456789\n\""
allist = []
for i in al:
    allist.append(i)
# print(allist)
alphasize = len(allist)
# print(alphasize)


# t2e = "bandymas vienas"
# t2e = "as esu kulverstukas o tu esi kulverstukas2345"
# t2e = """as esu kulverstukas o tu esi kulverstukas2345
#         new line kabutes\"\" """

t2e = openedfile.read()

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
openedfile.close()
outputfile.close()