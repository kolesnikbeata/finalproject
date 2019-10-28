# coding=utf-8
import random
import sys

print("\nEncryption machine is starting...")
print("\nSelect the option for text for encryption input:")
whattodo = str(input("\nDo you want to encrypt text from file or to write your own text into cmnd line? (File/CMND/Q - quit) "))

while whattodo.upper() not in ("Q","FILE","CMND"):
    print("Input was not recognised!!! ")
    whattodo = input("\nDo you want to encrypt text from file or to write your own text into cmnd line? (File/CMND/Q - quit) ")

if whattodo.upper() == "FILE":
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
alphasize = len(allist)
print("\nPlease wait...")
print("\nEncryption machine is working on ciphering your text...")

key = []
for i in t2e:
    key.append(random.randrange(0,len(allist)+1))

t2eindexed = [] 
for c in t2e:
    t2eindexed.append(allist.index(c))

encryptedindexes = []
withkey = zip(t2eindexed,key)
for a,b in  withkey:
    encryptedindexes.append(a-b)

encriptedtext = []
for i in encryptedindexes:
    encriptedtext.append(allist[i])
encriptedtext2 = ''.join(encriptedtext)
Encryptedmessage.write(encriptedtext2)
print("""
""")
print("**************************************************************************")
print("Your text was encrypted. Find encrypted text in encrypted_message.txt file")
print("**************************************************************************")
print("""
""")
for i in t2e:
    key.append(random.randrange(0,len(allist)+1))
for i in key:
    i = str(i)
    keyfile.write(i)

savekey = input(" Do you want to save the key? Y/N ")
while savekey.upper() not in ("Y","N"):
    savekey = input("Invalid input. Do you want to save the key? Y/N ")
if savekey.upper() == "N":
    keyfile.close()
    open("key.txt", "w").close()
    print("---------!!!!!!!!--------")
    print("ALERT - KEY WAS NOT SAVED")
    print("---------!!!!!!!!--------")
else:
    print("**************************")
    print("KEY WAS SUCCESSFULLY SAVED")
    print("**************************")
decryptmessage = input("Do you want to decrypt your message? Y/N ")
while decryptmessage.upper() not in ("Y","N"):
    decryptmessage = input("Invalid input. Do you want to save the key? Y/N ")
if decryptmessage.upper() == "N":
    print("\nExiting....\n")
    exit()
else:
    if savekey.upper() == "N":
        print("\n\n\n\n\nYou have not saved your key!!!! Your message is lost forever\n\n\n")
        print("\nExiting....\n")
        exit()
    else:
        print("\n\nDecrycpting\n\n\n\n")
        print("Please wait...\n\n")

t2deindexed = [] 
for c in encriptedtext2:
    t2deindexed.append(allist.index(c))

dencryptedindexes = []
withkey = zip(t2deindexed,key)
for a,b in  withkey:
    dencryptedindexes.append(a+b-len(allist))

dencriptedtext = []
for i in dencryptedindexes:
    dencriptedtext.append(allist[i])
dencriptedtext2 = "".join(dencriptedtext)
print("dencriptedtext2",dencriptedtext2)
print("Congrats. Your message was decrypted. Find the results in program files")
outputfile.write(dencriptedtext2)
if whattodo.upper() == "FILE":
    openedfile.close()
outputfile.close()