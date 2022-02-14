import socket
from threading import Thread
from datetime import datetime
SERVER_HOST = input("Enter Server address: ")
SERVER_PORT = int(input("Enter Port: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[+] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
server.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
name = input("Enter your name: ")
def listen_for_messages():
    while True:
        message = server.recv(1024).decode()
        print("\n" + message)

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send =  input(">>> ")
    if to_send.lower() == 'q':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"[{date_now}] {name}: {to_send}"
    server.send(to_send.encode())

# close the socket
server.close()