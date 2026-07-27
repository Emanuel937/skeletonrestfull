import socket

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enable broadcast
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Broadcast address and port
broadcast_ip = "172.20.10.15"
port = 5005

# Message
message = b"Hello everyone!"

# Send broadcast
s.sendto(message, (broadcast_ip, port))
print("Broadcast sent!")