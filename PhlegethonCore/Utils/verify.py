import sys,os

def getProjectContents():
	directoryContents = []

	for dirname, dirnames, filenames in os.walk('.'):
		# print path to all filenames.
		for filename in filenames:
			fileName = os.path.join(dirname, filename)
			if('git' in fileName):
				continue
			directoryContents.append(fileName[2:])

	return directoryContents

def run():

	contents = []
	f = open('textFiles/dirContents.txt','r')

	for line in f:
		newLine = line.replace('\n','')
		contents.append(line)

	directoryContents = getProjectContents()

	dangerFlag = 0
	for entry in contents:
		actualEntry = entry.rstrip()
		if actualEntry not in directoryContents:
			errorMessage = "The file " + actualEntry + " is not present."
			print errorMessage
			raise ValueError(errorMessage)
			dangerFlag = 1

	if dangerFlag == 1:
		sys.exit("Not all files are present")


if __name__ == "__main__":
    run()