import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode()

        if data.strip() == "EXIT":
            print("Nhận yêu cầu thoát. Đóng kết nối với client.")
            break

        print(f"Nhận dữ liệu: {data}")

        with open("data.txt", "a") as file:
            file.write(data + "\n")

        print("Dữ liệu đã được lưu vào file data.txt.")

        lines = data.strip().split("\n")
        responses = []

        for line in lines:
            if '.' in line:
                break
            numbers = list(map(int, line.split()))
            total = sum(numbers)
            result = f"Tổng của chuỗi {line} là: {total}"
            responses.append(result)

        response = "\n".join(responses)

        client_socket.send(response.encode())

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
