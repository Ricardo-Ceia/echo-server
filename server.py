import socket
import threading

HOST = "127.0.0.1"
PORT = 65432


def handle_client(conn,addr):
    print(f"Connected to addr:{addr}")
    with conn:
        while True:
            message = conn.recv(1024)
            #Stop Connetions on empy messages use strip cause telnet client adds \n\r to end of messages
            if not message.decode(encoding="utf-8").strip():
                print(f"Connection closed with:{addr}")
                break
            conn.sendall(message)  

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    #To remove TCP´s TIME_wAIT state
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((HOST,PORT))
    s.listen()
    while True:
        conn,addr = s.accept()
        t = threading.Thread(target=handle_client,args=(conn,addr))
        #Set the thread as a daemon (similar to detach in C)
        t.daemon = True
        t.start()
