#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2

#this url is the middle frame with the incident list at lafayette911.org
url = "http://67.32.159.27/webcad/webcad.asp"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

def get_incidents():
    # Create an emapty list for incidents
    incidents = []

    # Find the second table which has the incidents and find the individual rows.
    for i in soup.findAll('table')[1].findAll('tr'):
        incidents.append(i.get_text()) # Add the text from the row to the list
    # Write out the result to a file.
    write_file(incidents)

def write_file(incidents):
    file = open("/var/www/911.txt", "w")
    for i in incidents[1:]:
        print i
        file.write(i.encode('ascii', 'ignore') + "\n")
    file.close()

get_incidents()

