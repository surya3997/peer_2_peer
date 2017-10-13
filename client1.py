import socket

host = 'localhost'
port = 1107

while True:
    # Create pa TCP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (host, port)

    sock.connect(server_address)

    message = input()

    try:
        sock.sendall(message.encode())

        amount_received = 0
        amount_send = len(message)

##        while amount_received < amount_send:
##            data = sock.recv(16)
##            amount_received += len(data)
    except:
        print("Data is not sent properly!")
    finally:
        sock.close()

