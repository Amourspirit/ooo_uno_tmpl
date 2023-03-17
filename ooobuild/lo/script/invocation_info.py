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
# Namespace: com.sun.star.script
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from ..reflection.param_mode import ParamMode as ParamMode_d7260ca9
from .member_type import MemberType as MemberType_b1e00b97


class InvocationInfo(object):
    """
    Struct Class

    This struct is used to specify information about object members (methods or properties) accessed via XInvocation, such as names, types, or parameters.

    See Also:
        `API InvocationInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1InvocationInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.InvocationInfo'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.script.InvocationInfo'
    """Literal Constant ``com.sun.star.script.InvocationInfo``"""

    def __init__(self, aParamTypes: typing.Optional[typing.Tuple[object, ...]] = (), aParamModes: typing.Optional[typing.Tuple[ParamMode_d7260ca9, ...]] = (), aName: typing.Optional[str] = '', eMemberType: typing.Optional[MemberType_b1e00b97] = MemberType_b1e00b97.METHOD, PropertyAttribute: typing.Optional[int] = 0, aType: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            aParamTypes (typing.Tuple[object, ...], optional): aParamTypes value.
            aParamModes (typing.Tuple[ParamMode, ...], optional): aParamModes value.
            aName (str, optional): aName value.
            eMemberType (MemberType, optional): eMemberType value.
            PropertyAttribute (int, optional): PropertyAttribute value.
            aType (object, optional): aType value.
        """
        super().__init__()

        if isinstance(aParamTypes, InvocationInfo):
            oth: InvocationInfo = aParamTypes
            self.aParamTypes = oth.aParamTypes
            self.aParamModes = oth.aParamModes
            self.aName = oth.aName
            self.eMemberType = oth.eMemberType
            self.PropertyAttribute = oth.PropertyAttribute
            self.aType = oth.aType
            return

        kargs = {
            "aParamTypes": aParamTypes,
            "aParamModes": aParamModes,
            "aName": aName,
            "eMemberType": eMemberType,
            "PropertyAttribute": PropertyAttribute,
            "aType": aType,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._a_param_types = kwargs["aParamTypes"]
        self._a_param_modes = kwargs["aParamModes"]
        self._a_name = kwargs["aName"]
        self._e_member_type = kwargs["eMemberType"]
        self._property_attribute = kwargs["PropertyAttribute"]
        self._a_type = kwargs["aType"]


    @property
    def aParamTypes(self) -> typing.Tuple[object, ...]:
        """
        Types method parameters, for properties this sequence is empty.
        """
        return self._a_param_types
    
    @aParamTypes.setter
    def aParamTypes(self, value: typing.Tuple[object, ...]) -> None:
        self._a_param_types = value

    @property
    def aParamModes(self) -> typing.Tuple[ParamMode_d7260ca9, ...]:
        """
        Mode of method parameters (IN, OUT, INOUT), for properties this sequence is empty.
        """
        return self._a_param_modes
    
    @aParamModes.setter
    def aParamModes(self, value: typing.Tuple[ParamMode_d7260ca9, ...]) -> None:
        self._a_param_modes = value

    @property
    def aName(self) -> str:
        """
        Name of the method or property.
        """
        return self._a_name
    
    @aName.setter
    def aName(self, value: str) -> None:
        self._a_name = value

    @property
    def eMemberType(self) -> MemberType_b1e00b97:
        """
        Kind of the member (method or property).
        """
        return self._e_member_type
    
    @eMemberType.setter
    def eMemberType(self, value: MemberType_b1e00b97) -> None:
        self._e_member_type = value

    @property
    def PropertyAttribute(self) -> int:
        """
        Only for property members: This field may contain zero or more constants of the com.sun.star.beans.PropertyAttribute constants group.
        
        It is not guaranteed that all necessary constants are set to describe the property completely, but a flag will only be set, if the corresponding charac- teristic really exists. Example: If the READONLY flag is set, the property is readonly. If it isn't set, the property nevertheless can be readonly.
        
        For methods this field is irrelevant and is set to 0.
        """
        return self._property_attribute
    
    @PropertyAttribute.setter
    def PropertyAttribute(self, value: int) -> None:
        self._property_attribute = value

    @property
    def aType(self) -> object:
        """
        Type of the member, for methods the return type.
        """
        return self._a_type
    
    @aType.setter
    def aType(self, value: object) -> None:
        self._a_type = value


__all__ = ['InvocationInfo']
