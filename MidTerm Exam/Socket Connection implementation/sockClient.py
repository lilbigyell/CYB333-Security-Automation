import socket


def main():
    s = socket.socket() #Creates Socket object
    p = 12345   # Port Number


    try:
        s.connect(('localhost', p)) #connects to localhost 127.0.0.1 and the p variable 12345
        print(s.recv(1024).decode())    #prints the received message from the socket and decodes it

    except ConnectionRefusedError as ce:    #if a connnection error pops up this will handle it
        print(f"Connection Error: {ce}")

    s.close()   #Closes Socket Object

if __name__ == "__main__":
    main()