#-*- coding : utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen

f = open('C:/Users/Hyelee/Desktop/ratings3.txt','w')
num=1
while num<=70 :
	link = 'http://comic.naver.com/webtoon/detail.nhn?titleId=651664&no=' + str(num) + '&weekday=fri'
	site = urlopen(link).read().decode('utf-8')
	soup=BeautifulSoup(site, 'html.parser')

	rate_tag = soup.find('span', id="bottomPointTotalNumber")
	rate=rate_tag.string
	f.write(str(num) +" "+ rate +"\n")
	num+=1

f.close()
