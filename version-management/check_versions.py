import sys
import telnetlib

def check_java(host, user, password):
	java_version = ""
	tn = telnetlib.Telnet(host)
	tn.read_until("Login:")
	tn.write(user + "\n")

	if password:
		tn.read_until("Password: ")
		tn.write("\n")

	tn.write("java -version\n")
	tn.write("exit\n")
	result = tn.read_all()
	result_list = result.split("\n")

	for line in result_list:
		if line.startswith("java version"):
			java_version = line[14:21]

	return java_version

def check_python(host, user, password):
	python_version = ""
	tn = telnetlib.Telnet(host)
	tn.read_until("Login:")
	tn.write(user + "\n")

	if password:
		tn.read_until("Password: ")
		tn.write("\n")

	tn.write("python -V\n")
	tn.write("exit\n")
	result = tn.read_all()
	result_list = result.split("\n")

	for line in result_list:
		if line.startswith("python version"):
			python_version = line[7:]

	return python_version

def check_perl(host, user, password):
	perl_version = ""
	tn = telnetlib.Telnet(host)
	tn.read_until("Login:")
	tn.write(user + "\n")

	if password:
		tn.read_until("Password: ")
		tn.write("\n")

	tn.write("perl -version\n")
	tn.write("exit\n")
	result = tn.read_all()
	result_list = result.split("\n")

	for line in result_list:
		if line.startswith("perl version"):
			perl_version = line[15:20]

	return perl_version