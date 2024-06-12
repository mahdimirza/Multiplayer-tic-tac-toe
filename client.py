# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 34134  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True: 
        data = s.recv(4096)
        data = data.decode() 
        if data:
            if 'wait' in data or 'opponent' in data:
                print(data)
                continue
            elif 'end' in data:
                print(data)
                break
            else:
                print(data)
                msg = input('(->)')
                s.send(msg.encode())
        


    s.close()


 