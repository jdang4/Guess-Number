#!/usr/bin/python3.6
from collections import deque
import sys

secretNum = "45458"
counter = 1
notInSecretNum = []
positionsTaken = []
actualNum = list("xxxxx")

def actualTotalGoats() :
	count = 0
	stringNum = ''.join(actualNum)
	for c in stringNum :
		if not c.isalpha() :
			count += 1
	return count

#this works
def find_Num_Not_In_Secret_Number(Snum) :
	for c in Snum :
		if c not in secretNum :
			notInSecretNum.append(c)
			break

	return len(notInSecretNum)

#this works
def test_Guess_Number_Chicken(Snum, chicken) :
	chicken = 0
	for c in Snum :
		if c in secretNum :
			chicken += 1

	return chicken

#this works
def test_Guess_Number_Goat(Snum, goat) :
	goat = 0
	for i in range(0, 5, 1) :
		char_of_Snum = Snum[i:(i+1)]
		char_of_secretNum = secretNum[i:(i+1)]
		if char_of_Snum == char_of_secretNum :
			goat += 1

	return goat

#this works
def printStats(Snum, chicken, goat) :
	global counter
	print("Guess Number: " + Snum)
	print("Number of Guesses: " + str(counter))
	print("Number of Chickens: " + str(chicken))
	print("Number of Goats: " + str(goat))
	print('')
	print("-----------------------")
	print('')
	counter += 1
	#return counter

# this works
def find_digit_position_for_one_goat(Sdigit, increment) :

	Snum = Sdigit + ((notInSecretNum[0]) * 4)
	for i in range(0, 5, increment) :
		#currentIndex = 0
		if i not in positionsTaken :
			#print(i)
			chicken = test_Guess_Number_Chicken(Snum, 0)
			goat = test_Guess_Number_Goat(Snum, 0)
			printStats(Snum, chicken, goat)
			if goat == 0 :
				temp_Snum = deque(list(Snum))
				#print("i: " + str(i))
				temp_Snum.rotate(increment)
				Snum = ''.join(temp_Snum)
				#currentIndex += 1
				#print(Snum1)
			else :
				actualNum[i] = Sdigit
				positionsTaken.append(i)
				#print(''.join(actualNum))
				break
		else :
			temp_Snum = deque(list(Snum))
				#print("i: " + str(i))
			temp_Snum.rotate(increment)
			Snum = ''.join(temp_Snum)


def algorithm_for_two_goats(Sdigit, Snum_even, Snum_odd) :
	for i in range(0, 2, 1) :
		if (i % 2) == 0 :
			chicken = test_Guess_Number_Chicken(Snum_even, 0)
			goat = test_Guess_Number_Goat(Snum_even, 0)
			printStats(Snum_even, chicken, goat)

			if goat == 0 :
				actualNum[1] = Sdigit
				actualNum[3] = Sdigit
				break

			elif goat == 1 :
				find_digit_position_for_one_goat(Sdigit, 2)

			else :
				Snum_even = ((Sdigit + notInSecretNum[0]) * 2) + notInSecretNum[0]

				#Snum_even = ((Sdigit + "5") * 2) + "5"
				chicken = test_Guess_Number_Chicken(Snum_even, 0)
				goat = test_Guess_Number_Goat(Snum_even, 0)
				printStats(Snum_even, chicken, goat)
						#print("sdljtlatjlatlh")
				if goat == 1 :
							#print("lsjlat")
					temp_Snum_even = deque(list(Snum_even))
							#print("i: " + str(i))
					temp_Snum_even.rotate(2)
					Snum_even = ''.join(temp_Snum_even)
					chicken = test_Guess_Number_Chicken(Snum_even, 0)
					goat = test_Guess_Number_Goat(Snum_even, 0)
					printStats(Snum_even, chicken, goat)
					print("Will Cooley")
					if goat == 2 :
						actualNum[2] = Sdigit
						actualNum[4] = Sdigit
						break
					else :
						actualNum[0] = Sdigit
						actualNum[4] = Sdigit
						break

						# 4 X 4 X 5
				elif goat == 2 :
					actualNum[0] = Sdigit
					actualNum[2] = Sdigit
							#print(''.join(actualNum))
					break

		else :
			chicken = test_Guess_Number_Chicken(Snum_odd, 0)
			goat = test_Guess_Number_Goat(Snum_odd, 0)
			printStats(Snum_odd, chicken, goat)

			if goat == 0 :
				actualNum[3] = Sdigit
			else:
				actualNum[1] = Sdigit

					
