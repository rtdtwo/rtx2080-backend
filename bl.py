import da


def get_things():
    return {
        'code': 200,
        'result': [thing.to_dict() for thing in da.get_all_things()]
    }


def get_services(thing_id):
    return {
        'code': 200,
        'result': [service.to_dict() for service in da.get_services_of_thing(thing_id)]
    }


def create_thing(data):
    if 'name' not in data or 'desc' not in data:
        return {
            'code': 400,
            'msg': 'Name or Description not provided'
        }

    name = data['name']
    desc = data['desc']
    if 'icon' in data:
        icon = data['icon']
    else:
        icon = ''

    result = da.create_thing(name=name, icon=icon, desc=desc)
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
    if 'thing_id' not in data or 'name' not in data or 'desc' not in data:
        return {
            'code': 400,
            'msg': 'Thing ID, Name or Description not provided'
        }

    thing_id = data['thing_id']
    name = data['name']
    desc = data['desc']
    if 'icon' in data:
        icon = data['icon']
    else:
        icon = ''

    result = da.create_service(
        thing_id=thing_id, name=name, icon=icon, desc=desc)
    if result:
        return {
            'code': 201,
            'msg': 'Service created'
        }
    else:
        return {
            'code': 500,
            'msg': 'Server error. It is not you, it is us.'
        }
