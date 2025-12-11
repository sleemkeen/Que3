import socket
import json
import uuid
from database import create_database, save_application

HOST = "127.0.0.1"
PORT = 5200

def start_server():
    create_database()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print("Server running... waiting for clients...")

    while True:
        client_socket, addr = server_socket.accept()
        print("Connected to:", addr)

        data = client_socket.recv(4096).decode()
        if not data:
            client_socket.close()
            continue

        try:
            form = json.loads(data)
        except:
            client_socket.send("Invalid JSON received.".encode())
            client_socket.close()
            continue

        reg_id = str(uuid.uuid4())
        save_application(reg_id, form)
        client_socket.send(f"Your registration ID: {reg_id}".encode())
        client_socket.close()


if __name__ == "__main__":
    start_server()
