#!/usr/bin/env python
# -*- coding: utf-8 -*-

#testing get commit from raspi
# Testing 123

from bs4 import BeautifulSoup
import urllib2
import codecs

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

    # Print each line of the list on its own.
    #for i in incidents:
    #    print i
    #    print "=============================="
    #print incidents
    write_file(incidents)

def write_file(incidents):
    file = codecs.open("/var/www/911.txt", "w", encoding="UTF-8")
    incidents2 = []
    print incidents
    for i in incidents:
        i.replace(u"Â ", "")
        incidents2.append(i)
    print incidents2
    for i in incidents2:
        file.write(i + "\n")
    #for i in incidents:
    #    file.write(i + "\n")
    #    print i
    file.close()

get_incidents()

