import socket
import  sys

def handle(client_sock, client_addr):
    while True:
        client_sock.settimeout(10)
        data = client_sock.recv(4096)
        if data:
            print "received: ", data
            sent = client_sock.send(data)
        else:
            print "disconnect", client_addr
            client_sock.close()
            break
            
def main():
    argc = len(sys.argv)
    if argc < 2:
        print("""
        Usage: echo_server port
        """)
        sys.exit()
    #get port
    porttext = sys.argv[1]
    try:
        port = int(porttext)
    except:
        try:
            port = socket.getservbyname(porttext)
        except socket.gaierror:
            print('port is illegal!')
            sys.exit()
    
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    server_sock.bind((socket.gethostbyname('localhost'), port))
    server_sock.listen(5)
    print "start server:", server_sock.getsockname()
    
    while True:
        try:
            (client_sock, client_addr) = server_sock.accept()
            print "got connection from", client_addr
            handle(client_sock, client_addr)
        except KeyboardInterrupt:
            break
        
if __name__ == "__main__":
    main()
