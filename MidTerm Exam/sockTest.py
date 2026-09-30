# Create a Python Script that establishes a socket connection #

import socket

def main():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("socket created")

    except socket.error as err:
            print(f"socket failed: {err}")

    try:
        h = "localhost"
        p = 135
        r = s.connect((h, p))   #Connect to socket with h and p as the host and port
        print ("successfully connnected to port") 

    except ConnectionRefusedError as e: #If error connecting to port pop this error
         print(f"Connection Refused: {e}")

    except socket.gaierror as ge:  # If error resolving host pop this error
             print(f"there was an error resolving: {ge}")

    s.close()

    

if __name__ == '__main__':
    main()