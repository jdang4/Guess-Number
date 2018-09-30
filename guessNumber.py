#!/usr/bin/python3.6
from collections import deque
import sys

secretNum = "98765"
counter = 1
notInSecretNum = []
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
	if len(notInSecretNum) == 0 :
		Snum1 = Sdigit + ("5" * 4)
	else :
		Snum2 = Sdigit + ((notInSecretNum[0]) * 4)

	for i in range(0, 5, increment) :
		if len(notInSecretNum) == 0 :
			chicken = test_Guess_Number_Chicken(Snum1, 0)
			goat = test_Guess_Number_Goat(Snum1, 0)
			printStats(Snum1, chicken, goat)
			if goat == 0 :
				temp_Snum = deque(list(Snum1))
				#print("i: " + str(i))
				temp_Snum.rotate(increment)
				Snum1 = ''.join(temp_Snum)
				#print(Snum1)
			else :
				actualNum[i] = Sdigit
				#print(''.join(actualNum))
				break

		else :
			chicken = test_Guess_Number_Chicken(Snum2, 0)
			goat = test_Guess_Number_Goat(Snum2, 0)
			printStats(Snum2, chicken, goat)
			if goat == 0 :
				temp_Snum = deque(list(Snum2))
				temp_Snum.rotate(increment)
				Snum2 = ''.join(temp_Snum)
			else :
				actualNum[i] = Sdigit
				#print(''.join(actualNum))
				break


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
				if len(notInSecretNum) == 0 :
					Snum_even = ((Sdigit + "5") * 2) + "5"
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
	if len(notInSecretNum) == 0 :
		Snum1_even = ((Sdigit + "5") * 2) + Sdigit
		#print(Snum1_even)
		Snum1_odd = ("5" + Sdigit) + ("5" * 3) 
		#print(Snum1_odd)
	else :
		Snum2_even = ((Sdigit + notInSecretNum[0]) * 2) + Sdigit
		#print(Snum2_even)
		Snum2_odd = (notInSecretNum[0] + Sdigit) + (notInSecretNum[0] * 3)
		#print(Snum2_odd)

	if len(notInSecretNum) == 0 :
		algorithm_for_two_goats(Sdigit, Snum1_even, Snum1_odd)
	else :
		algorithm_for_two_goats(Sdigit, Snum2_even, Snum2_odd)



def algorithm_for_three_goats(Sdigit, Snum_even, Snum_odd) :
	chicken = test_Guess_Number_Chicken(Snum_even, 0)
	goat = test_Guess_Number_Goat(Snum_even, 0)
	printStats(Snum_even, chicken, goat)

	if goat == 3 :
		actualNum[0] = Sdigit
		actualNum[2] = Sdigit
		actualNum[4] = Sdigit


	elif goat == 2 :
		print("here")
		if len(notInSecretNum) == 0 :
			Snum_even = ((Sdigit + "5") * 2) + "5"
		else :
			Snum_even = ((Sdigit + notInSecretNum[0]) * 2) + notInSecretNum[0]

		chicken = test_Guess_Number_Chicken(Snum_even, 0)
		goat = test_Guess_Number_Goat(Snum_even, 0)
		printStats(Snum_even, chicken, goat)
		print("here1")
		if goat == 1 :
			temp_Snum_even = deque(list(Snum_even))
			temp_Snum_even.rotate(2)
			Snum_even = ''.join(temp_Snum_even)
			chicken = test_Guess_Number_Chicken(Snum_even, 0)
			goat = test_Guess_Number_Goat(Snum_even, 0)
			printStats(Snum_even, chicken, goat)
			print("here2")
			print(goat)
			if goat == 1 :
				actualNum[0] = Sdigit
				actualNum[4] = Sdigit
				chicken = test_Guess_Number_Chicken(Snum_odd, 0)
				goat = test_Guess_Number_Goat(Snum_odd, 0)
				printStats(Snum_odd, chicken, goat)
				if goat == 1 :
					actualNum[1] = Sdigit
							#break
				else :
					actualNum[3] = Sdigit
							#break
			else :
				actualNum[2] = Sdigit
				actualNum[4] = Sdigit
				chicken = test_Guess_Number_Chicken(Snum_odd, 0)
				goat = test_Guess_Number_Goat(Snum_odd, 0)
				printStats(Snum_odd, chicken, goat)
				if goat == 1 :
					actualNum[1] = Sdigit
							#break
				else :
					actualNum[3] = Sdigit

				# 4 X 4 X 5
		elif goat == 2 :
			actualNum[0] = Sdigit
			actualNum[2] = Sdigit
			chicken = test_Guess_Number_Chicken(Snum_odd, 0)
			goat = test_Guess_Number_Goat(Snum_odd, 0)
			printStats(Snum_odd, chicken, goat)

			if goat == 1 :
				actualNum[1] = Sdigit
						#break
			else :
				actualNum[3] = Sdigit
						#break
	else :
		find_digit_position_for_one_goat(Sdigit, 2)
		actualNum[1] = Sdigit
		actualNum[3] = Sdigit

