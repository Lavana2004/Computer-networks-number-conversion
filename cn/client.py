import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

   
    number = input("Enter a number: ")
    base = input("Enter the base to convert to (2 for binary, 8 for octal, 16 for hexadecimal): ")

   
    message = f"{number},{base}"
    client_socket.sendall(message.encode())

   
    data = client_socket.recv(1024)
    print(f"Converted number: {data.decode()}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
