import netifaces as ni
from datetime import datetime
import socket
import threading
import os
import time
import netifaces as ni

def get_ip_address(interface='eth0'):
    """Retrieve the IP address of the specified network interface."""
    return ni.ifaddresses(interface)[ni.AF_INET][0]['addr']

def handle_client(conn, addr, server_type, worker_info=""):
    try:
        with conn:
            data = conn.recv(1024).decode()
            time.sleep(3)  
            reversed_str = data[::-1]
            conn.sendall(reversed_str.encode())
    finally:
        print(f"{worker_info} - Completed {addr}")
