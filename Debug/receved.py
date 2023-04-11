import socket
import struct 


#  https://wiki.python.org/moin/UdpCommunication  (site)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 6000))
# mreq = struct.pack("=4sl", socket.inet_aton("255.255.255.255"), socket.INADDR_ANY)

# sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
while True:
    a =(sock.recv(10240))
    print(a)
    # print(a,end=" ")
    
    for byte in a:
        print(byte, end=' ')
    print("__________###___________",end=' ')    
    # break

