"""
File: hailstone.py
Name: 黃科諺
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Input: A natural number
    Output: Print all the Hailstone sequences the number gone through and the steps it took to reach 1
    """
    pass
    print('This program computes Hailstone sequences.')
    print('')
    number = int(input('Enter a number: '))
    if number==1:
        print('It took 0 steps to reach 1.')
    else:
        steps=0
        while True:
            if number%2==1:
                odd_number=int(number*3+1)
                print(str(number)+' is odd, so I make 3n+1: '+str(odd_number))
                number=odd_number
                steps = int(steps+1)
            else:
                even_number=int(number/2)
                print(str(number)+' is even, so I take half: '+str(even_number))
                number=even_number
                steps = int(steps+1)
            if number==1:
                print('It took '+str(steps)+' steps to reach 1.')
                break



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
