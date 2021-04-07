"""
File: largest_digit.py
Name: 黃科諺
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the integer given
	:return: the biggest digit in the given integer
	"""
	biggest = 0
	return helper(n, biggest)


def helper(n, biggest):
	"""
	:param n: the integer given
	:param biggest: the biggest digit so far
	:return: the biggest digit in the given integer
	"""
	new_int = abs(n)
	left_num = new_int // 10
	units_digit = new_int - left_num * 10
	if new_int < 10:
		if units_digit > biggest:
			biggest = units_digit
		return biggest
	else:
		if units_digit > biggest:
			biggest = units_digit
		return helper(left_num, biggest)


if __name__ == '__main__':
	main()
