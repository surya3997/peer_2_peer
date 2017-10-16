import socket

host = '192.168.43.1'
port = 6000

while True:
    # Create a TCP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (host, port)

    sock.connect(server_address)

    message = input()

    try:
        sock.sendall(message.encode())

        amount_received = 0
        amount_send = len(message)
        
    except:
        print("Data is not sent properly!")
    finally:
        sock.close()

