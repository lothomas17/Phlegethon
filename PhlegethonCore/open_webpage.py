import webbrowser

#takes user input and assigns it to a URL variable
def getBrowserURL():
	#grabs user input
	url = raw_input("Please provide a valid URL. \n")

	#checks to see if the beginning is a valid format
	if(url[0:5] != 'https' and url[0:5] != 'http:'):
		url = 'https://' + url
	return url


def run():
	url =getBrowserURL()
	webbrowser.open_new_tab(url)

if __name__ == "__main__":
    run()