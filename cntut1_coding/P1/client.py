import socket
import netifaces as ni

def get_ip_address(interface):
    return ni.ifaddresses(interface)[ni.AF_INET][0]['addr']

def run_client(server_interface='eth0', server_port=65432):
    server_host = get_ip_address(server_interface)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, server_port))
        print(f"Connected to server at {server_host}:{server_port}")
        while True:
            print("\nChoose an action:")
            print("1. Swap case of string")
            print("2. Evaluate arithmetic expression")
            print("3. Reverse string")
            print("4. Exit")            
            choice = input("Enter choice (1-4): ")
            
            if choice == '4':
                break
                
            if choice in ('1', '2', '3'):
                data = input("Enter input: ")
                s.sendall(f"{choice}|{data}".encode())
                response = s.recv(1024).decode()
                print("Result:", response)
            else:
                print("Invalid choice")

if __name__ == "__main__":
    run_client(server_interface='eth0')