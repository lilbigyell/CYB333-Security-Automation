# Server Script that listens for connections #

import socket



def main():
    s = socket.socket() #Creates Socket Object
    print("Socket Created")

    p = 80   #Port Number

    s.bind(('', p)) #Binds the p variable 12345 as a port to the s socket object
    print(f"Socket bound to port: {p}")


    s.listen(5) #Allows the server to accept connections
    print("Socket is listening")


    while True:
        c, addr = s.accept()    #Assigns the socket accepted connctions to the variables c and addr
        print(f'Got Connection from: {addr}')

        c.send('Thank you for connecting'.encode()) #Sends an encoded message to connection

        c.close()   #closes connection

        break



if __name__ == "__main__":
    main()