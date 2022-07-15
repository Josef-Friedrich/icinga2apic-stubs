from icinga2apic.base import Base


LOG = ...
class Objects(Base):
    '''
    Icinga 2 API objects class
    '''
    base_url_path = ...
    def get(self, object_type, name, attrs=..., joins=...):
        '''
        get object by type or name

        :param object_type: type of the object
        :type object_type: string
        :param name: list object with this name
        :type name: string
        :param attrs: only return these attributes
        :type attrs: list
        :param joins: show joined object
        :type joins: list

        example 1:
        get('Host', 'webserver01.domain')

        example 2:
        get('Service', 'webserver01.domain!ping4')

        example 3:
        get('Host', 'webserver01.domain', attrs=["address", "state"])

        example 4:
        get('Service', 'webserver01.domain!ping4', joins=True)
        '''
        ...

    def list(self, object_type, name=..., attrs=..., filters=..., filter_vars=..., joins=...):
        '''
        get object by type or name

        :param object_type: type of the object
        :type object_type: string
        :param name: list object with this name
        :type name: string
        :param attrs: only return these attributes
        :type attrs: list
        :param filters: filters matched object(s)
        :type filters: string
        :param filter_vars: variables used in the filters expression
        :type filter_vars: dict
        :param joins: show joined object
        :type joins: list

        example 1:
        list('Host')

        example 2:
        list('Service', 'webserver01.domain!ping4')

        example 3:
        list('Host', attrs='["address", "state"])

        example 4:
        list('Host', filters='match("webserver*", host.name)')

        example 5:
        list('Service', joins=['host.name'])

        example 6:
        list('Service', joins=True)
        '''
        ...

    def create(self, object_type, name, templates=..., attrs=...): # -> Response | Any:
        '''
        create an object

        :param object_type: type of the object
        :type object_type: string
        :param name: the name of the object
        :type name: string
        :param templates: templates used
        :type templates: list
        :param attrs: object's attributes
        :type attrs: dictionary

        example 1:
        create('Host', 'localhost', ['generic-host'], {'address': '127.0.0.1'})

        example 2:
        create('Service',
               'testhost3!dummy',
               {'check_command': 'dummy'},
               ['generic-service'])
        '''
        ...

    def update(self, object_type, name, attrs): # -> Response | Any:
        '''
        update an object

        :param object_type: type of the object
        :type object_type: string
        :param name: the name of the object
        :type name: string
        :param attrs: object's attributes to change
        :type attrs: dictionary

        example 1:
        update('Host', 'localhost', {'address': '127.0.1.1'})

        example 2:
        update('Service', 'testhost3!dummy', {'check_interval': '10m'})
        '''
        ...

    def delete(self, object_type, name=..., filters=..., filter_vars=..., cascade=...): # -> Response | Any:
        '''
        delete an object

        :param object_type: type of the object
        :type object_type: string
        :param name: the name of the object
        :type name: string
        :param filters: filters matched object(s)
        :type filters: string
        :param filter_vars: variables used in the filters expression
        :type filter_vars: dict
        :param cascade: deleted dependent objects
        :type joins: bool

        example 1:
        delete('Host', 'localhost')

        example 2:
        delete('Service', filters='match("vhost*", service.name)')
        '''
        ...
