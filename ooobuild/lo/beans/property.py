# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.beans
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class Property(object):
    """
    Struct Class

    This structure describes a property.
    
    There are three types of properties:

    See Also:
        `API Property <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Property.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.Property'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.beans.Property'
    """Literal Constant ``com.sun.star.beans.Property``"""

    def __init__(self, Name: typing.Optional[str] = '', Handle: typing.Optional[int] = 0, Type: typing.Optional[object] = None, Attributes: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Handle (int, optional): Handle value.
            Type (object, optional): Type value.
            Attributes (int, optional): Attributes value.
        """
        super().__init__()

        if isinstance(Name, Property):
            oth: Property = Name
            self.Name = oth.Name
            self.Handle = oth.Handle
            self.Type = oth.Type
            self.Attributes = oth.Attributes
            return

        kargs = {
            "Name": Name,
            "Handle": Handle,
            "Type": Type,
            "Attributes": Attributes,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._handle = kwargs["Handle"]
        self._type = kwargs["Type"]
        self._attributes = kwargs["Attributes"]


    @property
    def Name(self) -> str:
        """
        specifies the name of the property.
        
        The name is unique within an XPropertySet. Upper and lower case are distinguished.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Handle(self) -> int:
        """
        contains an implementation-specific handle for the property.
        
        It may be -1 if the implementation has no handle. You can use this handle to get values from the XFastPropertySet.
        """
        return self._handle
    
    @Handle.setter
    def Handle(self, value: int) -> None:
        self._handle = value

    @property
    def Type(self) -> object:
        """
        contains an object that identifies the declared type for the property.
        
        If the property has multiple types or the type is not known, but not an any, then void must be returned.
        """
        return self._type
    
    @Type.setter
    def Type(self, value: object) -> None:
        self._type = value

    @property
    def Attributes(self) -> int:
        """
        This field may contain zero or more constants of the PropertyAttribute constants group.
        """
        return self._attributes
    
    @Attributes.setter
    def Attributes(self, value: int) -> None:
        self._attributes = value


__all__ = ['Property']
