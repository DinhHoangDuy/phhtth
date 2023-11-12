import socket

class Server:
    def __init__(self, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', port))
        self.socket.listen(1)

    def listen(self):
        while True:
            connection, address = self.socket.accept()
            self.handle_connection(connection)

    def handle_connection(self, connection):
        data = connection.recv(1024)
        integers = data.decode().split()
        sum = 0
        for integer in integers:
            sum += int(integer)

        response = f'The total string just received is: {sum}'
        connection.send(response.encode())
        connection.close()

if __name__ == '__main__':
    server = Server(5000)
    server.listen()
