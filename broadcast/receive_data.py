import socket

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to all interfaces on port 5005
s.bind(("", 5005))

print("Listening for broadcast messages...")
while True:
    data, addr = s.recvfrom(1024)
    print(f"Received message from {addr}: {data.decode()}")