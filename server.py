import socket
import json
import uuid
from database import create_database, save_application

HOST = "127.0.0.1"
PORT = 5200

def start_server():
    create_database()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Server running on {HOST}:{PORT}... waiting for clients...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected to: {addr}")

        try:
            data = client_socket.recv(4096).decode()
            if not data:
                client_socket.close()
                continue

            form = json.loads(data)
            reg_id = str(uuid.uuid4())
            save_application(reg_id, form)
            client_socket.send(f"Your registration ID: {reg_id}".encode())

        except json.JSONDecodeError:
            client_socket.send("Error: Invalid JSON received.".encode())
        except Exception as e:
            client_socket.send(f"Error: {e}".encode())
        finally:
            client_socket.close()


if __name__ == "__main__":
    start_server()
