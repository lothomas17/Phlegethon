import sys,os
import cleanup
import verify


def run():
	print "Exiting program, cleaning files."
	cleanup.run()
	while(True):
		try:
			verify.run()
			print "Verified files, everything is here."
			break
		except ValueError:
			print "Check dirContents against directory to verify missing files."
			exit(1)

if __name__ == "__main__":
    run()