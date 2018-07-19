import bs4
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
url = 'https://www.bankbazaar.com/insurance/life-insurance.html'
uClient = uReq(url)
rsp = uClient.read()
uClient.close()
rsp_soup = soup(rsp,"html.parser")
items = rsp_soup.findAll("div", {"class":"item"})

links = []
x=0;
for item in items:
	c_name = item.findAll("li", {"class":"insurance-info-row"})
	for name_one in c_name:
		name = name_one.div.a['title']
		links.append(name_one.div.a['href'])
		solve = name_one.findAll("div", {"class":"info-coverage"})
		settle = name_one.findAll("div", {"class":"info-expense"})
		max_sa = name_one.findAll("div", {"class":"info-copay"})
		age = name_one.findAll("div", {"class":"info-preexist"})
		x = x+1
		print(str(x) +") Seller:" + name +" ||" + "Settlement:"+ settle[0].text +"||" + "Max_Sum_Assured:"+ max_sa[0].text + "||" + "Max_Age:" + age[0].text)

print("Enter the No to know more")
y = input()
13
url = links[y-1]
uClient = uReq(url)
rsp = uClient.read()
uClient.close()
rsp_soup = soup(rsp,"html.parser")
items = rsp_soup.findAll("div", {"class":"product-content"})
title = items[0].h2.text
tables = items[0].findAll("table", {"class":"table table-curved"})
x=0
print(title)
for table in tables:
	t_row = table.tbody.findAll("tr")
	for i in t_row:
		try:
			plan = i.td.strong.text
			if (plan!='Plan' and plan != 'Year' and plan!='Plan Type'): 
				sum_assured = i.findAll("td")
				sa = sum_assured[1].text.encode('utf8')
				sa = sa.replace("\xe2\x80\x93","")
				tp = sum_assured[2].text.encode('utf8')
				tp = tp.replace("\xe2\x80\x93","")
				x = x + 1
				print(str(x) +") Policy:" + plan+" || "   +"||" + "Sum_Assured:"+ sa + "Term:"+ tp)
		except Exception as exp:
			print ("End")














