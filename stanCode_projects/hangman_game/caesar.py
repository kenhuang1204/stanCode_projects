"""
File: caesar.py
Name: 黃科諺
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Input: int, a secret number; str, a ciphered string
    Output: str, a deciphered string
    """
    secret_number=int(input('Secret number: '))
    ciphered=input('What\'s the ciphered string?')
    ciphered=ciphered.upper()
    deciphered=decipher(secret_number, ciphered)
    print('The deciphered string is: '+deciphered)


def decipher(secret_number, ciphered):
    """
    param1: int, the number determines the steps moved to find the new alphabet from the alphabet
    param2: str, the ciphered string entered by the user
    return: str, the deciphered string
    """
    new_alphabet=''
    for i in range(len(ALPHABET)):
        if i-secret_number>-1:
            ch=ALPHABET[i-secret_number]
            new_alphabet+=ch
        else:
            ch=ALPHABET[i+(len(ALPHABET)-secret_number)]
            # len(ALPHABET)-secret_number: int, assign the characters in ALPHABET to characters in new alphabet
            new_alphabet+=ch
    ans=''
    for i in range(len(ciphered)):
        ch = ciphered[i]
        if ch not in ALPHABET:
            ans+=ch
        else:
            location=new_alphabet.find(ch)
            ch = ALPHABET[location]
            ans+=ch
    return ans







#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
