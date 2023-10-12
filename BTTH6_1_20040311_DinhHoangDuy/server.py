#=============SERVER=============
import socket
import threading
HOST = "localhost"
PORT = 5000

def handle_client(conn):
    """
    Handles a single client connection.

    Args:
        conn: The client connection socket.
    """

    while True:
        try:
            # Receive the string of integers from the client.
            data = conn.recv(1024)

            # If the client sends ".", exit the loop.
            if data == b".":
                break

            # Decode the string of integers into a list of integers.
            integers = [int(integer) for integer in data.decode().split()]

            # Calculate the sum of the integers.
            sum = 0
            for integer in integers:
                sum += integer

            # Send the sum back to the client.
            conn.sendall(str(sum).encode())
        except ConnectionAbortedError:
            # The client has closed the connection abruptly.
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()

        # Handle the client connection in a separate thread.
        threading.Thread(target=handle_client, args=(conn,)).start()
