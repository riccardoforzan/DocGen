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

#attribute parameter is the attribute to print, second parameter is the line to parse, third parameter is the output stream
def print_attribute(attribute,line,outstream):

	attribute_name = attribute.replace("@","").replace(" ","")


	outstream.write("<tr>"+"\n")

	outstream.write("<th>"+"\n")
	outstream.write(attribute_name+"\n")
	outstream.write("</th>"+"\n")


	attribute_value = line.replace(attribute,"").replace("*","").replace(" ","")

	outstream.write("<th>"+"\n")
	outstream.write(attribute_value)
	outstream.write("</th>"+"\n")

	outstream.write("</tr>"+"\n")



#MAIN
output = open_file()

#finding all *.java files in the current directory
for sourcefile in glob.glob("*.java"):
	output.write("<b>"+sourcefile+"</b>"+"\n")

	#scanning the sourcefile
	file = open(sourcefile,"r");
	for line in file:

		if("/**" in line):
			output.write("<table>"+"\n")

		if("*/" in line):
			output.write("</table>"+"\n")

		#parsing out all code line
		if("*" in line):

			for tag in tags:
				if(tag in line):
					print_attribute(tag,line,output)



		print(line);

close_file(output)

