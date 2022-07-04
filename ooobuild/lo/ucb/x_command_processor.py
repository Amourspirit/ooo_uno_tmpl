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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.ucb
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .command import Command as Command_709c0901
    from .x_command_environment import XCommandEnvironment as XCommandEnvironment_fb330dee

class XCommandProcessor(XInterface_8f010a43):
    """
    defines a processor for synchronous commands, which are executed in a specific execution environment.

    See Also:
        `API XCommandProcessor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XCommandProcessor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XCommandProcessor'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XCommandProcessor'

    @abstractmethod
    def abort(self, CommandId: int) -> None:
        """
        ends the command associated with the given id.
        
        Not every command can be aborted. It's up to the implementation to decide whether this method will actually end the processing of the command or simply do nothing.
        """
        ...
    @abstractmethod
    def createCommandIdentifier(self) -> int:
        """
        creates a unique identifier for a command.
        
        This identifier can be used to abort the execution of the command associated with that identifier. Note that it is generally not necessary to obtain a new id for each command, because commands are executed synchronously. So the id for a command is valid again after a command previously associated with this id has finished. In fact you only should get one identifier per thread and assign it to every command executed by that thread.
        
        Also, after a call to XCommandProcessor.abort(), an identifier should not be used any longer (and instead be released by a call to XCommandProcessor2.releaseCommandIdentifier()), because it may well abort all further calls to XCommandProcessor.execute().
        
        To avoid ever-increasing resource consumption, the identifier should be released via XCommandProcessor2.releaseCommandIdentifier() when it is no longer used.
        """
        ...
    @abstractmethod
    def execute(self, aCommand: 'Command_709c0901', CommandId: int, Environment: 'XCommandEnvironment_fb330dee') -> object:
        """
        executes a command.
        
        Common command definitions can be found in the specification of the service Content.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
            CommandAbortedException: ``CommandAbortedException``
        """
        ...

__all__ = ['XCommandProcessor']

