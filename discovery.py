#!/usr/bin/python

#import numpy as np
#import pandas as pd
import os
import xml.etree.ElementTree as ET

from datetime import date

#set date variable
date1 = date.today()
#print(date1)



#network discovery
#cmd = "nmap -v -A 192.168.0.0/24 -oX discovery_%d.xml"%(date1)
#cmd = "nmap -v -A 192.168.0.0/24 -oX discovery_.xml"
#s = os.system(cmd)
#s = os.system("nmap -vv -A 192.168.0.0/24 -oX discovery_.xml")

#parse the discovery.xml file
tree = ET.parse('discovery_.xml')
root = tree.getroot()
root.getchildren()[0].getchildren()
