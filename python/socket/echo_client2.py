#!/bin/bash python
import  socket
import  sys


def create_client(conn,timeout):
    cli = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    try:
        cli.settimeout(timeout)
        cli.connect(conn)
    except socket.error as err:
        print('cant connect to the server',err)
        sys.exit()
    return  cli

def do_client(cli):
    #cli = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    while   True:
        try:
            data = raw_input('>>>')
            if  data.lower() == 'end':
                print('Bye!')
                break
            cli.send(data)
            print("echo->>"+cli.recv(512).decode('utf-8'))
        except  socket.error as err:
            print(err)
        except  NameError as err:
            print(err,"need a string")
            continue

def main():
	argc = len(sys.argv)
	if  argc < 3:
		print("""
		Usage : echo_client ipaddr port
		""")
		sys.exit()
	ipaddr = sys.argv[1]
	porttext = sys.argv[2]
    #get port
	try:
		port = int(porttext)
	except:
		try:
			port = socket.getservbyname(porttext)
		except socket.gaierror :
			print('port is illeagl')
			sys.exit()

	i = 0
	while   i<100:
		#port = socket.getservbyname('echo')
		cli=create_client((ipaddr,port),5)
		print(cli.getpeername())
		do_client(cli)
		cli.close()
		input()
		i += 1
    #sys.stdout.close()
    #sys.stdout = oldstdout
    
main()