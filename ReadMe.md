# Python Pub Sub Pattern
Designing and implementing a simple Publish and Subscribe middleware using Client-Server Sockets Programming concepts and techniques

## Task 1: The Client-Server Application

1. Start the Server by passing the PORT as a command line argument.

```bash
py task_1/server.py 5000
```

2. Start a Client to connect with the server by passing Server IP and Server PORT as command line arguments.

```bash
py task_1/client.py 127.0.0.1 5000
```

## Task 2: Publishers and Subscribers

1. Start the Server by passing the PORT as a command line argument.

```bash
py task_2/server.py 5000
```

2. Start Clients to connect with the server by passing Server IP and Server PORT as command line arguments.

```bash
py task_2/client.py 127.0.0.1 5000 PUBLISHER
py task_2/client.py 127.0.0.1 5000 SUBSCRIBER
```