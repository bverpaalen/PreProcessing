import re

filename = "tesseract_ST_9788_2015_INIT_EN.txt"

enterregex=""
#One . One space Capitale latter|non letter or start of line
dotregex="[^(].*\.{1}.*[^)]"
tabregex ="\\t"
#Can't be between () bugged
regex = ".*("+dotregex+"|"+tabregex+")"

def main(filepath):
	textObject = open(filepath,'r')
	text = textObject.read()
	textObject.close()

	#text = text.replace("\n","")

	writeOutput(text)

	lines = re.split(regex,text)

	#print(len(lines))
	print("Regex: "+regex)
	print(len(lines))
	for i in range(1,10,1):
		print("Line "+str(i)+": "+lines[i])

def writeOutput(input):
	output = open("output.txt","w+")
	output.write(input)
	output.close()

main(filename)
