# Encryption Program - prompts user for a file in directory, checks if file is valid
# and then creates an encrypted version of the file.
#
#
# By Team 16
# 
#
########################

import os
import shutil

from cryptography.fernet import Fernet

#files = [] 

# User Interface

print(" Welcome to the file encryption program.\n\n") 

print("Here is your directory path:\n\n") 

print(os.getcwd()) # Get CWD

print("Here is a list of files in your directory\n")


# Encryption function - encrypts given file and stores it in new file with .crypt extension

def encrypt_file(file):

    key = Fernet.generate_key() 

    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    fernet = Fernet(key)

    with open(file, 'rb') as target:
        original = target.read()

    encrypted = fernet.encrypt(original)

    new_file = open(file + ".crypt", "x")

    with open(file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)



for file in os.listdir(): # Get all files in CWD
    print(file)


file_name = input("\nPlease enter a file to encrypt: ")


if file_name in os.listdir():
    print("\nFile is in this directory. Encrypting processing...")
    encrypt_file(file_name)

    print("File name {file} has been encrypted in a new file called {file}.crypt.\n".format(file = file_name)) 
    print("Your original file has been preserved. Goodbye.") 

else: 
    print("File not in directory. Exiting Program..." )




