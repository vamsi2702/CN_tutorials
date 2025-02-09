import socket
import os
from utils import get_ip_address, handle_client

def multi_process_server(interface='eth0', port=65432):
    """Start a multi-process server where each client is handled in a separate process."""
    host = get_ip_address(interface)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Multi-Process Server running on {host}:{port}")
        
        while True:
            conn, addr = server_socket.accept()
            pid = os.fork()
            
            if pid == 0:  # Child process
                server_socket.close()
                handle_client(conn, addr, "Multi-Process")
                os._exit(0)
            else:  # Parent process
                conn.close()

if __name__ == "__main__":
    multi_process_server()
