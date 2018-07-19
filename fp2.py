import sys, string, os, subprocess
from bs4 import BeautifulSoup
import re

#case insensitive search
regex = r"FUND MANAGER(.*?):(.*?)experience"

def prc_child(data,pos):
	x = data[pos:len(data)+15]
	matches = re.search(regex, x, re.DOTALL| re.IGNORECASE)
	if matches:
    		#print matches.group()
		y = matches.group(1)
		pattern = re.compile("fund manager", re.IGNORECASE)
		pattern1 = re.compile(r"\((.*?)\)") #remove wef etc etc
		y = pattern.sub("", y)
		y = pattern1.sub("", y)
		z = matches.group(2)
		z = pattern1.sub("", z)
		z += "experience"
		y += z
		print y
		#print matches.group(1)
		#print matches.group(2)
		text_file = open("c:\\Python27\\dello\\o.txt", "a")
		text_file.write( y.encode('utf8'))
		text_file.write( "\n")
		text_file.close()
		return 'jumbo'
	else:
		print ("No Match Found")
	
def prc(data):#traverse the para and check for matches
	for i in para:
		y = data.find(i)
		if(y>=0):
			return prc_child(data,y)
	

para = ["FUND MANAGER"]


for i in range(4,6):
	os.chdir('c:\\Python27\\dello')
	print ("page No" + str(i) )
	stringer = "c:\\Python27\\dello\\pdf2htmlEX.exe i.pdf -f "+ str(i) +" -l "+ str(i)
	os.system(stringer)
	soup = BeautifulSoup(open("C:\\Python27\\dello\\i.html"), "html.parser")
	for city in soup.find_all('div'):
		x = city.text.strip()
		if(prc(x)=='jumbo'):
			break