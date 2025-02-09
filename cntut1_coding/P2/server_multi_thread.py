import socket
import threading
from utils import get_ip_address, handle_client

def multi_threaded_server(interface='eth0', port=65432):
    """Start a multi-threaded server where each client is handled in a separate thread."""
    host = get_ip_address(interface)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Multi-Threaded Server running on {host}:{port}")
        
        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr, "Multi-Threaded"))
            thread.start()

if __name__ == "__main__":
    multi_threaded_server()
