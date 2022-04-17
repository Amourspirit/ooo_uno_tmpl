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
# Namespace: com.sun.star.ui
from typing_extensions import Literal
import typing
from .xui_configuration import XUIConfiguration as XUIConfiguration_c4eb0c34
from .xui_configuration_persistence import XUIConfigurationPersistence as XUIConfigurationPersistence_661010b9
from .xui_configuration_storage import XUIConfigurationStorage as XUIConfigurationStorage_25ac0f09
if typing.TYPE_CHECKING:
    from ..awt.key_event import KeyEvent as KeyEvent_7a78097f

class XAcceleratorConfiguration(XUIConfiguration_c4eb0c34, XUIConfigurationPersistence_661010b9, XUIConfigurationStorage_25ac0f09):
    """
    provides read/write access to an accelerator configuration set.
    
    Such configuration set base on:
    
    Note further:
    All changes you made on this configuration access modify the configuration set inside memory only. You have to use the com.sun.star.util.XFlushable interface (which must be available at the same implementation object too), to make it persistent.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XAcceleratorConfiguration <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XAcceleratorConfiguration.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ui.XAcceleratorConfiguration']

    def getAllKeyEvents(self) -> 'typing.Tuple[KeyEvent_7a78097f, ...]':
        """
        return the list of all key events, which are available at this configuration set.
        
        The key events are the \"primary keys\" of this configuration sets. Means: Commands are registered for key events.
        
        Such key event can be mapped to its bound command, using the method getCommandForKeyEvent().
        """
    def getCommandByKeyEvent(self, aKeyEvent: 'KeyEvent_7a78097f') -> str:
        """
        return the registered command for the specified key event.
        
        This function can be used to:

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
    def getKeyEventsByCommand(self, sCommand: str) -> 'typing.Tuple[KeyEvent_7a78097f, ...]':
        """
        optimized access to the relation \"command-key\" instead of \"key-command\" which is provided normally by this interface.
        
        It can be used to implement collision handling, if more than one key event match to the same command. The returned list contains all possible key events - and the outside code can select a possible one. Of course - mostly this list will contain only one key event ...

        Raises:
            : ````
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
    def getPreferredKeyEventsForCommandList(self, lCommandList: 'typing.Tuple[str, ...]') -> 'typing.Tuple[object, ...]':
        """
        optimized function to map a list of commands to a corresponding list of key events.
        
        It provides a fast mapping, which is e.g. needed by a menu or toolbar implementation. E.g. a sub menu is described by a list of commands - and the implementation of the menu must show the corresponding shortcuts. Iteration over all items of this configuration set can be very expensive.
        
        Instead to the method getKeyEventsForCommand() the returned list contains only one(!) key event bound to one(!) requested command. If more than one key event is bound to a command - a selection is done inside this method. This internal selection can't be influenced from outside.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
    def removeCommandFromAllKeyEvents(self, sCommand: str) -> None:
        """
        search for a key-command-binding inside this configuration set, where the specified command is used.
        
        If such binding could be located, the command will be removed from it. If as result of that the key binding will be empty, if will be removed too.
        
        This is an optimized method, which can perform removing of commands from this configuration set. Because normally Commands are \"foreign keys\" and key identifier the \"primary keys\" - it needs some work to remove all commands outside this container ...

        Raises:
            : ````
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
    def removeKeyEvent(self, aKeyEvent: 'KeyEvent_7a78097f') -> None:
        """
        remove a key-command-binding from this configuration set.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
    def setKeyEvent(self, aKeyEvent: 'KeyEvent_7a78097f', sCommand: str) -> None:
        """
        modify or create a key - command - binding.
        
        If the specified key event does not already exists inside this configuration access, it will be created and the command will be registered for it.
        
        If the specified key event already exists, its command will be overwritten with the new command. There is no warning nor any error about that! The outside code has to use the method getCommandForKeyEvent() to check for possible collisions.
        
        Note: This method can't be used to remove entities from the configuration set. Empty parameters will result into an exception! Use the method removeKeyEvent() instead.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """

