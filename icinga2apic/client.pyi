from .actions import Actions

LOG = ...
class Client:
    '''
    Icinga 2 Client class
    '''

    actions: Actions

    def __init__(self, url=..., username=..., password=..., timeout=..., certificate=..., key=..., ca_certificate=..., config_file=...) -> None:
        '''
        initialize object
        '''
        ...
