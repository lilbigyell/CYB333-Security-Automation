import socket


def main():
    s = socket.socket()

    p = 12345


    s.connect(('localhost', p))

    print(s.recv(1024).decode())

    s.close()

if __name__ == "__main__":
    main()