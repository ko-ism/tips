"""
ウェルノウンポート番号：0-1023
登録済み：1034-49151
静的・プライベート　ポート番号：49152-65535
"""

import socket

# # TCP SOCKET
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('127.0.0.1', 50007))
#     s.listen(1)
#     while True:
#         conn, addr = s.accept()
#         with conn:
#             while True:
#                 data = conn.recv(1024)
#                 if not data:
#                     break
#                 print('data:{}, addr:{}'.format(data, addr))
#                 conn.sendall(b'Received: ' + data)


# UDP SOCKET
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    while True:
        data, addr  = s.recvfrom(1024)
        if not data:
            break
        print('data:{}, addr:{}'.format(data, addr))