import glob, os


#keywords to recognize
tags = [ "@title", "@description", "@expectedResults", "@actualResult", "@dependencies", "@preConditions", "@postConditions"]

def open_file():
	#output file
	output = open("Doc.html","w")
	output.write("<!DOCTYPE html>"+"\n")
	output.write("<body>"+"\n")
	return output

def close_file(file):
	#closing output file
	file.write("\n"+"</body>")
	file.write("\n"+"</html>")
	file.close()
	
def label(lab):
    switcher={
        "title":'Title',
        "description":'Description',
        "expectedResults":'Expected results',
        "actualResult":'Actual result',
        "dependencies":'Dependencies',
        "preConditions":'Pre Conditions',
        "postConditions":'Post Conditions'
    }
    return switcher.get(lab,"error")

#attribute parameter is the attribute to print, second parameter is the line to parse, third parameter is the output stream
def print_attribute(attribute,line,outstream):

	attribute_name = attribute.replace("@","").replace(" ","")


	outstream.write("<tr>"+"\n")

	outstream.write("<th style=\"width:15%; text-align:right; padding-right: 1em; background-color:#DDDDDD;\">"+"\n")
	outstream.write(label(attribute_name)+"\n")
	outstream.write("</th>"+"\n")


	attribute_value = line.replace(attribute,"").replace("*","")

	outstream.write("<th style=\"width:75%; text-align:left; padding-left: 2em;\">"+"\n")
	outstream.write(attribute_value)
	outstream.write("</th>"+"\n")

	outstream.write("</tr>"+"\n")



#MAIN
output = open_file()

#finding all *.java files in the current directory
for sourcefile in glob.glob("*.java"):
	output.write(sourcefile+"\n")
	imported = "<style>@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');</style>"
	output.write(imported);
	style = "<style> th {font-weight: normal} table {border-collapse: collapse; width:100%;} table, th, td {border: 1px solid black;}</style>"
	output.write(style);
	#scanning the sourcefile
	file = open(sourcefile,"r");
	for line in file:

		if("/**" in line):
			output.write("<table style=\"font-family: 'Roboto', sans-serif;\">"+"\n")

		if("*/" in line):
			output.write("</table><br>"+"\n")

		#parsing out all code line
		if("*" in line):

			for tag in tags:
				if(tag in line):
					print_attribute(tag,line,output)



close_file(output)
