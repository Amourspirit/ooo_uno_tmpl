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
# Namespace: com.sun.star.frame
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from ..beans.property_value import PropertyValue as PropertyValue_c9610c73


class DispatchStatement(object):
    """
    Struct Class

    represents a dispatch statement from a recorded macro
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API DispatchStatement <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1DispatchStatement.html>`_
    """
    typeName: Literal['com.sun.star.frame.DispatchStatement']

    def __init__(self, aArgs: typing.Optional[typing.Tuple[PropertyValue_c9610c73, ...]] = ..., aCommand: typing.Optional[str] = ..., aTarget: typing.Optional[str] = ..., nFlags: typing.Optional[int] = ..., bIsComment: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            aArgs (typing.Tuple[PropertyValue, ...], optional): aArgs value.
            aCommand (str, optional): aCommand value.
            aTarget (str, optional): aTarget value.
            nFlags (int, optional): nFlags value.
            bIsComment (bool, optional): bIsComment value.
        """
        ...


    @property
    def aArgs(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        specifies the dispatch command arguments
        
        That means the Arguments parameter of a corresponding XDispatch.dispatch() request.
        """
        ...


    @property
    def aCommand(self) -> str:
        """
        specifies the dispatch command
        
        That means the URL parameter of a corresponding XDispatchProvider.queryDispatch() request.
        """
        ...


    @property
    def aTarget(self) -> str:
        """
        specifies the frame target
        
        That means the TargetFrameName parameter of a corresponding XDispatchProvider.queryDispatch() request.
        """
        ...


    @property
    def nFlags(self) -> int:
        """
        specifies the optional search flags
        
        That means the SearchFlags parameter of a corresponding XDispatchProvider.queryDispatch() request.
        """
        ...


    @property
    def bIsComment(self) -> bool:
        """
        specifies if this statement should be recorded as commented out or not
        """
        ...


