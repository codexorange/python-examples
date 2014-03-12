# Importamos librerias para crear el servidor
import SimpleHTTPServer, SocketServer, sys

# Cambiar el puerto segun lo que se recibe de la linea de comandos
PORT = sys.argv[1]

def runServer():
	try:
		# Creamos un manejador de peticiones HTTP
		httpHandler = SimpleHTTPServer.SimpleHTTPRequestHandler

		# Creamos un servidor TCP pasandole el numero del puerto y el objeto httpHandler
		httpd = SocketServer.TCPServer(("", int(PORT)), httpHandler)

		# Imprimimos el mensaje de que el servidor esta corriendo. Se correra con el metodo 
		# serve_forever()
		print "Python Web Server is running at the port " + PORT
		httpd.serve_forever()
	except (KeyboardInterrupt, SystemExit):
		print "Exiting..."
		sys.exit
	except:
		print "There was a problem starting the webserver at port " + PORT

runServer()
