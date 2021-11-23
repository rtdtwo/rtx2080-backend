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


def get_relationships():
    return {
        'code': 200,
        'result' :[{
            'id' : 1,
            'name' : 'relationship1',
            'service1' : {
                'id': 1,
                'thingId':1,
                'name': 'Service1',
                'icon': '',
                'desc': ''
            },
             'service2' : {
                'id': 2,
                'thingId':2,
                'name': 'Service2',
                'icon': '',
                'desc': ''
            },
        },
        {
            'id' : 2,
            'name' : 'relationship2',
            'service1' : {
                'id': 2,
                'thingId':2,
                'name': 'Service2',
                'icon': '',
                'desc': ''
            },
             'service2' : {
                'id': 3,
                'thingId':3,
                'name': 'Service3',
                'icon': '',
                'desc': ''
            },
        },
        {
            'id' : 3,
            'name' : 'relationship3',
            'service1' : {
                'id': 3,
                'thingId':3,
                'name': 'Service3',
                'icon': '',
                'desc': ''
            },
             'service2' : {
                'id': 4,
                'thingId':4,
                'name': 'Service4',
                'icon': '',
                'desc': ''
            },
        }]

    }