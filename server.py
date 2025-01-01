import socket

HOST = "127.0.0.1"
PORT = 65432


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    #To remove TCP´s TIME_wAIT state
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((HOST,PORT))
    s.listen()
    conn,addr = s.accept()
    with conn:
        while True:
            message = conn.recv(1024)
            #Stop Connetions on empy messages use strip cause telnet client adds \n\r to end of messages
            if not message.decode(encoding="utf-8").strip():
                break
            conn.sendall(message)


'''

'b\n\r'
 in reality 

b''
in reality


'''