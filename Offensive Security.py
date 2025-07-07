import socket # The socket module provides access to the BSD socket interface.

def scan_port(ip_address, port):
    """
    Attempts to connect to a specific port on a given IP address.
    Returns True if the port is open, False otherwise.
    """
    try:
        # Create a new socket object
        # AF_INET specifies the address family (IPv4)
        # SOCK_STREAM specifies the socket type (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the connection attempt.
        # This prevents the script from hanging indefinitely if a port is closed or filtered.
        s.settimeout(1)

        # Attempt to connect to the target IP and port.
        # If the connection is successful, the port is likely open.
        result = s.connect_ex((ip_address, port))

        # connect_ex returns 0 if the connection is successful (port is open).
        if result == 0:
            return True
        else:
            return False
    except socket.error as e:
        # Handle potential socket errors (e.g., network unreachable)
        print(f"Socket error: {e}")
        return False
    finally:
        # Ensure the socket is closed whether the connection was successful or not.
        s.close()

def main():
    """
    Main function to get user input and run the port scan.
    """
    print("--- Simple Port Scanner ---")
    print("This tool checks if specific ports are open on a target IP address.")

    target_ip = input("Enter the target IP address (e.g., 127.0.0.1 or a local network IP): ")

    # You can specify a range or a list of common ports
    # For a simple example, let's scan a few common ports.
    ports_to_scan = [21, 22, 23, 80, 443, 8080] # FTP, SSH, Telnet, HTTP, HTTPS, HTTP-Alt

    print(f"\nScanning common ports on {target_ip}...")

    for port in ports_to_scan:
        if scan_port(target_ip, port):
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED/FILTERED")

    print("\nScan complete.")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
