from typing import Protocol, Any

class UnoEnum(Protocol):
    def name(self) -> str:...
    def value(self) -> Any:...
