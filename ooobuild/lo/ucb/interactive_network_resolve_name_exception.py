# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .interactive_network_exception import InteractiveNetworkException as InteractiveNetworkException_7ca31159
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..task.interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7

class InteractiveNetworkResolveNameException(InteractiveNetworkException_7ca31159):
    """
    Exception Class

    A network error specifying a name resolution failure.

    See Also:
        `API InteractiveNetworkResolveNameException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1InteractiveNetworkResolveNameException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.InteractiveNetworkResolveNameException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.ucb.InteractiveNetworkResolveNameException'
    __pyunostruct__: str = 'com.sun.star.ucb.InteractiveNetworkResolveNameException'

    typeName: str = 'com.sun.star.ucb.InteractiveNetworkResolveNameException'
    """Literal Constant ``com.sun.star.ucb.InteractiveNetworkResolveNameException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Classification: typing.Optional[InteractionClassification_6c4d10e7] = InteractionClassification_6c4d10e7.ERROR, Server: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            Server (str, optional): Server value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Classification": Classification,
            "Server": Server,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._server = kwargs["Server"]
        inst_keys = ('Server',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def Server(self) -> str:
        """
        The server name for which resolution failed.
        """
        return self._server
    
    @Server.setter
    def Server(self, value: str) -> None:
        self._server = value


__all__ = ['InteractiveNetworkResolveNameException']

