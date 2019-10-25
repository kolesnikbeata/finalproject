# coding=utf-8
import random
import sys

print("\nEncryption machine is starting...")
print("\nSelect the option for text for encryption input:")



whattodo = str(input("\nDo you want to encrypt text from file or to write your own text into cmnd line? (File/CMND/Q - quit) "))
# print(whattodo)

while whattodo.upper() not in ("Q","FILE","CMND"):
    print("Input was not recognised!!! ")
    whattodo = input("\nDo you want to encrypt text from file or to write your own text into cmnd line? (File/CMND/Q - quit) ")


if whattodo.upper() == "FILE":
    # import text from file
    filename = "texttoencrypt.txt"
    openedfile = open(filename, "r")
    t2e = openedfile.read()
elif whattodo.upper() == "CMND":
    t2e = input("\nInput the text you want to be encrypted: ") 
else: 
    print("\nExiting....\n")
    exit()

open("Output.txt", "w").close()
outputfile = open("Output.txt","w")

open("Encrypted_message.txt", "w").close()
Encryptedmessage = open("Encrypted_message.txt","w")

open("key.txt", "w").close()
keyfile = open("key.txt","w")

al = " §±!@#$%^&*()_+-={[]}\?/.>,<~`;:\'|AqQBCDEFGHIJKLMNOPRSTUVWabcdefghijklmnoprstuvwxyz0123456789\n\""
allist = []
for i in al:
    allist.append(i)
# print(allist)
alphasize = len(allist)
# print(alphasize)

print("\nPlease wait...")
print("\nEncryption machine is working on ciphering your text...")

# print("tekstas kodavimui: ",t2e)
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
# print("encriptedtext2",encriptedtext2)
Encryptedmessage.write(encriptedtext2)
print("""
""")
print("**************************************************************************")
print("Your text was encrypted. Find encrypted text in Encrypted_message.txt file")
print("**************************************************************************")

print("""
""")






for i in t2e:
    key.append(random.randrange(0,len(allist)+1))
# print("key", key)
for i in key:
    i = str(i)
    keyfile.write(i)

# def alphacalculator(list,number):


savekey = input(" Do you want to save the key? Y/N")
while savekey.upper() not in ("Y","N"):
    savekey = input("Invalid input. Do you want to save the key? Y/N ")
if savekey.upper() == "N":
    keyfile.close()
    open("key.txt", "w").close()



# DECRIPTION

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