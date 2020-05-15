import socket

# # TCP SOCKET
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect(('127.0.0.1', 50007))
#     s.sendall(b'Hello')
#     data = s.recv(1024)
#     print(repr(data))
#     print(data)


# UDP SOCKET
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello UDP', ('127.0.0.1', 50007))