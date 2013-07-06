#testing get commit from raspi

from bs4 import BeautifulSoup
import urllib2

#this url is the middle frame with the incident list at lafayette911.org
url = "http://67.32.159.27/webcad/webcad.asp"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

#test for now to just find links since incidents are down at the moment
incidents = soup.find_all('a')

for links in incidents:
  print(links.get('href'))


