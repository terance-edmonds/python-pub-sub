from _socket_client import SocketClient
import sys

def on_callback(msg):
    print(f"Received message: {msg}")

if __name__ == "__main__":
    # read arg 1 as server ip and arg 2 as server port
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    role = sys.argv[3]
    topic = sys.argv[4]

    socket = SocketClient(ip=server_ip, port=server_port, role=role, topic=topic)
    socket.connect()
    
    # show the response according to role
    if role == 'PUBLISHER':
        while True:
            # get user message
            msg = input("Enter message: ")

            if(msg == 'terminate'):
                socket.close()
                break
            
            # send message
            socket.emit(data=msg)
            
    elif role == 'SUBSCRIBER':
        socket.on(on_callback)
        