from selenium import webdriver
from bs4 import BeautifulSoup
import time
import string
import re
import codecs
f = codecs.open("velocityhall.csv","w","utf-8")
browser = webdriver.Chrome()
browser.get("https://velocityhall.com/accela/velocityhall/?CFID=6947742&CFTOKEN=18197820&jsessionid=A87CC3F82366913AEEA8058135A15F0A")
browser.find_element_by_name("submit").click()
browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr[1]/td[2]/table[2]/tbody/tr[2]/td[1]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/p/a").click()
browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr[1]/td[2]/table[3]/tbody/tr/td[2]/ul/li[1]/a").click()
alpha = string.uppercase
for letter in alpha:
	browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr[1]/td[2]/form/table/tbody/tr[4]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[3]/input").send_keys("%s"%letter)
	browser.find_element_by_name("Submit").click()
	links = browser.find_elements_by_xpath("/html/body/div/table[2]/tbody/tr[1]/td[2]/table[3]/tbody/tr/td/a")
	soup = BeautifulSoup(browser.page_source)
	total = soup.find("td",{"class":"HighlightTextInvert"})
	top = total.text.rsplit(" ")
	asdf = top[-1]
	numb = int(asdf)
	x = 0
	while x < numb:
		for i in range(3,13):
			try:
				addr = browser.find_element_by_css_selector("body > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2) > table:nth-child(8) > tbody > tr:nth-child(%d) > td > a"%i)
				addr.click()
				perms = browser.find_elements_by_css_selector("body > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2) > table:nth-child(8) > tbody > tr > td:nth-child(1) > a")
				for z in perms:
					try:
						z.click()
						soup = BeautifulSoup(browser.page_source)
						td = soup.findAll("td",{"width":"47%"},{"valign":"top"})
						info = []
						for ok in td:
							content = re.sub("\n\s\s*","",ok.text.strip())
							info.append(content)
						print "\"" + "\",\"".join(info) + "\"\n"
						f.write("\"" + "\",\"".join(info) + "\"\n")	
						browser.back()
					except:
						continue
				time.sleep(1)
				browser.back()
			except:
				pass
		browser.find_element_by_css_selector("body > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2) > table:nth-child(8) > tbody > tr:nth-child(13) > td:nth-child(2) > table > tbody > tr > td:nth-child(1) > form").click()
		x = x + 10
		print x, numb
