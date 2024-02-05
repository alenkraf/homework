import socket
import multiprocessing

def handle_client(client_socket):
    data = client_socket.recv(1024)
    client_socket.send(data)
    client_socket.close()

def echo_server():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_process = multiprocessing.Process(target=handle_client, args=(client_socket,))
        client_process.start()

if __name__ == "__main__":
    echo_server()
