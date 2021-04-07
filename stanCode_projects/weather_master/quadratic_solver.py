"""
File: quadratic_solver.py
Name: 黃科諺
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Input: a, b, c
	Output: The root of ax^2 + bx + c = 0
	"""
	print('This program is stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	if a==0:
		print('a can not be 0.')
	else:
		b = int(input('Enter b: '))
		c = int(input('Enter c: '))
		d = b*b - 4 * a * c
		if d<0:
			print('No real roots')
		else:
			y = math.sqrt(d)
			if d>0:
				ans1=float(-b/(2*a)+y/(2*a))
				ans2=float(-b/(2*a)-y/(2*a))
				print('Two roots: '+str(ans1)+' , '+str(ans2))
			else:
				ans3=float(-b/(2*a))
				print('One root: '+str(ans3))









###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
