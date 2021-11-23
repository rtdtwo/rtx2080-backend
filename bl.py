import da


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


def create_service(data):
    if 'thing_id' not in data or 'name' not in data or 'desc' not in data:
        return {
            'code': 400,
            'msg': 'Thing ID, Name or Description not provided'
        }

    thing_id = data['thing_id']
    name = data['name']
    if 'icon' in data:
        icon = data['icon']
    else:
        icon = ''
    desc = data['desc']

    result = da.create_service(thing_id=thing_id, name=name, icon=icon, desc=desc)
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
    
