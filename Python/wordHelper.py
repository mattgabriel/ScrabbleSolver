import random
from random import randint

class WordHelper():

	def __init__(self, dictionary, numLetters, numVowels):
		self.vowels = 'aeiou'
		self.consonants = 'bcdfghjklmnpqrstvwxyz'
		self.dictionary = dictionary
		self.numLetters = numLetters
		self.numVowels = numVowels
		self.numConsonants = numLetters - numVowels
		self.letters = []
		self.solutions = []

	def __getVowels(self):
		self.letters = []
		# get random vowels
		for x in range(0, self.numVowels):
			index = randint(0,len(self.vowels)-1)
			self.letters.append(self.vowels[index])

	def __getConsonants(self):
		# get random consonants
		for x in range(0, self.numConsonants):
			index = randint(0,len(self.consonants)-1)
			self.letters.append(self.consonants[index])

	def getLettersAndSolutions(self):
		_solutions = []
		while len(_solutions) < 5:
			data = self.__getLettersAndSolutions()
			_letters = data[0]
			_solutions = data[1]
		return [_letters, _solutions]

	def __getLettersAndSolutions(self):
		_letters = self.getLetters()
		_solutions = self.findWordsContaining(_letters)
		return [_letters, _solutions]

	def getLetters(self):
		self.__getVowels()
		self.__getConsonants()
		random.shuffle(self.letters)
		return self.letters

	def findWordsContaining(self, letterArray):
		#  loop through each dict word
		for i in self.dictionary:
			wordArr = list(i) # turn word into an array of letters
			self.__findPossibleSolutions(wordArr, letterArray)
		
		self.solutions.sort(key=len) # sort array, shortest to longest word
		self.solutions = self.solutions[::-1] # reverse array
		return self.solutions


	# where a is the dictionary word and b is the array of letters given to the user to solve
	def __findPossibleSolutions(self, a, b):
		c = [val for val in a if val in b]
		if len(c) > 5 and len(c) == len(a):
			# print(self.arrayToString(a))
			# self.__validateSolution(a, b)
			if self.__validateSolution(a, b):
				self.solutions.append(self.arrayToString(a).title())
		

	# this will remove false solutions. This may be caused by a words having 
	# duplicate letters that succeeded in the intersection search
	# a is the found dictionary word
	# b is the array of letters given to use user to find words on
	def __validateSolution(self, a, b):
		arr = b[:]
		for i in a:
			if i in arr:
				arr = self.__removeElementFromArray(arr, i)
			else:
				return False

		return True
		# print(self.arrayToString(b))

	# removes only the first occurance of the element
	#  so if there are dupplicates it will keep the remaining ones
	def __removeElementFromArray(self, array, element):
		counter = 0
		for i in array:
			if i == element:
				array.pop(counter)
				return array
			counter += 1
		return array


	def arrayToString(self, array):
		return ''.join(str(x) for x in array)