def find_digit_position_for_two_goats(Sdigit) :

	Snum_even = ((Sdigit + notInSecretNum[0]) * 2) + Sdigit
		#print(Snum2_even)
	Snum_odd = (notInSecretNum[0] + Sdigit) + (notInSecretNum[0] * 3)
		#print(Snum2_odd)

	algorithm_for_two_goats(Sdigit, Snum_even, Snum_odd)



def algorithm_for_three_goats(Sdigit, Snum_even, Snum_odd) :
	chicken = test_Guess_Number_Chicken(Snum_even, 0)
	goat = test_Guess_Number_Goat(Snum_even, 0)
	printStats(Snum_even, chicken, goat)

	# if first guess resulted in 3 goats, then correctly guessed
	# the 3 positions that hold the specified Sdigit within the secret number
	if goat == 3 :
		actualNum[0] = Sdigit
		actualNum[2] = Sdigit
		actualNum[4] = Sdigit

	# means two of the positions that contain the specified Sdigit within guess
	# is correctly placed
	# must figure out which ones 
	elif goat == 2 :
		# start off with placing the specified Sdigit within the 0 and 2 index position
		Snum_even = ((Sdigit + notInSecretNum[0]) * 2) + notInSecretNum[0]

		# X 0 X 0 0
		chicken = test_Guess_Number_Chicken(Snum_even, 0)
		goat = test_Guess_Number_Goat(Snum_even, 0)
		printStats(Snum_even, chicken, goat)
		
		# if only 1 was correct then must find which of the 2 even index positions hold
		# 2 of the specified digit
		if goat == 1 :
			temp_Snum_even = deque(list(Snum_even))
			temp_Snum_even.rotate(2) # shifting each character by 2
			Snum_even = ''.join(temp_Snum_even)

			# 0 0 X 0 X
			# making another guess
			chicken = test_Guess_Number_Chicken(Snum_even, 0)
			goat = test_Guess_Number_Goat(Snum_even, 0)
			printStats(Snum_even, chicken, goat)
			
			# if still got 1 then 2 of the specfied Sdigit has to be placed 
			# at positions 0 and 4 within the secret number
			if goat == 1 :
				actualNum[0] = Sdigit
				actualNum[4] = Sdigit

				# now must locate which of the odd position index holds the 
				# third specified digit
				# 0 X 0 0 0
				chicken = test_Guess_Number_Chicken(Snum_odd, 0)
				goat = test_Guess_Number_Goat(Snum_odd, 0)
				printStats(Snum_odd, chicken, goat)

				# correctly guessed the position of the third digit of the specified
				# digit
				if goat == 1 :
					actualNum[1] = Sdigit
				
				# then it has to be in the other odd index position, which is at 3
				# 0 0 0 X 0			
				else :
					actualNum[3] = Sdigit
			
			# if it resulted in 2 goats then know where 2 of 
			# the specified digit are located 
			else :
				actualNum[2] = Sdigit
				actualNum[4] = Sdigit

				# now must locate which of the odd position index holds the 
				# third specified digit
				# 0 X 0 0 0
				chicken = test_Guess_Number_Chicken(Snum_odd, 0)
				goat = test_Guess_Number_Goat(Snum_odd, 0)
				printStats(Snum_odd, chicken, goat)

				# correctly guessed the position of the third digit of the specified
				# digit
				if goat == 1 :
					actualNum[1] = Sdigit
				
				# then it has to be in the other odd index position, which is at 3
				# 0 0 0 X 0
				else :
					actualNum[3] = Sdigit

		# if it resulted in 2 goasts then 2 of the specified digit
		# are located at 0 and 2 index position
		elif goat == 2 :
			actualNum[0] = Sdigit
			actualNum[2] = Sdigit

			#now finding the third
			# 0 X 0 0 0
			chicken = test_Guess_Number_Chicken(Snum_odd, 0)
			goat = test_Guess_Number_Goat(Snum_odd, 0)
			printStats(Snum_odd, chicken, goat)

			# correctly guessed the position of the third digit of the specified
			# digit
			if goat == 1 :
				actualNum[1] = Sdigit
			
			# no goats so then it has to be in the other odd index position, which is at 3
			# 0 0 0 X 0
			else :
				actualNum[3] = Sdigit
	
	# if it resulted in 0 goats then know that one of the specified digit is located
	# at one of the even index position so check each one
	# already know that the 2 other locations of the specified digit must be at the 
	# odd position 
	else :
		find_digit_position_for_one_goat(Sdigit, 2)
		actualNum[1] = Sdigit
		actualNum[3] = Sdigit

