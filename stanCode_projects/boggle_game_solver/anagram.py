"""
File: anagram.py
Name: 黃科諺
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

word_list = []


def main():
    global word_list
    word_list = read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        search_word = input('Find anagrams for: ')
        if search_word == EXIT:
            break
        else:
            anagram_list = find_anagrams(search_word)
            print(f'{len(anagram_list)} anagrams: {anagram_list}')


def read_dictionary():
    """
    :return: list, containing all the words in the file 'dictionary.txt'
    """
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            word_list.append(word)
        return word_list


def find_anagrams(s):
    """
    :param s: str, the input word
    :return: list, a list containing all the anagrams of the input word
    """
    print('Searching...')
    return find_helper(s, [], [])


def find_helper(s, current, ana_list):
    """
    :param s: str, the input word
    :param current: list, containing the permutations of characters in the input word saved in an index form
    :param ana_list: list, consisting of anagrams of the input word
    :return: a list containing all the anagrams of the input word
    """
    if len(current) == len(s):
        str_current = ''
        for ele in current:
            str_current += s[ele]
        if str_current in word_list and str_current not in ana_list:
            print(f'Found: {str_current}')
            ana_list.append(str_current)
            print('Searching...')
    else:
        for i in range(len(s)):
            if len(current) < len(s):
                if i not in current:
                    current.append(i)
                    str_current = ''
                    for ele in current:
                        str_current += s[ele]
                    # Choose
                    if has_prefix(str_current):
                        find_helper(s, current, ana_list)
                    else:
                        pass
                    # # Explore
                    current.pop()
                    # Un-choose
    return ana_list


def has_prefix(sub_s):
    """
    :param sub_s: str, a prefix to be tested
    :return: Boolean, indicating whether anagrams that start with the tested prefix exist
    """
    for word in word_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
