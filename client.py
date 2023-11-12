import socket
import os

def get_data_from_keyboard():
    data_to_send = ""
    while True:
        data = input("Nhập chuỗi các số nguyên (nhập '.' để kết thúc): ")
        data_to_send += data + "\n"
        if "." in data:
            print("Đã nhập dấu chấm. Kết thúc nhập liệu.")
            break
    return data_to_send.strip()

def get_data_from_specified_file():
    filename = input("Bạn muốn nhận dữ liệu từ file nào? ")
    if not os.path.exists(filename):
        print(f"File '{filename}' không tồn tại. Vui lòng kiểm tra lại.")
        return ""
    with open(filename, "r") as file:
        return file.read().strip()

# Tạo một socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối đến server
client_socket.connect(("localhost", 12345))

while True:
    print("\nMenu:")
    print("1. Nhập dữ liệu từ bàn phím")
    print("2. Nhập dữ liệu từ file")
    print("3. Thoát")
    choice = input("Chọn (1/2/3): ")

    if choice == "1":
        data_to_send = get_data_from_keyboard()
    elif choice == "2":
        data_to_send = get_data_from_specified_file()
        if not data_to_send:
            continue
    elif choice == "3":
        print("Thoát.")
        client_socket.send("EXIT".encode())
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        continue

    # Gửi dữ liệu đến server
    client_socket.send(data_to_send.encode())
    print("Dữ liệu đã được gửi đến server.")

    # Nhận kết quả từ server
    response = client_socket.recv(1024).decode()
    print("Kết quả từ server:")
    print(response)

# Đóng kết nối
client_socket.close()
