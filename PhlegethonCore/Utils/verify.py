import sys,os


def run():

	contents = []
	f = open('dirContents.txt','r')

	for line in f:
		newLine = line.replace('\n','')
		contents.append(line)

	directoryName = os.path.dirname(os.path.abspath(__file__))
	directoryContents = os.listdir(directoryName)

	dangerFlag = 0
	for entry in contents:
		actualEntry = entry.rstrip()
		if actualEntry not in directoryContents:
			errorMessage = "The file ", actualEntry, " is not present."
			print errorMessage
			raise ValueError(errorMessage)
			dangerFlag = 1

	if dangerFlag == 1:
		sys.exit("Not all files are present")


if __name__ == "__main__":
    run()