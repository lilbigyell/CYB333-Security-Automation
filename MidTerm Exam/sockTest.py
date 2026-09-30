# Create a Python Script that establishes a socket connection #

import socket

def main():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #create socket using s variable
        print("socket created")

    except socket.error as se: #If error creating socket pop this error
            print(f"socket failed: {se}")

    try:
        h = "localhost"
        p = 12345
        r = s.connect((h, p))   #Connect to socket with h and p as the host and port
        print (f"successfully connnected to port: {p}") 

    except ConnectionRefusedError as ce: #If error connecting to port pop this error
         print(f"Connection Refused: {ce}")

    except socket.gaierror as ge:   # If error resolving host pop this error
             print(f"there was an error resolving: {ge}")

    s.close()

    

if __name__ == '__main__':
    main()