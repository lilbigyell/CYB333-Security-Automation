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
        s.settimeout(0.0001)
        result = s.connect_ex((self.ip, port))
        print(f'Port {port}:   {result}')
        s.close()
        return result == 0

    def write(self, filepath):
        pass

@timefun
def main():
    ip = '192.168.0.234'
    scanner = Scanner(ip)
    scanner.scan(1,1000)
    print(scanner.open_ports)

if __name__ == '__main__':
    main()