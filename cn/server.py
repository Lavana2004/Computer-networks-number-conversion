import socket

def convert_number(number, base):
    if base == 2:
        return bin(int(number))[2:]  
    elif base == 8:
        return oct(int(number))[2:] 
    elif base == 16:
        return hex(int(number))[2:]  
    else:
        return str(number)  

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))  
    server_socket.listen()

    print("Server is listening on port 65432...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected by {addr}")

        data = client_socket.recv(1024).decode()
        if not data:
            break

       
        number, base = data.split(',')
        base = int(base)

        converted_number = convert_number(number, base)
        client_socket.sendall(converted_number.encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()
