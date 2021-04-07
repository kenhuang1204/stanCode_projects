"""
File: weather_master.py
Name: 黃科諺
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100
"""
EXIT: When the value assigned to EXIT is entered, input of the data set is completed and the results will show.
"""


def main():
	"""
	Input: Various amount of temperature data
	Output: The highest temperature, lowest temperature, average, and cold days of the data set of input(s)
	"""
	print('stanCode \"Weather Master 4.0\"!')
	data=int(input('Next Temperature: '+'(or '+str(EXIT)+' to quit)? '))
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = data
		minimum = data
		sum = data
		days = 1
		average = float(data)
		cold_days = 0
		if data < 16:
			cold_days = int(cold_days + 1)
		while True:
			data = int(input('Next Temperature: '+'(or '+str(EXIT)+' to quit)? '))
			if data == EXIT:
				break
			if data < 16:
				cold_days = int(cold_days+1)
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
			sum = float(sum + data)
			days = int(days+1)
			average = sum/days
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = '+ str(average))
		print(str(cold_days) + ' cold day(s)')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
