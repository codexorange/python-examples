# Importamos las librerias que se ejecutaran en el Cliente
import webclient, os

# Menu que aparecera en la consola
def menu():
	os.system('cls')
	print """
	======================================================
	WEB PERFORMANCE TESTER
	======================================================
	1 - Test client connection to external web sites
	2 - Test internal web server performance
	3 - Display a log file
	4 - Exit
	======================================================
	"""
	choice = raw_input("\tEnter a choice and press enter : ")
	return choice

# Obtiene el choice
choice = ""
while choice != "4":
	choice = menu()

	if choice == "1":
		os.system("cls")
		sites = []
		print """
		======================================================
		WEB PERFORMANCE TESTER - EXTERNAL SITE CHECK
		======================================================
		"""
		siteResponse = raw_input("Enter the websites to check, separated by spaces: \n\n\t")
		sites = siteResponse.split()
		webclient.checkExternalSites(sites)

	elif choice == "2":
		os.system("cls")
		servers = []
		print """
		======================================================
		WEB PERFORMANCE TESTER - INTERNAL SITE CHECK
		======================================================
		"""
		print """
		Enter the ip addresses of the web servers running
		the Python Webserver, separated by spaces:\n\t"""
		serverResponse = raw_input("\t")
		servers = serverResponse.split()
		port = raw_input("Enter the port the web server is listening on : ")
		webclient.checkInternalSites(servers, port)

	elif choice == "3":
		os.system("notepad logefile.txt")











