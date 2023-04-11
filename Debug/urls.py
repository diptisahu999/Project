from socket import *
s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5)
# print(sys.getrecursionlimit())


m=socket(AF_INET, SOCK_DGRAM)
m.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

m.bind(('0.0.0.0', 6000))