import socket
import netifaces as ni
import sys
def get_ip_address(interface):
    return ni.ifaddresses(interface)[ni.AF_INET][0]['addr']

def run_client(server_interface='eth0', server_port=65432):
    try:
        server_host = get_ip_address(server_interface)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_host, server_port))
            s.sendall("vamsi".encode())
            response = s.recv(1024).decode()
            print("Result:", response)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
if __name__ == "__main__":
    run_client(server_interface='eth0')