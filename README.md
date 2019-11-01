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

**HOW TO RUN A PROGRAM?**

To start a prograrm run _main.py_ in terminal.

Machine can encode and decode messages. You need to select which action you would like to do.

If you want to encode a message you will be able to select the method of input for encryption. Two methods are available:
* to input the message directly,
* to use the message from the file "texttoencrypt.txt"

After Encrypting the message, program will ask if you want to:
* save the key and initial indexes of symbols needed to decrypt the code. Remember - without key saved - it will be impossible to decode the message.

If you want to decode your message - key.txt and encrypted message need to be saved.


**STUCTURE OF FILES**

* texttoencrypt.txt - file, that consist the message, you can chose to be encrypted
* encrypted_message.txt - file, where encrypted message will be saved after successful run of the progarm 
* key.txt - file, where key, needed to decrypt the encrypted file will be saved adter successful run of the progam 
* output - file, that gives back the initial message, that was encrypted.