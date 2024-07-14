import socket

class SocketClient():
    def __init__(self, port, topic, ip = '', role = 'SUBSCRIBER'):
        self.ip = ip
        self.port = port
        self.role = role
        self.topic = topic
        # initiate socket
        self.socket = socket.socket()

    # connect to socket server
    def connect(self):
        self.socket.connect((self.ip, self.port))
        # set the role and topic
        role_topic = f"{self.role} {self.topic}"
        self.socket.send(role_topic.encode('utf-8'))

    # close socket
    def close(self):
        self.socket.close()

    # send message
    def emit(self, data):
        self.socket.send(data.encode('utf-8'))

    # on data
    def on(self, callback):
        while True:
            # read 1024 byte
            data = self.socket.recv(1024)
            if not data:
                break
            
            callback(data.decode('utf-8'))