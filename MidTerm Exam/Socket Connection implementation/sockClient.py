import socket


def main():
    s = socket.socket()
    p = 12345


    try:
        s.connect(('localhost', p))
        print(s.recv(1024).decode())

    except ConnectionRefusedError as ce:
        print(f"Connection Error: {ce}")

    s.close()

if __name__ == "__main__":
    main()