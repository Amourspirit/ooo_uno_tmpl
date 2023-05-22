import os
from typing import Any, TYPE_CHECKING

__version__ = "1.0.5"
__version_tmpl__ = "0.3.0"

_IGNORE_IMPORT_ERROR = os.environ.get(
    "ooouno_ignore_import_error", None) in ("True", "true", "yes")

if TYPE_CHECKING is False and _IGNORE_IMPORT_ERROR is False:
    raise ImportError("Are you sure that uno has been imported?")


if TYPE_CHECKING:
    from typing import Protocol
else:
    Protocol = object

class UnoEnumProto(Protocol):
    typeName: str
    value: Any
    
    def __init__(self, *args, **kwargs) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, that: Any) -> bool: ...
    def __ne__(self,other: Any) -> bool: ...