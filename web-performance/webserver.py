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
		print "Servidor en Python esta corriendo en el puerto : " + PORT
		httpd.serve_forever()
		
	except (KeyboardInterrupt, SystemExit):
		print "Saliendo..."
		sys.exit
		
	except:
		print "Ha ocurrido un problema al iniciar el servidor en el puerto : " + PORT

runServer()
