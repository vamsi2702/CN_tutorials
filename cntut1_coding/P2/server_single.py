import socket
from utils import get_ip_address, handle_client

def single_process_server(interface='eth0', port=65432):
    """Start a single-process server that handles one client at a time."""
    host = get_ip_address(interface)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Single-Process Server running on {host}:{port}")
        
        while True:
            conn, addr = server_socket.accept()
            handle_client(conn, addr, "Single-Process")

if __name__ == "__main__":
    single_process_server()
