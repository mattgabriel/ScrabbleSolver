
class ReadFile():

	# reads a given file line by line and returs an array 
	# with the contents of each line (as an array)
	def linesToArray(self, filePath):
		words = []
		lines = self.__readLines(filePath)
		for i in lines:
			item = i.replace("\r","")
			item = item.replace("\n","")
			words.append(item)

		return words


	# private method
	def __readLines(self, filePath):
		# open file, read line by line and store each line in an array
		with open(filePath) as f:
			lines = f.readlines()

		return lines