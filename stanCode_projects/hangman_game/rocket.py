"""
File: rocket.py
Name: 黃科諺
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	This program draws a rocket composed of six parts; its size changes proportionately to the constant SIZE
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	This function draws the head with a length equal to SIZE and a width of SIZE*2+2
	"""
	for i in range(SIZE):
		for j in range(SIZE+1):
			if (i+j)>(SIZE-1):
				print('/', end='')
			else:
				print(' ', end='')
		for j in range(SIZE+1,SIZE*2+2):
			if (j-i)>(SIZE+1):
				print(' ', end='')
			else:
				print('\\', end='')
		print('')


def belt():
	"""
	This function draws the belt with a length of 1 and a width of SIZE*2+2
	"""
	for i in range(SIZE*2+2):
		if i==0:
			print('+', end='')
		elif i==SIZE*2+1:
			print('+', end='')
		else:
			print('=', end='')
	print('')


def upper():
	"""
	This function draws the upper part of the body with a length equal to SIZE and a width of SIZE*2+2
	"""
	for i in range(SIZE):
		for j in range(SIZE+1):
			if j==0:
				print('|', end='')
			elif (i+j)<SIZE:
				print('.', end='')
			else:
				if SIZE%2==1:
					if (i + j) % 2 == 1:
						print('/', end='')
					else:
						print('\\', end='')
				else:
					if (i + j) % 2 == 1:
						print('\\', end='')
					else:
						print('/', end='')
		for j in range(SIZE+1,SIZE*2+2):
			if j == SIZE * 2 + 1:
				print('|', end='')
			elif (j-i) > SIZE+1:
				print('.', end='')
			else:
				if SIZE % 2 == 1:
					if (i + j) % 2 == 1:
						print('/', end='')
					else:
						print('\\', end='')
				else:
					if (i + j) % 2 == 1:
						print('\\', end='')
					else:
						print('/', end='')
		print('')


def lower():
	"""
	This function draws the lower part of the body with a length equal to SIZE and a width of SIZE*2+2
	"""
	for i in range(SIZE):
		for j in range(SIZE+1):
			if j==0:
				print('|', end='')
			elif (j-i)<1:
				print('.', end='')
			else:
				if (i + j) % 2 == 1:
					print('\\', end='')
				else:
					print('/', end='')
		for j in range(SIZE+1,SIZE*2+2):
			if j == SIZE * 2 + 1:
				print('|', end='')
			elif (i+j) > SIZE*2:
				print('.', end='')
			else:
				if (i + j) % 2 == 1:
					print('\\', end='')
				else:
					print('/', end='')
		print('')












###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()