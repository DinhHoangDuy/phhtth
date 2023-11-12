import socket
import threading


class Server:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip_address, port))
        self.server_socket.listen(5)

        print("Server đang hoạt động tại địa chỉ IP {} và cổng {}".format(ip_address, port))

    def run(self):
        while True:
            connection, address = self.server_socket.accept()
            print("Client {} đã kết nối".format(address))

            # Khởi tạo thread để xử lý yêu cầu của client
            thread = threading.Thread(target=self.handle_client, args=(connection,))
            thread.start()

            if False:
                print("Client {} đã ngắt kết nối".format(address))
    def handle_client(self, connection):
        while True:
            # Gửi danh sách dịch vụ đến client
            connection.sendall("1. Đảo ngược chuỗi đồng thời in hoa ký tự đầu của mỗi từ\n"
                             "2. Tính tổng chuỗi các số nguyên\n"
                             "3. Thoát\n".encode())

            # Nhận lựa chọn dịch vụ từ client
            service_id= connection.recv(1024).decode()


            if service_id == "1":
                # Dịch vụ 1: Đảo ngược chuỗi đồng thời in hoa ký tự đầu của mỗi từ
                string = connection.recv(1024).decode()
                connection.sendall(string[::-1].title().encode())

            elif service_id == "2":
                # Dịch vụ 2: Tính tổng chuỗi các số nguyên
                # integer_list = connection.recv(1024).decode().split()
                integer_list = connection.recv(1024).decode()
                total = 0
                for integer in integer_list:
                    total += int(integer)
                connection.sendall(str(total).encode())
                # result = connection.recv(1024).decode()
            elif service_id == "3":
                # Dịch vụ 3: Thoát
                break

        connection.close()


if __name__ == "__main__":
    server = Server("127.0.0.1", 8080)
    server.run()
