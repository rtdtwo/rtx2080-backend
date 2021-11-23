from sqlobject import SQLObject
from sqlobject.col import IntCol, StringCol
from sqlobject.sqlite import builder

connection = builder()('data.db')


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
            'thing': get_thing(self.thing_id),
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


def get_thing(thing_id):
    things = list(Thing.selectBy(id=thing_id))
    if len(things) > 0:
        return things[0]
    else:
        return None


def get_all_things():
    return list(Thing.select())


def get_services_of_thing(thing_id):
    return list(Service.selectBy(thing_id=thing_id))


def create_service(**kwargs):
    thing_id = kwargs.get('thing_id')
    name = kwargs.get('name')
    desc = kwargs.get('desc')
    icon = kwargs.get('icon')

    try:
        Service(
            thing_id=thing_id,
            name=name,
            desc=desc,
            icon=icon
        ).set()
        return True
    except:
        return False


Thing.createTable(ifNotExists=True)
Service.createTable(ifNotExists=True)
