import socket

server_address = ('localhost', 5555)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "connection successful"
client_socket.sendto(message.encode(), server_address)

data, server_address = client_socket.recvfrom(1024)
print(f"Відповідь сервера: {data.decode()}")

client_socket.close()
