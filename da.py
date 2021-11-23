from sqlobject import SQLObject
from sqlobject.col import IntCol, JSONCol, StringCol
from sqlobject.sqlite import builder

connection = builder()('data.db')

class Relationship(SQLObject):
    class sqlmeta:
        lazyUpdate = True
    _connection = connection
    name= StringCol()
    desc= StringCol()
    service_1 = IntCol()
    service_2 = IntCol()
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.desc,
            'service1': get_service(self.service_1).to_dict(),
            'service2': get_service(self.service_2).to_dict()
        }
class Service(SQLObject):
    class sqlmeta:
        lazyUpdate = True

    _connection = connection
    thing_id = IntCol()
    name = StringCol()
    icon = StringCol()
    desc = StringCol()

    def to_dict(self):
        return {
            'id': self.id,
            'thing': get_thing(self.thing_id).to_dict(),
            'name': self.name,
            'icon': self.icon,
            'desc': self.desc
        }


class Thing(SQLObject):
    class sqlmeta:
        lazyUpdate = True

    _connection = connection
    name = StringCol()
    icon = StringCol()
    desc = StringCol()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'icon': self.icon,
            'desc': self.desc
        }

def get_service(service_id):
    services = list(Service.selectBy(id=service_id))
    if len(services) > 0:
        return services[0]
    else:
        return None

def get_thing(thing_id):
    things = list(Thing.selectBy(id=thing_id))
    if len(things) > 0:
        return things[0]
    else:
        return None

def get_all_relationships():
    return list(Relationship.select())

def get_all_things():
    return list(Thing.select())


def get_services_of_thing(thing_id):
    return list(Service.selectBy(thing_id=thing_id))


def create_thing(**kwargs):
    name = kwargs.get('name')
    desc = kwargs.get('desc')
    icon = kwargs.get('icon')

    try:
        Thing(
            name=name,
            desc=desc,
            icon=icon
        ).set()
        return True
    except:
        return False


def create_service(**kwargs):
    thing_id = kwargs.get('thing_id')
    name = kwargs.get('name')
    desc = kwargs.get('desc')
    icon = kwargs.get('icon')

    try:
        Service(
            name=name,
            desc=desc,
            icon=icon,
            thing_id=thing_id
        ).set()
        return True
    except:
        return False


Thing.createTable(ifNotExists=True)
Service.createTable(ifNotExists=True)
