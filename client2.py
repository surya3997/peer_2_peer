import socket

host = 'localhost'
port = 1107

while True:
    # Create a TCP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (host, port)

##    print("connecting to server at port ", port)
    sock.connect(server_address)

    message = input()

    try:
        sock.sendall(message.encode())

        amount_received = 0
        amount_send = len(message)

##        while amount_received < amount_send:
##            data = sock.recv(16)
##            amount_received += len(data)
##            print("\nReceived data : ", data)
    except:
        print("Data is not sent properly!")
    finally:
##        print("Closing connection")
        sock.close()

