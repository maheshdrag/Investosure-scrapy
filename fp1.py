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

url = links[y-1]
uClient = uReq(url)
rsp = uClient.read()
uClient.close()
rsp_soup = soup(rsp,"html.parser")
items = rsp_soup.findAll("div", {"class":"product-content"})
title = items[0].h2.text
tables = items[0].findAll("table", {"class":"table table-curved"})

print(title)
classy = items[0].findAll("h2")
k = 1
for table in tables:
	print(" ")
	print(classy[k].text.encode('utf8').replace("\xe2\x80\x93","").strip())
	print(" ")
	print(" ")
	k = k + 1
	t_row = table.tbody.findAll("tr")
	for t in t_row:
		cols = t.findAll("td")
		for td in cols:
			sa = td.text.encode('utf8').replace("\xe2\x80\x93","").strip()
			print( sa + "||"),
			
		print("")
		




