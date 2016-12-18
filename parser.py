#-*- coding: utf-8 -*- 
from bs4 import BeautifulSoup
from urllib.request import urlopen

first_site = urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=651664&weekday=fri').read().decode('utf-8')
soup = BeautifulSoup(first_site, 'html.parser')

next_page=soup.find('a', class_='next')
last_page=next_page.previous_sibling.previous_sibling.string

f=open("C:/Users/hyelee/Desktop/rating2.txt",'w')
"""
page = 1
while page <=int(last_page) : 
	link = 'http://comic.naver.com/webtoon/list.nhn?titleId=651664&weekday=fri&page='+ str(page)
	site=urlopen(link).read().decode('utf-8')
	soup=BeautifulSoup(site,'html.parser')
	rate = soup.find_all('div', class_='rating_type')

	for i in rate : 
		f.write(i.strong.string + "\n")
	
	page+=1
"""

"""
num=int(last_page)
j=1
while num>=1 : 
	link = 'http://comic.naver.com/webtoon/list.nhn?titleId=651664&weekday=fri&page='+ str(num)
	site=urlopen(link).read().decode('utf-8')
	soup=BeautifulSoup(site,'html.parser')
	rate = soup.find_all('div', class_='rating_type')
	rate.reverse()

	for i in rate : 
		f.write(str(j) +" " +i.strong.string + "\n")
		j+=1
	
	num+=-1
	
f.close()
"""
# print(soup.prettify()) whew