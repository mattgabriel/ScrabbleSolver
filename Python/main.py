# import json
import argparse

import readFile as rf
import wordHelper as wh

# config
numLetters = 9
numVowels = 4
dictionary = rf.ReadFile().linesToArray('../dictionary.txt')
letterArray = [] # populated only is mode 1 is selected

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('--letters', help="A string of letters with no spaces. If provided the program will return the list of words that could be formed with the given letters.")
args = parser.parse_args()


if args.letters and len(args.letters) >= 5 and len(args.letters) <= 10:
	letterArray = list(args.letters.lower())


wordHelper = wh.WordHelper(dictionary, numLetters, numVowels)

if len(letterArray) > 0:
	#find the possible words that could be formed with the given letters
	solutions = wordHelper.findWordsContaining(letterArray)

else:
	#returns an array of random letters and the possible words that could be formed with them
	data = wordHelper.getLettersAndSolutions()
	letters = data[0]
	solutions = data[1]

	print('\n\n\n\n\n')
	print('------------------------------------------------')
	print('Form the longest possible word with the following letters:')
	print(' - '.join(str(x).upper() for x in letters))
	print('------------------------------------------------')


print('\n')
print('------------------------------------------------')
if len(solutions) > 0:
	print('BEST: ' + str(len(solutions[0])) + ' letters')
else:
	print('No words found')
print('SOLUTIONS:')
print(solutions)
print('------------------------------------------------')
