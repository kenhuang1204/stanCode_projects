"""
File: boggle.py
Name: 黃科諺
----------------------------------------
Input: 4 rows of 4 letters
Output: all the words found within the given 4 x 4 letter matrix under the rule of the game 'Boggle'
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

word_list = []
found_word_list = []


def main():
	"""
	Input: 4 rows of 4 letters
	Output: all the words found within the given 4 x 4 letter matrix under the rule of the game 'Boggle'
	"""
	global word_list
	global found_word_list
	word_list = read_dictionary()
	letter_list = []
	for i in range(4):
		row = str(input(f'{i+1} row of letters: '))
		if len(row) == 7:
			new_row = row.lower()
			split_new_row = new_row.split()
			letter_list.append(split_new_row)
		else:
			print('Illegal input')
			break

	if len(letter_list) == 4:
		current = []
		for i in range(4):
			for j in range(4):
				current.append([i, j])
				search_machine(letter_list, current)
				current.pop()
		print(f'There are {len(found_word_list)} words in total.')


def search_machine(letter_list, current):
	"""
	:param letter_list: list, containing 4 sub-lists (each sub-list contains 4 letters)
	:param current: list, containing an i-j pair (stored as a list unit) that stands for a letter
	:return: this function returns nothing
	"""
	prev_index = current[len(current) - 1]
	prev_i = prev_index[0]
	prev_j = prev_index[1]
	for x in range(-1, 2, 1):
		for y in range(-1, 2, 1):
			next_index_i = prev_i + x
			next_index_j = prev_j + y
			if 0 <= next_index_i < 4:
				if 0 <= next_index_j < 4:
					if [next_index_i, next_index_j] not in current:
						current.append([next_index_i, next_index_j])
						str_current = ''
						for ele in current:
							ch = letter_list[ele[0]][ele[1]]
							str_current += ch
						# Choose

						if len(current) >= 4:
							if str_current in word_list:
								if str_current not in found_word_list:
									print(f'Found: \"{str_current}\"')
									found_word_list.append(str_current)

						if has_prefix(str_current):
							search_machine(letter_list, current)
						# Explore

						current.pop()
						# Un-choose


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			word_list.append(word)
		return word_list


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()