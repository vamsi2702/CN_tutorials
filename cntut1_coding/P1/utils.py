import netifaces as ni
from datetime import datetime

def get_ip_address(interface='eth0'):
    """Retrieve the IP address of the specified network interface."""
    return ni.ifaddresses(interface)[ni.AF_INET][0]['addr']

def process_request(data):
    """Process incoming client request and return appropriate response."""
    try:
        action, payload = data.split('|', 1)
        if action == '1':
            return payload.swapcase()
        elif action == '2':
            return str(eval(payload))
        elif action == '3':
            return payload[::-1]
        return "Invalid choice"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_client(conn, addr):
    """Handle communication with a connected client."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Connection from {addr}")
    with conn:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            response = process_request(data)
            conn.sendall(response.encode())
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Client {addr} disconnected")
