import socket


class Client:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((ip_address, port))

    def send_message(self, message):
        self.client_socket.sendall(message.encode())

    def receive_message(self):
        return self.client_socket.recv(1024).decode()

    def run(self):
        # Kết nối đến server
        self.connect()

        # Nhận danh sách dịch vụ
        services = self.receive_message()
        print("Danh sách dịch vụ:")
        print(services)

        # Lựa chọn dịch vụ
        while True:
            service_id = input("Nhập lựa chọn dịch vụ (1-3): ")

            if service_id == "1":
                self.send_message(service_id)
                # Dịch vụ 1: Đảo ngược chuỗi đồng thời in hoa ký tự đầu của mỗi từ
                string = input("Nhập chuỗi: ")
                self.send_message(string)
                result = self.receive_message()
                print("Kết quả:")
                print(result)
            # -------------------------------------------------
            elif service_id == "2":
                # Dịch vụ 2: Tính tổng chuỗi các số nguyên
                integer_list = input("Nhập chuỗi các số nguyên (cách nhau bởi khoảng trắng): ").split()
                self.send_message(" ".join(integer_list))
                result = self.receive_message()
                print("Kết quả: ")
                print(result)
            elif service_id == "3":
                # Dịch vụ 3: Thoát
                break
            else:
                print("Nhập lại!!")

        # Ngắt kết nối
        self.client_socket.close()


if __name__ == "__main__":
    # Khai báo địa chỉ IP và cổng của server
    ip_address = "127.0.0.1"
    port = 8080

    # Tạo client
    client = Client(ip_address, port)

    # Chạy ứng dụng
    client.run()
