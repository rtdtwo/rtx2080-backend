import socket
import json


def execute_service(service, thing):
    message = json.dumps({
        "Tweet Type": "Service call",
        "Service Name": service['name'],
        "Thing ID": service['thing'],
        "Entity ID": service['entity'],
        "Space ID": service['space'],
    })

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((thing['ip'], 6668))
    s.sendall(bytes(message, 'utf-8'))
    data = s.recv(1024)
    s.close()
    return True, json.loads(data.decode())