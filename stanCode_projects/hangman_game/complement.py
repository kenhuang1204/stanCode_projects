"""
File: complement.py
Name: 黃科諺
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Input: str; ask users to enter a DNA sequence; characters can only involve A, T, C, G; case insensitive
    Output: str; produce the DNA sequence of the complement strand of the entered DNA sequence
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    dna = dna.upper()
    complement = build_complement(dna)
    print('The complement of '+dna+' is '+complement)


def build_complement(dna):
    """
    :param dna: str, the DNA sequence entered by the user
    :return: str, the complement DNA sequence of the entered sequence
    """
    ans=''
    for base in dna:
        if base=='A':
            ans+='T'
        elif base=='T':
            ans+='A'
        elif base=='C':
            ans+='G'
        else:
            ans+='C'
    return ans



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
