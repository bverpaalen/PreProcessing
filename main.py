import re

filename = "tesseract_ST_9788_2015_INIT_EN.txt"

enterregex=""

# No( chars oneDot chars No)
#dotregex="[^(].*\.{1}.*[^)]"
beforeStop = "([^\.]|[^\\t])*"
dotregex="[^(.*]([^\.]|[^\\t])\.[^.*)]"
#regex = ".*?([^(.*]([^\.]|[^\t])\.{1}[^.*)]|([^\.]|[^\t])\t)"
#Tab
#tabregex ="\\t"
tabregex="([^\.]|[^\\t])\\t"
#Chars dotregexOrTabregex
regex = beforeStop+"("+dotregex+"|"+tabregex+")*"

def main(filepath):

	text = retrieveText(filepath)

	header,body = splitText(text)

	writeOutput(body)

	print("Regex: " + regex)

	bodyLines = re.split(regex,body)
	headerLines = re.split(regex,header)


	print(len(bodyLines))
	for i in range(1,10,1):
		if(bodyLines[i]!=None):
			print("Line "+str(i)+": "+bodyLines[i])

def retrieveText(filepath):
	textObject = open(filepath, mode='r', encoding="utf-8")
	text = textObject.read()
	textObject.close()

	return text

def splitText(text):
	splitText = text.split("\n")

	listHeaderText = splitText[:36]
	listBodyText = splitText[37:]

	headerText = ' '.join(listHeaderText)
	bodyText = ' '.join(listBodyText)

	return headerText,bodyText

def writeOutput(input):
	output = open("output.txt",mode="w+",encoding="utf-8")
	output.write(input)
	output.close()

main(filename)
