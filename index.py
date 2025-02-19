import random
import string

char = " "+ string.punctuation + string.digits +string.ascii_letters
chars = list(char)
key=chars.copy()

random.shuffle(key)


#Encrpyt
plain_text = input("Enter the message to encrypt: ")
cipher_text = " "

for letter in plain_text:
    index = chars.index(letter)
    cipher_text +=key[index]
print(f"Original Message {plain_text}")
print(f"Encypted Message {cipher_text}")



#decrpyt
cipher_text  = input("Enter the message to decrypt: ")
plain_text = " "

for letter in cipher_text:
    index = chars.index(letter)
    plain_text +=key[index]
print(f"Original Message {cipher_text}")
print(f"Encypted Message {plain_text}")