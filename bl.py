import da
import json
import socket


def get_things():
    return {
        'code': 200,
        'result': da.get_all_things()
    }


def get_services(thing_id):
    return {
        'code': 200,
        'result': da.get_services_of_thing(thing_id)
    }


def get_relationships():
    return{
        'code': 200,
        'result': da.get_all_relationships()
    }


def create_relationship(data):
    if 'name' not in data or 'desc' not in data or 'service_1' not in data or 'service_2' not in data:
        return {
            'code': 400,
            'msg': 'Name, Description, or Services not provided'
        }

    name = data['name']
    desc = data['desc']
    service_1 = data['service_1']
    service_2 = data['service_2']
    if 'icon' in data:
        icon = data['icon']
    else:
        icon = ''

    result = da.create_relationship(
        name=name, icon=icon, desc=desc, service_1=service_1, service_2=service_2)
    if result:
        return {
            'code': 201,
            'msg': 'Relationship created'
        }
    else:
        return {
            'code': 500,
            'msg': 'Server error. It is not you, it is us.'
        }


def create_thing(data):
    if 'id' not in data or 'name' not in data or 'desc' not in data or 'space' not in data or 'ip' not in data:
        return {
            'code': 400,
            'msg': 'ID, Name, Description, IP address or Space not provided'
        }

    id = data['id']
    name = data['name']
    desc = data['desc']
    space = data['space']
    ip = data['ip']
    if 'icon' in data:
        icon = data['icon']
    else:
        icon = ''

    result = da.create_thing(
        id=id, name=name, icon=icon, desc=desc, space=space, ip=ip)
    if result:
        return {
            'code': 201,
            'msg': 'Thing created'
        }
    else:
        return {
            'code': 500,
            'msg': 'Server error. It is not you, it is us.'
        }


def create_service(data):
    if 'thing' not in data or 'name' not in data or 'entity' not in data or 'space' not in data:
        return {
            'code': 400,
            'msg': 'Thing, Name, Entity or Space not provided'
        }

    thing = data['thing']
    name = data['name']
    entity = data['entity']
    space = data['space']

    if 'icon' in data:
        icon = data['icon']
    else:
        icon = ''

    result = da.create_service(
        thing=thing, name=name, icon=icon, entity=entity, space=space)
    if result:
        return {
            'code': 201,
            'msg': 'Service {} created'.format(name)
        }
    else:
        return {
            'code': 500,
            'msg': 'Server error. It is not you, it is us.'
        }


def run_app(app_id):
    app = da.get_app()
    app_results = []
    for recipe in [da.get_recipe(recipe_id) for recipe_id in app['recipes']]:
        recipe_results = {
            'id': recipe['id'],
            'result': []
        }
        for relationship in [da.get_relationship(relationship_id) for relationship_id in recipe['relationships']]:
            relationship_results = {
                'relationship': relationship,
                'result': []
            }
            service_1 = da.get_service(relationship['service_1'])
            result_1 = execute_service(service_1)
            service_2 = da.get_service(relationship['service_2'])
            result_2 = execute_service(service_2)
            relationship_results['result'].append({
                'service': service_1,
                'result': result_1
            })
            relationship_results['result'].append({
                'service': service_2,
                'result': result_2
            })

            recipe_results['result'].append(relationship_results)

        app_results.append(recipe_results)

    return {
        'code': 200,
        'msg': 'Actions performed',
        'result': app_results
    }


def execute_service(service):
    message = json.dumps({
        "Tweet Type": "Service call",
        "Service Name": service['name'],
        "Thing ID": service['thing'],
        "Entity ID": service['entity'],
        "Space ID": service['space'],
    })

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((da.get_thing(service['thing'])['ip'], 6668))
    s.sendall(bytes(message, 'utf-8'))
    data = s.recv(1024)
    s.close()
    return True, json.loads(data.decode())
