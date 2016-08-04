import sys,os

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
	directoryName = os.path.dirname(os.path.abspath(__file__))
	directoryContents = os.listdir(directoryName)

	badFiles = matchFiles(directoryContents)

	for i in badFiles:
		killCommand = 'rm ' + i
		os.system(killCommand)




if __name__ == "__main__":
    run()