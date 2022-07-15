from typing import Union, Dict, List, Type
import sys
from logging import Logger
from icinga2apic.exceptions import *

if sys.version_info >= (3, 0):
    ...
else:
    ...
LOG: Logger = ...


Json = Union[Dict[str, 'Json'], List['Json'],
             int, str, float, bool, Type[None]]


class Base:
    '''
    Icinga 2 API Base class
    '''
    base_url_path = ...

    def __init__(self, manager) -> None:
        '''
        initialize object
        '''
        ...
