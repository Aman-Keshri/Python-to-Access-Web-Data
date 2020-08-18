import urllib.request
from bs4 import BeautifulSoup

sample_url = "http://python-data.dr-chuck.net/comments_42.html"
data_url = "http://py4e-data.dr-chuck.net/comments_906449.html"

#Getting the html information and parsing it with BeautifulSoup
html = urllib.request.urlopen(data_url).read()
soup = BeautifulSoup(html)

#Getting a list with the "span" tags
tags = soup('span')

#Counting the sum of all the values within the span tags
count = 0
for tag in tags:
	
	#We need to cast them to int, as they're parsed as text strings
	count += int(tag.contents[0])

print(count)