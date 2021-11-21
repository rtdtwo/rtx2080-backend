def get_things():
    return {
        'code': 200,
        'result': [
            {
                'id': 1,
                'name': 'Thing1',
                'icon': '',
                'desc': ''
            },
            {
                'id': 2,
                'name': 'Thing2',
                'icon': '',
                'desc': ''
            },
            {
                'id': 3,
                'name': 'Thing3',
                'icon': '',
                'desc': ''
            },

            {
                'id': 4,
                'name': 'Thing4',
                'icon': '',
                'desc': ''
            }
        ]
    }
def get_services(thing_id):
    # if thing_id==1:
    return {
        'code' : 200,
        'result' : [ {
            'id': 1,
            'thingId':thing_id,
            'name': 'Service1',
            'icon': '',
            'desc': ''
        },
        {
            'id': 2,
            'thingId':thing_id,
            'name': 'Service2',
            'icon': '',
            'desc': ''
        },
        {
            'id': 3,
            'thingId':thing_id,
            'name': 'Service3',
            'icon': '',
            'desc': ''
        },
        {
            'id': 4,
            'thingId':thing_id,
            'name': 'Service4',
            'icon': '',
            'desc': ''
        },]
    }