def find_digit_position_for_three_goats(Sdigit) :
	Snum_even = ((Sdigit + notInSecretNum[0]) * 2) + Sdigit
		#print(Snum2_even)
	Snum_odd = (notInSecretNum[0] + Sdigit) + (notInSecretNum[0] * 3)

	algorithm_for_three_goats(Sdigit, Snum_even, Snum_odd)



def algorithm_for_four_goats(Sdigit, Snum) :

	Snum = Sdigit + ((notInSecretNum[0]) * 4)
	# checking each position within the number
	for i in range(0, 5, 1) :
		if i not in positionsTaken :
			actualNum[i] = Sdigit

		else :
			temp_Snum = deque(list(Snum))
			temp_Snum.rotate(1) # shifting the characters to the right by 1
			Snum = ''.join(temp_Snum) # putting it back to string form

				
def find_digit_position_for_four_goats(Sdigit) :

	Snum = Sdigit + ((notInSecretNum[0] * 4))
	algorithm_for_four_goats(Sdigit, Snum)

def simulation(start, end, chicken, goat) :
	
	for i in range(start, end, 1) :
		stringDigit = str(i)
		stringNum = stringDigit * 5
		chicken = test_Guess_Number_Chicken(stringNum, chicken)
		goat = test_Guess_Number_Goat(stringNum, goat)
		printStats(stringNum, chicken, goat)

		if goat == 1 :
			find_digit_position_for_one_goat(stringDigit, 1)
		#print(''.join(actualNum))
			num = actualTotalGoats()
			if num == 5 :
				break

		elif goat == 2 :
			find_digit_position_for_two_goats(stringDigit)
		#print(''.join(actualNum))
			num = actualTotalGoats()
			if num == 5 :
				break

		elif goat == 3 :
			find_digit_position_for_three_goats(stringDigit)
		#print(''.join(actualNum))
			num = actualTotalGoats()
			if num == 5 :
				break

		elif goat == 4 :
			find_digit_position_for_four_goats(stringDigit)
		#print(''.join(actualNum))
			num = actualTotalGoats()
			if num == 5 :
				break

		elif goat == 5:
			actualNum = list(stringNum)
			sys.exit(0)


if __name__ == "__main__" :
	chicken = 0
	goat = 0
	guessNum = "01234" # making my first guess
	chicken = test_Guess_Number_Chicken(guessNum, chicken)
	goat = test_Guess_Number_Goat(guessNum, goat)
	print('')
	printStats(guessNum, chicken, goat)
	#print stats (use seperate function to check)

	# in the case if my first attempt happened to be the secret number
	if guessNum == secretNum :
		sys.exit(0)

	if chicken == 5 :
		notInSecretNum.append('5')
		simulation(0, 5, chicken, goat)

	elif chicken == 0 :
		notInSecretNum.append('0')
		simulation(5, 10, chicken, goat)

	else :
		for i in range(0, 5, 1) :
			stringDigit = str(i)
			stringNum = stringDigit * 5
			chicken = test_Guess_Number_Chicken(stringNum, chicken)
			goat = test_Guess_Number_Goat(stringNum, goat)
			printStats(stringNum, chicken, goat)

			if goat == 0 :
				notInSecretNum.append(stringDigit)
				break

		simulation(0, 10, chicken, goat)


	num = actualTotalGoats()
	if num == 5 :
		finalGuess = ''.join(actualNum)
		chicken = test_Guess_Number_Chicken(finalGuess, chicken)
		goat = test_Guess_Number_Goat(finalGuess, goat)
		printStats(finalGuess, chicken, goat)


	print("Secret Number: " + secretNum)
	print(''.join(actualNum))

	