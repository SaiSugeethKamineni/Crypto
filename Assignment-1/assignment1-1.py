#!/usr/local/bin/python3
# Encoding: UTF-8
# Style guide: pep8
"""
Created: 24 January 2019
Author: Sai Sugeeth Kamineni
"""


def caesar_encrypt(key):
    file = open("process.txt", 'r')
    cleartext = file.read()
    ciphertext = ''
    for i in cleartext:
        asciiVal = ord(i)
        if (65 <= asciiVal <= 90) or (97 <= asciiVal <= 122):
            if i.islower():
                ciphertext += chr((asciiVal - 97 + key) % 26 + 97)
            else:
                ciphertext += chr((asciiVal - 65 + key) % 26 + 65)
        else:
            ciphertext += i
    file.close()
    file = open("ciphertext.txt", 'w+')
    file.write(ciphertext)
    file.close()
    print("\nCipher text:", ciphertext)
    print("Note: The ciphertext is stored in the file 'ciphertext.txt'.")


def vigenere_encrypt(key):
    file = open("process.txt", 'r')
    cleartext = file.read()
    ciphertext = ''
    count = 0
    keyMod = len(key) + 1
    for i in cleartext:
        subKey = key[count % keyMod]
        asciiVal = ord(i)
        asciiValSK = ord(subKey)
        if (65 <= asciiVal <= 90) or (97 <= asciiVal <= 122):
            if i.islower():
                ciphertext += chr((asciiVal - 97 + asciiValSK) % 26 + 97)
            else:
                ciphertext += chr((asciiVal - 65 + asciiValSK) % 26 + 65)
            count += 1
        else:
            ciphertext += i
    file.close()
    file = open("ciphertext.txt", 'w+')
    file.write(ciphertext)
    file.close()
    print("\nCipher text:", ciphertext)
    print("Note: The ciphertext is stored in the file 'ciphertext.txt'.")


def caesar_decrypt(key):
    file = open("process.txt", 'r')
    ciphertext = file.read()
    cleartext = ''
    key = 26 - key
    for i in ciphertext:
        asciiVal = ord(i)
        if (65 <= asciiVal <= 90) or (97 <= asciiVal <= 122):
            if i.islower():
                cleartext += chr((asciiVal - 97 + key) % 26 + 97)
            else:
                cleartext += chr((asciiVal - 65 + key) % 26 + 65)
        else:
            cleartext += i
    file.close()
    file = open("cleartext.txt", 'w+')
    file.write(cleartext)
    file.close()
    print("\nClear text:", cleartext)
    print("Note: The cleartext is stored in the file 'cleartext.txt'.")


def vigenere_decrypt(key):
    file = open("process.txt", 'r')
    ciphertext = file.read()
    cleartext = ''
    count = 0
    keyMod = len(key) + 1
    for i in ciphertext:
        subKey = key[count % keyMod]
        asciiVal = ord(i)
        asciiValSK = ord(subKey)
        asciiValSK = 26 - asciiValSK
        if (65 <= asciiVal <= 90) or (97 <= asciiVal <= 122):
            if i.islower():
                cleartext += chr((asciiVal - 97 + asciiValSK) % 26 + 97)
            else:
                cleartext += chr((asciiVal - 65 + asciiValSK) % 26 + 65)
            count += 1
        else:
            cleartext += i
    file.close()
    file = open("cleartext.txt", 'w+')
    file.write(cleartext)
    file.close()
    print("\nClear text:", cleartext)
    print("Note: The cleartext is stored in the file 'cleartext.txt'.")


def main_prog():
    routine = input(
        "> Select the type of cipher:\n1. Caesar\n2. Vigenere\nEnter choice: ")
    process = input(
        "> Select the required process:\n1. Encrypt\n2. Decrypt\nEnter choice: ")
    if routine == '1' or routine.lower() == 'caesar':
        key = input("> Enter the key: ")
        if key.isdigit():
            intkey = int(key)
            if process == '1' or process.lower() == 'encrypt':
                # caesar_encrypt
                caesar_encrypt(intkey)
            elif process == '2' or process.lower() == 'decrypt':
                # caesar_decrypt
                caesar_decrypt(intkey)
            else:
                print("Enter valid input for process selection.\n")
        else:
            print("Enter a valid key (Any Whole Number).")
    elif routine == '2' or routine.lower() == 'vigenere':
        key = input("> Enter the key: ")
        if key.isalpha():
            lkey = key.lower()
            if process == '1' or process.lower() == 'encrypt':
                # vigenere_encrypt
                vigenere_encrypt(lkey)
            elif process == '2' or process.lower() == 'decrypt':
                # vigenere_decrypt
                vigenere_decrypt(lkey)
            else:
                print("Enter valid input for process selection.\n")
        else:
            print("Enter a valid key (Any word).")
    else:
        print("Enter valid input for cipher type selection.\n")


if __name__ == '__main__':
    main_prog()
