from _socket_ import Socket
import sys

def on_callback(msg, con, address):
    print(f"Received message from {address} = {msg}")

if __name__ == "__main__":
    # read first argument (PORT)
    port = int(sys.argv[1])
    socket = Socket(port=port)
    
    # start the server
    socket.start()
    # on callback (received data)
    socket.on(on_callback)
