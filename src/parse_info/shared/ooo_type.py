from enum import Enum

class OooType(str, Enum):
    CONST = "const"
    ENUM = "enum"
    EXCEPTION = "exception"
    INTERFACE = "interface"
    SINGLETON = "singleton"
    SERVICE = "service"
    STRUCT = "struct"
    TYPEDEF = "typedef"