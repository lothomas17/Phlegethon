import PhlegParse
import Utils.exit
import sys,os

def setup():

	modules = []
	f = open('index.txt','r')

	for line in f:
		if not line:
			print "Empty import list :("
			break
		partLine = line.replace('\n','')
		modName = partLine.replace('.py','')
		__import__(modName)
	


def run():
	#imports phlegethon modules and scripts
	setup()

	while(True):

		function = PhlegParse.run()
		runFunction = 'python ' + function

		os.system(runFunction)

		if(function == 'exit.py'):
			sys.exit("Goodbye!")


if __name__ == "__main__":
    run()