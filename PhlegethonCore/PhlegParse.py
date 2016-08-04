import sys,os


#finds the longest substring of two strings
def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]


#checks the input against an index to determine action
def identifyFunction(input):
	options = []
	maxLen = 0
	retIndex = 0

	f = open("index.txt", 'r')
	for line in f:
		if not line:
			print "There has been an error"
			break
		newLine = line.rstrip()
		options.append(newLine)

	index = 0
	for i in options:
		subStr = longest_common_substring(input,i)
		if (len(subStr) > maxLen):
			maxLen = len(subStr)
			retIndex = index
		index += 1

	return options[retIndex]


#Removes extraneous bits and formats the input string correctly
def parseInput(args):
	args.lower()
	args.replace('phlegethon','')
	args.replace(' ','_')
	return args

def run():
	args = raw_input()
	inpStr = parseInput(args)
	retStr = identifyFunction(inpStr)
	return retStr


if __name__ == "__main__":
    run()