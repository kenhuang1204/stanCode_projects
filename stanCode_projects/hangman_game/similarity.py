"""
File: similarity.py
Name: 黃科諺
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Input: str, long sequence s1 and short sequence s2
    Output: str, sequence of the homology of s1 and s2
    """
    s1 = input('Please give me a DNA sequence to search: ')
    s2 = input('What DNA sequence would you like to match? ')
    s1 = s1.upper()
    s2 = s2.upper()
    best_match=find_homology(s1, s2)
    print('The best match is '+best_match)


def find_homology(long, short):
    """
    :param long: str, the long sequence to be compared
    :param short: str, the short sequence to be compared
    :return: str, the homology of the long and shor sequence
    """
    l1=len(long)
    l2=len(short)
    subsequence1=long[0:len(short)]
    score1=0
    # score1=the matching result of the comparison of the first subsequence of long
    for i in range(len(short)):
        base1=subsequence1[i]
        base2=short[i]
        if base1==base2:
            score1+=1
    maximum=score1
    match = subsequence1
    for i in range(1,l1-l2+1):
        # l1-l2+1 = Total number of subsequence sets for comparison
        subsequence=long[0+i:l2+i]
        score = 0
        # The compared subsequence of long sequence
        for j in range(len(short)):
            # len(short) = Number of characters compared in each subsequence set
            base1=subsequence[j]
            base2=short[j]
            if base1==base2:
                score+=1
        if score>maximum:
            maximum=score
            match=subsequence
    return match











###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
