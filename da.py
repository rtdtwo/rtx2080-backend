import json


def get_data():
    f = open('config.json', 'r')
    data = json.load(f)
    f.close()
    return data


def get_all_things():
    data = get_data()
    return data['things']


def get_thing(thing_id):
    data = get_data()
    things = data['things']
    for thing in things:
        if thing['id'] == thing_id:
            return thing
    return None


def create_thing(**kwargs):
    id = kwargs.get('id')
    name = kwargs.get('name')
    desc = kwargs.get('desc')
    icon = kwargs.get('icon')
    space = kwargs.get('space')
    ip = kwargs.get('ip')

    try:
        new = True
        data = get_data()
        generated_thing = {
            "id": id,
            "name": name,
            "desc": desc,
            "icon": icon,
            "space": space,
            "ip": ip
        }
        updated_things = []
        for thing in data['things']:
            if thing['id'] == id:
                updated_things.append(generated_thing)
                new = False
            else:
                updated_things.append(thing)

        if new:
            updated_things.append(generated_thing)

        data['things'] = updated_things

        f = open('config.json', 'w')
        json.dump(data, f)
        f.close()
        return True
    except:
        return False


def get_services_of_thing(thing_id):
    services = []
    data = get_data()
    for service in data['services']:
        if service['thing'] == thing_id:
            service['thing'] = get_thing(thing_id)
            services.append(service)
    return services


def get_service(name):
    data = get_data()
    services = data['services']
    for service in services:
        if service['name'] == name:
            service['thing'] = get_thing(service['thing'])
            return service
    return None


def create_service(**kwargs):
    thing = kwargs.get('thing')
    name = kwargs.get('name')
    entity = kwargs.get('entity')
    space = kwargs.get('space')
    icon = kwargs.get('icon')

    try:
        new = True
        data = get_data()
        generated_service = {
            "thing": thing,
            "name": name,
            "id": name,
            "entity": entity,
            "space": space,
            "icon": icon
        }
        updated_services = []
        for service in data['services']:
            if service['name'] == name:
                updated_services.append(generated_service)
                new = False
            else:
                updated_services.append(service)

        if new:
            updated_services.append(generated_service)

        data['services'] = updated_services

        f = open('config.json', 'w')
        json.dump(data, f)
        f.close()
        return True
    except:
        return False


def get_all_relationships():
    data = get_data()
    relationships = data['relationships']
    for relationship in relationships:
        relationship['service_1'] = get_service(relationship['service_1'])
        relationship['service_2'] = get_service(relationship['service_2'])
    return relationships


def create_relationship(**kwargs):
    name = kwargs.get('name')
    desc = kwargs.get('desc')
    icon = kwargs.get('icon')
    service_1 = kwargs.get('service_1')
    service_2 = kwargs.get('service_2')

    try:
        new = True
        data = get_data()
        generated_relationship = {
            "name": name,
            "id": name,
            "icon": icon,
            "desc": desc,
            'service_1': service_1,
            'service_2': service_2
        }
        updated_relationships = []
        for relationship in data['services']:
            if relationship['name'] == name:
                updated_relationships.append(generated_relationship)
                new = False
            else:
                updated_relationships.append(relationship)

        if new:
            updated_relationships.append(generated_relationship)

        data['relationships'] = updated_relationships

        f = open('config.json', 'w')
        json.dump(data, f)
        f.close()
        return True
    except:
        return False
