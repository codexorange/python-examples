# Importamos las librerias que usaremos
from urllib2 import urlopen
import socket, sys, time, datetime

socket.setdefaulttimeout(15)

def checkExternalSites(sites):
	logfile = open("logfile.txt", "a")
	logtime = time.strftime("\n%a, %d %b %Y %H: %M: %S")
	print logtime
	logfile.write(logtime + "\n")

	for site in sites:
		try:
			start = time.time()
			data = urlopen("http://" + site)
			stuff = data.read()
			end = time.time()
			difference = end - start
			output = "Site %s took %2.2f seconds to load" %(site, difference)
			logfile.write(logtime + "\n")
			print output
			