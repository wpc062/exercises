import  socket
import  sys

class   EchoServer:
    def __init__(self,ipaddr='127.0.0.1',port=7,backlog=10):
        self.ipaddr = ipaddr
        self.port = port
        self.buflen = 512
        self.backlog = backlog
        
    def _create(self):
        print(self.port)
        try:
            self.ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
            self.ser.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
            #self.ser.setblocking(True)
            self.ser.settimeout(1)
            self.ser.bind((self.ipaddr,self.port))
            self.ser.listen(self.backlog)
        except socket.error as err:
            print('cant create a server',err)
            sys.exit()
            
    def run(self):
        self._create()
        while   True:
            try:
                cli = self.ser.accept()
                print('got a client')
                self._send_to_kid(cli)
            except KeyboardInterrupt:
                break
            except:
                continue
        return  0
    
    def close(self):
        self.ser.close()
        try:
            while os.wait():
                pass
        except  ChildProcessError:
            pass
        
    def _do_echo(self,cli):
        print('new kid')
        sys.stdout.flush()
        while   True:
            try:
                rec = cli.recv(5)
                print("echo : "+rec.decode('utf-8'))
                cli.send(rec)
            except  socket.error as err:
                print(err)
                continue
            except:
                print(err)
        cli.shutdown(socket.SHUT_RDWR)
        print('a client is outline')
        sys.stdout.flush()
    
    def _send_to_kid(self,cli):
        pid = os.fork()
        if  pid < 0:
            print('cant fork a child process')
            return  -1
        elif pid > 0:
            os.wait()
        else:
            pid = os.fork()
            if  pid == 0 :
                self._do_echo(cli)
            elif  pid > 0:
                sys.exit()


def main():
    argc = len(sys.argv)
    if  argc < 3:
        print("""
        Usage : echo_server ipaddr port
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
    #get connection
    try:
        echo = EchoServer(ipaddr,port,10)
        echo.run()
        echo.close()
    except  KeyboardInterrupt:
        print('server stop')

main()