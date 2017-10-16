import socket
import time
import threading
from random import randint

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(160)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = data.decode()
                    print(response) 
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    port = 3997

    host = 'localhost'

    while True:
        # Create a TCP Socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = (host, port)

        try:
            sock.connect(server_address)
        except:
            time.sleep(randint(1, 5))
            print("acting as server")
            ThreadedServer('', port).listen()

        print("acting as client : ")
        message = input()

        try:
            sock.sendall(message.encode())

            amount_received = 0
            amount_send = len(message)
        except:
            print("Data is not sent properly!")
        finally:
            sock.close()

