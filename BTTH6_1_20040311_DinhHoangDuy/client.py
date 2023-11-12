#=============CLIENT=============
import socket

HOST = "localhost"
PORT = 5000

def send_integers(conn, integers):
    """
    Sends a string of integers to the server.

    Args:
        conn: The server connection socket.
        integers: A list of integers to send.
    """

    data = ""
    for integer in integers:
        data += str(integer) + " "

    # Remove the trailing space.
    data = data[:-1]

    # Send the data to the server.
    conn.sendall(data.encode())

def receive_sum(conn):
    """
    Receives the sum of the integers from the server.

    Args:
        conn: The server connection socket.
    """

    data = conn.recv(1024)

    # Decode the data into an integer.
    sum = int(data.decode())

    return sum

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            # Get the integers from the user.
            integers = []
            while True:
                integer_input = input("Enter an integer: ")

                if integer_input == ".":
                    break

                integer = int(integer_input)
                integers.append(integer)

            # If the user enters ".", exit the loop.
            if integers == ["."]:
                break

            # Send the integers to the server.
            send_integers(s, integers)

            # Receive the sum from the server.
            sum = receive_sum(s)

            # Print the sum.
            print("The sum of the integers is:", sum)

            # Ask the user if they want to continue or exit.
            continue_or_exit = input("Do you want to continue (y/n)? ")

            if continue_or_exit != "y":
                break

if __name__ == "__main__":
    main()
