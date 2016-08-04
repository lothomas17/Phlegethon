import sys,os
import re

def matchFiles(contents):

	correctNames = []
	removalList = []
	f = open('dirContents.txt','r')

	for line in f:
		newLine = line.replace('\n','')
		correctNames.append(newLine)

	for i in contents:
		if (i not in correctNames):
			removalList.append(i)

	return removalList

def run():
	contents = []

	for dirname, dirnames, filenames in os.walk('.'):
		# print path to all filenames.
		for filename in filenames:
			fileName = os.path.join(dirname, filename)
			if('git' in fileName):
				continue
			contents.append(fileName[2:])

	badFiles = matchFiles(contents)
	print badFiles

	for i in badFiles:
		killCommand = 'rm ' + i
		os.system(killCommand)




if __name__ == "__main__":
    run()