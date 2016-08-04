import PhlegParse
from PhlegethonCore.Utils import cleanup
import sys,os

def setup():

	modules = {'cleanup': cleanup}
	# f = open('index.txt','r')

	# for line in f:
	# 	if not line:
	# 		print "Empty import list :("
	# 		break
	# 	partLine = line.replace('\n','')
	# 	modName = partLine.replace('.py','')
	# 	modules[modName] = modName.run()

	return modules
	


def run():
	#imports phlegethon modules and scripts
	modules =setup()

	print "Setup is complete. Please make a query"

	while(True):

		function = PhlegParse.run()
		runFunction = 'python ' + function

		modules[function].run()
		
		#function.run()

		#os.system(runFunction)

		if(function == 'exit.py'):
			cleanup.run()
			sys.exit("Goodbye!")


if __name__ == "__main__":
    run()