#!/usr/local/bin/python3
# Encoding: UTF-8
# Style guide: pep8
"""
Created: 29 January 2019
Author: Sai Sugeeth Kamineni
"""

from collections import Counter

WORDS = ['in', 'an', 'the', 'of', 'and', 'for', 'to',
         'at', 'has', 'have', 'that', 'which', 'this', 'and']
RANK = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C',
        'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']


def caesar_decrypt_analytical():
    file = open("caesar.txt", 'r')
    ciphertext = file.read()
    file.close()
    words = WORDS
    rank = RANK
    freq = Counter(ciphertext)
    maxfreq = max(freq, key=freq.get)
    asciiValMax = ord(maxfreq.lower())
    for i in range(26):
        select = rank[i]
        asciiValSelect = ord(select.lower())
        key = asciiValSelect - asciiValMax
        cleartext = ''
        for j in ciphertext:
            asciiVal = ord(j)
            if j.islower():
                cleartext += chr((asciiVal - 97 + key) % 26 + 97)
            else:
                cleartext += chr((asciiVal - 65 + key) % 26 + 65)
        """
        print("\n->Possible clear text:", cleartext+"\n")
        conf = input(">Does this clear text make sense (apart from spaces)? :\n1. Yes\n2. No\nEnter the choice: ")
        if conf == '1' or conf.lower() == "yes":
            print("\nWe did it!")
            break
        elif conf == '2' or conf.lower() == "no":
            print("\nWe shall try again!")
        """
        if all(word in cleartext.lower() for word in words):
            break
    ckey = (26 - key) % 26
    print("\n>Key:", ckey, "\n\n>Cleartext:", cleartext)
    file = open("cleartextcaesar.txt", 'w+')
    file.write(cleartext)
    file.close()
    print("\nNote: The cleartext is stored in the file 'cleartextcaesar.txt'.")


if __name__ == '__main__':
    caesar_decrypt_analytical()
