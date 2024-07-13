from _socket_ import Socket
import sys

if __name__ == "__main__":
    # read arg 1 as server ip and arg 2 as server port
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    socket = Socket(ip=server_ip, port=server_port)
    socket.connect()
    
    while True:
        # get user message
        msg = input("Enter message: ")

        if(msg == 'terminate'):
            socket.close()
            break
        
        # send message
        socket.emit(data=msg)
        