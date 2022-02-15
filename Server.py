import socket, cv2, pickle, struct

SERVER = 'localhost'
PORT = 5454

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVER,PORT))
server.listen()
print(f"[LISTENING] Server is listening on {SERVER}")

connection, address = server.accept()
print(f"[NEW CONNECTION] New Connection : {connection} | ADDR : {address} connected.")

def ReceiveVideo():
    data = b''
    payload = struct.calcsize("Q") #bytes
    while True:
        while len(data) < payload:
            packet = connection.recv(2*1024) #2kB
            if not packet:
                break
            data += packet
        PackedMsg = data[:payload]        
        data = data[payload:]
        msg = struct.unpack("Q", PackedMsg)[0]
        
        while len(data) < msg :
            data += connection.recv(2*1024)
            
        FrameData = data[:msg]
        data = data[msg:]
        frame = pickle.loads(FrameData)
        
        cv2.imshow('Server Receiving..,',frame)
        if cv2.waitKey(10) == ord('q'):
            client.close()
            
ReceiveVideo()