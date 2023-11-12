import socket
import threading

def handle_client(client_socket):
    while True:
        # Nhận dữ liệu từ client
        data = client_socket.recv(1024).decode()

        if data.strip() == "EXIT":
            print("Nhận yêu cầu thoát. Đóng kết nối với client.")
            break

        print(f"Nhận dữ liệu: {data}")

        # Đảo ngược chuỗi
        reversed_data = data[::-1]
        print(f"Chuỗi sau khi đảo ngược: {reversed_data}")

        # Gửi kết quả về cho client
        client_socket.send(reversed_data.encode())

    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen()

print("Server đang chờ kết nối từ client...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Kết nối từ {client_address} đã được chấp nhận.")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
