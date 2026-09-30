# Server Script that listens for connections #

import socket



def main():
    s = socket.socket()
    print("Socket Created")

    p = 12345

    s.bind(('', p))
    print(f"Socket binded to: {p}")


    s.listen(5)
    print("Socket is listening")


    while True:
        c, addr = s.accept()
        print(f'Got Connection from: {addr}')

        c.send('Thank you for connecting'.encode())

        c.close()

        break



if __name__ == "__main__":
    main()