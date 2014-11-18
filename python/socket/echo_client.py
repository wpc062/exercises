import socket
import sys

def do_client(cli):
    while True:
        try:
            data = raw_input('>>>')
            if  data.lower() == 'end':
                print('Bye!')
                break
            cli.send(data)
            print("echo->>" + cli.recv(512).decode('utf-8'))
            
        except  socket.error as err:
            print(err)
        except  NameError as err:
            print(err,"need a string")
            continue

def main():
    if len(sys.argv) < 3:
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
        print('port is illeagl')
        sys.exit()

    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cli.settimeout(5)
        cli.connect((ipaddr, port))
    except socket.error as err:
        print("can't connect to the server",err)
        sys.exit()

    print"connect to: ", cli.getpeername()

    do_client(cli)
    cli.close()

if __name__ == "__main__":
    main()
