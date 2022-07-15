from _typeshed import Incomplete as Incomplete
from icinga2apic.base import Base as Base

LOG: Incomplete

class Objects(Base):
    base_url_path: str
    def get(
        self,
        object_type,
        name,
        attrs: Union[Incomplete, None] = ...,
        joins: Union[Incomplete, None] = ...,
    ): ...
    def list(
        self,
        object_type,
        name: Union[Incomplete, None] = ...,
        attrs: Union[Incomplete, None] = ...,
        filters: Union[Incomplete, None] = ...,
        filter_vars: Union[Incomplete, None] = ...,
        joins: Union[Incomplete, None] = ...,
    ): ...
    def create(
        self,
        object_type,
        name,
        templates: Union[Incomplete, None] = ...,
        attrs: Union[Incomplete, None] = ...,
    ): ...
    def update(self, object_type, name, attrs) -> None: ...
    def delete(
        self,
        object_type,
        name: Union[Incomplete, None] = ...,
        filters: Union[Incomplete, None] = ...,
        filter_vars: Union[Incomplete, None] = ...,
        cascade: bool = ...,
    ): ...
