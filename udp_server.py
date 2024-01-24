import socket

server_address = ('localhost', 5555)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)

print(f"UDP server listening on {server_address}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Дані отримано {client_address}: {data.decode()}")

    response = "Hello, Alex!"
    server_socket.sendto(response.encode(), client_address)
