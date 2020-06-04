from bs4 import BeautifulSoup as bs

name = input("Insert file name (must be in this directory): ")

html_file = open(name,"r")

soup = bs(html_file, 'html.parser')

outstream = open(name+"_prettified.html","w");
outstream.write(soup.prettify());
