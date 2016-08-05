import webbrowser
import sys,os

def getCommonChars(s1,s2):
	numCommon = 0
	for char in s1:
		if char in s2:
			numCommon += 1
	return numCommon

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

def identifyTemplate(input):
	options = []
	maxLen = 0
	retIndex = 0

	f = open("textFiles/webindex.txt", 'r')
	for line in f:
		if not line:
			print "There has been an error"
			break
		newLine = line.rstrip()
		lineToAdd = newLine.replace(".txt","")
		options.append(lineToAdd)

	index = 0
	for i in options:

		subStr = longest_common_substring(input,i)
		numCommon = getCommonChars(input,i)

		percCommon = (numCommon * 1.0) / len(i)

		evalNum = len(subStr) * percCommon

		if (evalNum > maxLen):
			maxLen = evalNum
			retIndex = index
		index += 1

	toReturn = options[retIndex] + ".txt"
	toReturn = "textFiles/" + toReturn
	return toReturn

#takes user input and assigns it to a URL variable
def getTempName():
	#grabs user input
	url = raw_input("Which template do you want to use? \n")

	url.lower()
	url.replace(" ","")

	template = identifyTemplate(url)
	return template


def formatURL(url):
	#checks to see if the beginning is a valid format
	if(url[0:5] != 'https' and url[0:5] != 'http:'):
		url = 'https://' + url
	return url

def OpenWindow(fileName):
	f = open(fileName,'r')

	for line in f:
		if not line:
			break
		url = formatURL(line)
		correctURL = url.replace('\n','')
		webbrowser.open_new_tab(correctURL)

def run():
	url = getTempName()
	OpenWindow(url)

if __name__ == "__main__":
    run()



