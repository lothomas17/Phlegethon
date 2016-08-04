import PhlegParse
import sys,os
from importlib import import_module
from pydoc import locate

def generateImports():

	modules = []
	f = open('index.txt','r')

	for line in f:
		truncLine = line.replace('\n','')
		packName = truncLine.rsplit('.', 1)
		modules.append(packName)

	for mod in modules:
		package = mod[0]
		module = mod[1]
		module = '.' + module
		globals()[module] = import_module(module,package)

def generateDict():

	modDict = {}
	f = open('index.txt','r')

	for line in f:
		truncLine = line.replace('\n','')
		partFilePath = truncLine.replace('.','/')
		filePath = partFilePath + '.py'
		modStmt = "<module '" + truncLine + "' from '" + filePath + "'>"
		mod = locate(truncLine)
		modDict[truncLine] = mod

	return modDict

def setup():
	generateImports()
	modules = generateDict()

	return modules

def run():
	#imports phlegethon modules and scripts
	modules = setup()

	print "Setup is complete. Please make a query"

	while(True):

		function = PhlegParse.run()
		print function

		modules[function].run()

		if(function == 'PhlegethonCore.Utils.exit'):
			sys.exit("Goodbye!")


if __name__ == "__main__":
    run()