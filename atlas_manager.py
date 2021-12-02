import socket
import json


def execute_service(service, result):
    if result is not None:
        print(result[0])
        result = result[1]
        if result['Status'] == 'Successful':
            input = "({},)".format(result['Service Result'])
        else:
            input = "(1,)"
    else:
        input = "(1,)"

    

    message = json.dumps({
        "Tweet Type": "Service call",
        "Service Name": service['name'],
        "Thing ID": service['thing']['id'],
        "Entity ID": service['entity'],
        "Space ID": service['space'],
        "Service Inputs": input
    })

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((service['thing']['ip'], 6668))
    s.sendall(bytes(message, 'utf-8'))
    data = s.recv(1024)
    s.close()
    return True, json.loads(data.decode())