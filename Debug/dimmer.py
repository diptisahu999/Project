import socket
s=socket.socket()

host='127.0.0.1'
port=6000
s.bind((host,port))
# print("ok")
s.listen(2)
conn,addr=s.accept()
print(addr,"as connected")
while 1:
    message=input(str("you:>>"))
    message=message.encode()
    conn.send(message)
    incoming_message=conn.recv(1025)
    incoming_message=incoming_message.decode()
    print(("clint:>>",incoming_message))

        
        

 
 



    
    