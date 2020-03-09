#!/usr/bin/python
import PartA
import sys

def retrieveFiles():
	"""Retrieve input files and try to open them. Return a tuple => (File1, File2)"""
	inlineArgs = sys.argv	
	try:
		#Open the files and close them to check that the files exist and are able to be opened
		input1 = open(inlineArgs[1])
		input2 = open(inlineArgs[2])
		input1.close()
		input2.close()

	except IndexError:
		#Terminate the program because an invalid number of arguments were given
		print("Invalid number of arguments, exiting now.")
		sys.exit()
	
	except IOError:
		#Terminate the program because at least one of the files is invalid 
		print("Unable to open one of the files. Check spelling and try again!")
		sys.exit()
	
	return (inlineArgs[1], inlineArgs[2])


if __name__ == "__main__":
	#Retrieve input files
	twoFiles = retrieveFiles()	#(FILE1, FILE2)

	#Parse the first file 
	fileParser1 = PartA.ParseFile(twoFiles[0])

	#Parsing a file runs in the order of O(N**2). It reads a file in a linear manner (e.g. line by line) and it 
	#splits the file into a list of words that are comprised of only alphanumeric characters. 
	#Generating a list is O(N), so O(N) * O(N) == O(N**2).
	fileParser1.readFile()

	#Unique tokens of File 1
	#Returning a reference to a set of unique tokens takes constant time O(1).
	set1 = fileParser1.returnSet()	

	#Parse the second file
	fileParser2 = PartA.ParseFile(twoFiles[1])


	#Parsing a file runs in the order of O(N**2). It reads a file in a linear manner (e.g. line by line) and it 
	#splits the file into a list of words that are comprised of only alphanumeric characters. 
	#Generating a list is O(N), so O(N) * O(N) == O(N**2).
	fileParser2.readFile()

	#Unique tokens of File 2
	#Returning a reference to a set of unique tokens takes constant time O(1).
	set2 = fileParser2.returnSet()

	#Find the intersection of the two sets
	#The average case of the intersection operation is O(1). According to Python Documentation,
	#the running time of the intersection operation is O(min(len(SET1),len(SET2))). Taking the length
	#of a set is O(1).
	inter = set2.intersection(set1)

	#Print the length
	#Printing the length of a list is O(1).
	print(len(list(inter)))

