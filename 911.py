#testing get commit from raspi

from bs4 import BeautifulSoup
import urllib2

#this url is the middle frame with the incident list at lafayette911.org
url = "http://67.32.159.27/webcad/webcad.asp"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

# Create an emapty list for incidents
incidents = []

# Find the second table which has the incidents and find the individual rows.
for i in soup.findAll('table')[1].findAll('tr'):
    incidents.append(i.get_text()) # Add the text from the row to the list

# Print each line of the list on its own.
for i in incidents:
   print i
