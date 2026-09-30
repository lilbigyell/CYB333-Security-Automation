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

    except socket.gaierror:
         print("there was an error resolving")


    try:
        r = s.connect((h, p))
        print ("successfully connnected to port")
        print(f"Result is: {r}")
        

    except ConnectionRefusedError as e:
         print(f"Connection Refused: {e}")

    s.close()

    






if __name__ == '__main__':
    main()