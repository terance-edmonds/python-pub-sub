from _socket_server import SocketServer
import sys

if __name__ == "__main__":
    # read first argument (PORT)
    port = int(sys.argv[1])
    socket = SocketServer(port=port)
    
    # start the server
    try:
        socket.start()
    except KeyboardInterrupt:
        pass
    finally:
        socket.close()
