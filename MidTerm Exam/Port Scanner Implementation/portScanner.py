import socket
from utilities import timefun

class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = [];

    def __repr__(self):
        return (f'Scanner: {self.ip}')

    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
                if(self.is_open(port)):
                    self.add_port(port)

    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.settimeout(0.1)
        result = s.connect_ex((self.ip, port))
        s.close()
        return result == 0

    def write(self, filepath):
        pass

class Grabber:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(.1)  
        self.socket.connect((self.ip, self.port))


    def read(self, length=1024):
        return self.socket.recv(length)

    def close(self):
        self.socket.close()


@timefun
def main():
    ip = 'scanme.nmap.org'
    scanner = Scanner(ip)
    scanner.scan(1,443)
    print('Open Ports;',scanner.open_ports)

    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip, port)
            print(grabber.read())
        except TimeoutError as to:
            print(f"Port: {port} timed out before grabbing")

if __name__ == '__main__':
    main()