def find_digit_position_for_three_goats(Sdigit) :
	if len(notInSecretNum) == 0 :
		Snum1_even = ((Sdigit + "5") * 2) + Sdigit
		#print(Snum1_even)
		Snum1_odd = ("5" + Sdigit) + ("5" * 3) 
		#print(Snum1_odd)
	else :
		Snum2_even = ((Sdigit + notInSecretNum[0]) * 2) + Sdigit
		#print(Snum2_even)
		Snum2_odd = (notInSecretNum[0] + Sdigit) + (notInSecretNum[0] * 3)

	if len(notInSecretNum) == 0 :
		algorithm_for_three_goats(Sdigit, Snum1_even, Snum1_odd)
	else :
		algorithm_for_three_goats(Sdigit, Snum2_even, Snum2_odd)


def algorithm_for_four_goats(Sdigit, Snum) :
	if len(notInSecretNum) == 0 :
		Snum = Sdigit + ("5" * 4)
	else :
		Snum = Sdigit + ((notInSecretNum[0]) * 4)

	for i in range(0, 5, 1) :
		#if len(notInSecretNum) == 0 :
		chicken = test_Guess_Number_Chicken(Snum, 0)
		goat = test_Guess_Number_Goat(Snum, 0)
		printStats(Snum, chicken, goat)

		if goat == 0 :
			#print(i)
			
			for j in range(0, 5, 1) :
				if j != i :
					print(j)
					actualNum[j] = Sdigit
			break
		

		else :
			temp_Snum = deque(list(Snum))
			temp_Snum.rotate(1)
			Snum = ''.join(temp_Snum)
				

def find_digit_position_for_four_goats(Sdigit) :
	#Snum = ""
	if len(notInSecretNum) == 0 :
		Snum = Sdigit + ("5" *4)
	else :
		print("hi")
		Snum = Sdigit + ((notInSecretNum[0] * 4))
		#algorithm_for_four_goats(Sdigit, Snum1)
	
	algorithm_for_four_goats(Sdigit, Snum)




if __name__ == "__main__" :
	chicken = 0
	goat = 0
	guessNum = "01234" 
	chicken = test_Guess_Number_Chicken(guessNum, chicken)
	goat = test_Guess_Number_Goat(guessNum, goat)
	print('')
	printStats(guessNum, chicken, goat)
	#print stats (use seperate function to check)

	if guessNum == secretNum :
		sys.exit(0)
	#want to find a number that isn't in the secret number
	num = find_Num_Not_In_Secret_Number(guessNum)

	for i in range(0, 10, 1) :
		stringDigit = str(i)
		stringNum = stringDigit * 5
		chicken = test_Guess_Number_Chicken(stringNum, chicken)
		goat = test_Guess_Number_Goat(stringNum, goat)
		printStats(stringNum, chicken, goat)
		
		if goat == 1 :
			find_digit_position_for_one_goat(stringDigit, 1)
			print(''.join(actualNum))
			num = actualTotalGoats()
			if num == 5 :
				break
			
		elif goat == 2 :
			find_digit_position_for_two_goats(stringDigit)
			print(''.join(actualNum))
			num = actualTotalGoats()
			if num == 5 :
				break
		
		elif goat == 3 :
			find_digit_position_for_three_goats(stringDigit)
			print(''.join(actualNum))
			num = actualTotalGoats()
			if num == 5 :
				break

		elif goat == 4 :
			find_digit_position_for_four_goats(stringDigit)
			print(''.join(actualNum))
			num = actualTotalGoats()
			if num == 5 :
				break

		elif goat == 5:
			actualNum = list(stringNum)
			sys.exit(0)

		
	num = actualTotalGoats()
	if num == 5 :
		finalGuess = ''.join(actualNum)
		chicken = test_Guess_Number_Chicken(finalGuess, chicken)
		goat = test_Guess_Number_Goat(finalGuess, goat)
		printStats(finalGuess, chicken, goat)


	print("Secret Number: " + secretNum)
	print(''.join(actualNum))

	