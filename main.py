# coding=utf-8
import random
import sys

al = " §±!@#$%^&*()_+-={[]}\?/.>,<~`;:\'|AqQBCDEFGHIJKLMNOPRSTUVWabcdefghijklmnoprstuvwxyz0123456789\n\""
allist = []
for i in al:
    allist.append(i)
alphasize = len(allist)

print("\nThe cipher mashine is able to encode and decode the messages.\n")
encryptordecrypt = input("Do you want to encrypt your message or to decrypt the code? Type Q to Quit E/D/Q")
while encryptordecrypt.upper() not in ("E","D","Q"):
    print("Input was not recognised!!! ")
    encryptordecrypt = input("\nDo you want to encrypt your message or to decrypt the code? E/D ")

if encryptordecrypt.upper() == "Q":
    print("\nExiting...")
    exit()
elif encryptordecrypt.upper() == "E":

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
    open("Encrypted_message.txt", "w").close()
    Encryptedmessage = open("Encrypted_message.txt","w")

    open("key.txt", "w").close()
    keyfile = open("key.txt","w")

    
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
    if whattodo.upper() == "FILE":
        openedfile.close()
    # for i in t2e:
    #     key.append(random.randrange(0,len(allist)+1))
    for i in key:
        i = str(i)
        keyfile.write(i)
        keyfile.write("\n")

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
        print("Receiver with the same program and with the KEY will be able to decode your message")
        print("\nRun cipher mashine as DECODER to decode the code")
        print("\nRun cipher mashine as ENCODER to encode other message")
        print("\nExiting")
        keyfile.close()

else:

    open("Output.txt", "w").close()
    outputfile = open("Output.txt","w")

    # decryptmessage = input("Do you want to decrypt your message? Y/N ")
    # while decryptmessage.upper() not in ("Y","N"):
    #     decryptmessage = input("Invalid input. Do you want to decrypt your message? Y/N ")
    # if decryptmessage.upper() == "N":
    #     print("\nExiting....\n")
    #     exit()
    # else:
    if open("key.txt","r").read() == "":
        print("\n\n\n\n\nYou have not saved your key!!!! Your message is lost forever\n\n\n")
        print("\nExiting....\n")
        exit()
    else:
        print("\n\nDecrycpting\n\n\n\n")
        print("Please wait...\n\n")

    t2deindexed = [] 
    for c in open("encrypted_message.txt","r").read():
        t2deindexed.append(allist.index(c))
    # print("t2dindexed",t2deindexed)

    dencryptedindexes = []
    readkey = open("key.txt","r").readlines()
    # print("readkey",readkey)
    keylist = []
    for i in readkey:
        i = int(i)
        keylist.append(i)
    # print("key",keylist)
    withkey = zip(t2deindexed,keylist)
    for a,b in  withkey:
        dencryptedindexes.append(a+b-len(allist))

    dencriptedtext = []
    for i in dencryptedindexes:
        dencriptedtext.append(allist[i])
    dencriptedtext2 = "".join(dencriptedtext)
    # print("dencriptedtext2",dencriptedtext2)
    print("Congrats. Your message was decrypted. Find the results in program files")
    outputfile.write(dencriptedtext2)
    
    outputfile.close()