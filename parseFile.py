#!/usr/bin/python
import sys
import re

#This function runs in constant time O(1) because the tasks that it performs
#will run in constant time regardless of the input size. 
#List indexing in Python is O(1).
#Opening a file in Python is also a constant time operation since retrieving 
#an open file descriptor takes constant time. 
def retrieveFile():
	"""Will be used to retrieve the command line arguments and return the input file
	Will attempt opening the file and handle any raised exceptions."""
	inlineArgs = sys.argv
	try:
		fileInput = open(inlineArgs[1])	
		fileInput.close()

	except IndexError as e:
		#Terminate the program because an invalid number of arguments were given
		print("Invalid number of arguments given. Should be 'python PartA.py filename_goes_here'")
		sys.exit()
	
	except IOError:
		#Terminate the program because an invalid path name was given
		print("Unable to open the file. Double-check spelling and run again!")
		sys.exit()

	return inlineArgs[1]

class ParseFile:
	def __init__(self, textFile):
		self._inputFile = textFile			#Store the input file
		self._tokens = {}			#Dictionary to store key=word and its value=counter
		self._uniqueSet = set()		#Set that will store unique tokens 

	#This method runs in the order of O(N).
	#It traverses a list sequentially and for every element of the list it 
	#performs performs a table lookup to see if the element is already in the dictionary.
	#The "not in" operation takes advantage of the dictionary's hashing capabilities to perform constant time lookups.
	def _update_dict(self, words):
		"""Helper function that stores a token and/or updates its frequency if it was previously stored already"""
		for t in words:
			if t not in self._tokens:	#First time seeing a token
				self._uniqueSet.add(t)	#Add unique token to the set
				self._tokens[t] = 1
			else:						#Token is repeated
				self._tokens[t] += 1		

	#This method runs in the order of O(N**2).
	#It reads a file sequentially (line-by-line) and for every line (or iteration)
	#it creates a list of the words found in that line, which is O(N). For every iteration, self._update_dict is called, which
	#is O(N) since it iterates over a list of words. 
	#O(N) * (O(N) + O(N)) = O(N**2)
	def readFile(self):
		"""Parse the file and generate the output"""
		targetFile = open(self._inputFile)
		
		#Read one line at a time into memory
		for line in targetFile:
			#We only want tokens comprised of alphanumeric characters
			words = re.split('\s|[^a-zA-Z0-9]', line)
			words = [w.lower() for w in words if len(w) >= 1]					#Make everything lower case and remove empty strings
			
			#Store/update token info => O(N)
			self._update_dict(words)
		
		targetFile.close()

	#Returning a reference to a collection takes constant time.
	def returnSet(self):
		"""Returns the set that contains the unique tokens"""
		return self._uniqueSet

	#This function generates a list by sorting the values and keys of the dictionary. It uses the sorted() builtin Python function 
	#which is a variation of MergeSort. Thus, the time complexity of generating a sorted list takes O(N*log*N) because dividing the list into two lists repeatedly takes
	#O(log*N) while merging the two lists takes linear time. The function also iterates over the generated list in order to print out the contents, which is a task that 
	#follows the order of O(N). Ultimately, the function follows the order of O(N*log*N).
	def sortDictAndDisplay(self):
		"""Sort the tokens in descending value; break ties by sorting key in ascending order"""
		#Sort the tokens by its frequency value (in descending order) and tokens with equal frequency values will be sorted by the token itself (in ascending order)
		tokens = sorted(self._tokens.items(), key=lambda x:(-x[1], x[0]))

		#Output the dictionary => {token}\t{frequency}
		for p in tokens:
			print("{}\t{}".format(p[0], p[1]))

if __name__ == "__main__":
	#Read the command line arguments and retrieve the input file.
	inputFile = retrieveFile()

	#Will be used to parse the input file 
	fileParser = ParseFile(inputFile)
	
	#Parse the file 
	fileParser.readFile()
	
	#Sort the dictionary of tokens and display the result
	fileParser.sortDictAndDisplay()


