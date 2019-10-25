# 09f Final Project
## Cipher: Encode and Decode Your Secret Messages

Program encodes and decodes messages using random shift method.

_How does it work?_

Cipher includes initial set of symbols and random indexes for each symbol in the message that is chosen to be encrypted.

**For Example:**

Initial set of symbols: "abcdefghijklmnoprstuw"; 
Text for encryption: "home"; 
Randomly generated key: 1234; 
Decrypted text: "gmja" (h - 1 = g, o - 2 = m, m -3 = j, e - 4 = a)

When receiver knows the initial set of symbols and have the randomly generated key he/she can easily decript the code.


All usual symbols from the keybord can be used for encryption.

**HOW TO RUN A PROGARM?**

To start a prograrm run _main.py_ in terminal.

You will be able to select how you would like to input the message for encryption. Two methods are available:
* to input the message directly,
* to use the message from the file "texttoencrypt.txt"

After Encrypting the message, program will ask if you want to:
* save the key and initial indexes of symbols needed to decrypt the code.
* decrypt the message using the program 

**STUCTURE OF FILES**

* texttoencrypt.txt - file, that consist the message, you can chose to be encrypted
* Encrypted_message.txt - file, where encrypted message will be saved after successful run of the progarm 
* key.txt - file, where key, needed to decrypt the encrypted file will be saved adter successful run of the progam 
* Output - file, that gives back the initial message, that was encrypted.