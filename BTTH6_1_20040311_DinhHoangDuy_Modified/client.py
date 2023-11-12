import socket

def export_calculations(calculations):
        with open('calculations.txt', 'w') as f:
            for calculation in calculations:
                f.write(str(calculation) + '\n')

def validate_user_input(input):
    if input.isdigit() or input == '.':
        return True
    else:
        return False

class Client:
    def __init__(self, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('localhost', port))

    def send_data(self, data):
        self.socket.send(data.encode())

    def receive_data(self):
        data = self.socket.recv(1024)
        return data.decode()

    def close(self):
        self.socket.close()


def main():
    client = Client(5000)

    calculations = []

    while True:
        number = input('Enter a number (or "." to stop): ')

        if not validate_user_input(number):
            print('Invalid input. Please enter a number or ".".')
            continue

        if number == '.':
            break

        # Convert the string input to an integer
        number = int(number)

        calculations.append(number)

    client.close()

    # Calculate the sum of the numbers
    sum = 0
    for number in calculations:
        sum += number

    # Display the sum to the user
    print(f'The sum of the numbers is: {sum}')

    # Ask the user if they want to continue
    continue_app = input('Do you want to continue?(y/n): ')

    # If the user says yes, keep the app running
    if continue_app == 'y':
        main()
    # Else, exit the app and export the calculations
    else:
        export_calculations(calculations)
        exit()

if __name__ == '__main__':
    main()

