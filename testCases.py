#!/usr/bin/python3.6

import guessNumber
import os
import sys

if __name__ == "__main__" :

	num_of_successes = 0
	for i in range(0, 100000, 1) :
		stringDigit = str(i)
		stringNum = stringDigit.zfill(5)

		# storing the current 5 digit number into 
		# a text file so that it can be read by 
		# guessNumber program
		# this current number will act as the secret number
		f = open("tempTest.txt", "w+")
		f.write(stringNum)
		f.close()

		# checking the return value of program
		value = os.system("python3 guessNumber.py tempTest.txt")

		# meant that program was unable to determine the
		# secret number 
		if value == 1 :
			print("Program Terminated")
			sys.exit(1)


		if value == 0 :
			num_of_successes += 1

	# obtain the worst case scenario's number of guesses
	# it took for my algorithm to discover the secret number
	f = open("maximumCount.txt", "r")
	worseCase = f.readline()
	f.close()
	worseCase.rstrip('\n')

	print(str(num_of_successes) + " out of 100000 were successful")
	print("Worst Case Scenario: " + worseCase)

	sys.exit(0)
