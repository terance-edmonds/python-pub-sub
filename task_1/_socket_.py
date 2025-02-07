import socket

class Socket():
    def __init__(self, port, ip = ''):
        self.ip = ip
        self.port = port
        # initiate socket
        self.socket = socket.socket()

    # start socket server
    def start(self):
        # bind the socket to ip and port
        self.socket.bind((self.ip, self.port))
        # start listening
        self.socket.listen(5)

        print(f"\33[35m[Socket initiated on]\033[0m \33[33m[{self.ip}:{self.port}]\033[0m")

    # connect to socket server
    def connect(self):
        self.socket.connect((self.ip, self.port))

    # close socket
    def close(self):
        self.socket.close()

    # send message
    def emit(self, data):
        enc = data.encode('utf-8')
        self.socket.send(enc)

    # handle on client
    def on_client(self, con, address):
        # read 1024 byte
        data = con.recv(1024)
        if not data:
            raise
        
        # callback the received data
        self.callback(data.decode('utf-8'), con, address)

    # on data
    def on(self, callback):
        self.callback = callback
        # establish a connection with server
        con, address = self.socket.accept()
        print(f"\33[32m[Client connected:]\033[0m \33[33m[{address}\033[0m")
        
        while True:
            try:
                # handle client
                self.on_client(con, address)
            except:
                # close the connection
                print(f"\33[91m[Client disconnected:]\033[0m \33[33m \33[33m[{address}]\033[0m")
                con.close()
                break