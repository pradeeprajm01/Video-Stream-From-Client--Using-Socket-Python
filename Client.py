import socket, cv2, struct, pickle, imutils

SERVER = 'localhost'
PORT = 5454

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER,PORT))
print(f'[CONNECTED] Connected to {SERVER}...')

def StreamVideo():
    while True:        
        video = cv2.VideoCapture(0)
        Img,Frame = video.read()
        cv2.imshow('Client Sending...', Frame)
        data = pickle.dumps(Frame)
        msg = struct.pack("Q",len(data)) + data
        client.send(msg)
        
        if cv2.waitKey(13) == ord('q'):
            cv2.destroyAllWindows()
            client.close()
                
StreamVideo()
