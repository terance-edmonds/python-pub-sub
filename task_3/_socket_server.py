import socket
import threading

class SocketServer():
    def __init__(self, port, ip = ''):
        self.ip = ip
        self.port = port
        self.topics = {}

        # initiate socket
        self.socket = socket.socket()

    # start socket server
    def start(self):
        # bind the socket to ip and port
        self.socket.bind((self.ip, self.port))
        # start listening
        self.socket.listen(5)

        print(f"\33[35m[Socket initiated on]\033[0m \33[33m[{self.ip}:{self.port}]\033[0m")

        # start listening to clients
        self.listen()

    # close socket
    def close(self):
        self.socket.close()

    # handle on client
    def on_client(self, con, address, role, topic):
        while True:
            # read 1024 byte
            data = con.recv(1024)
            
            # close the connection
            if not data:
                if role == 'SUBSCRIBER':
                    self.topics[topic].remove(con)

                print(f"\33[91m[Client disconnected:]\033[0m \33[33m \33[33m[{address}]\033[0m")
                con.close()
                break
            
            # send message to all subscribers of the topic
            if topic in self.topics:
                for subscriber in self.topics[topic]:
                    subscriber.send(data)

            print(f"\33[34m[Client message received from]\033[0m \33[33m[{address}]\033[0m")

    # start listening to clients
    def listen(self):
        while True:
            # establish a connection with server
            con, address = self.socket.accept()
            print(f"\33[32m[Client connected:]\033[0m \33[33m[{address}\033[0m")
            
            role_topic = con.recv(1024).decode('utf-8').split()
            role = role_topic[0]
            topic = role_topic[1]

            if role == 'SUBSCRIBER':
                # add topic if does not exist
                if topic not in self.topics:
                    self.topics[topic] = []

                # append subscriber to topic    
                self.topics[topic].append(con)
        
            # handle client
            thread = threading.Thread(target=self.on_client, args=(con, address, role, topic))
            # daemon is true to make sure all processes stop when program exits
            thread.daemon = True
            # start the thread
            thread.start()