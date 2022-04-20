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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.frame
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.frame import CommandGroup as CommandGroup
    if hasattr(CommandGroup, '_constants') and isinstance(CommandGroup._constants, dict):
        CommandGroup._constants['__ooo_ns__'] = 'com.sun.star.frame'
        CommandGroup._constants['__ooo_full_ns__'] = 'com.sun.star.frame.CommandGroup'
        CommandGroup._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global CommandGroupEnum
        ls = [f for f in dir(CommandGroup) if not callable(getattr(CommandGroup, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(CommandGroup, name)
        CommandGroupEnum = IntEnum('CommandGroupEnum', _dict)
    build_enum()
else:
    from ...lo.frame.command_group import CommandGroup as CommandGroup

    class CommandGroupEnum(IntEnum):
        """
        Enum of Const Class CommandGroup

        provides information about a supported command
        
        **since**
        
            OOo 2.0
        """
        INTERNAL = CommandGroup.INTERNAL
        """
        specifies internal commands.
        """
        APPLICATION = CommandGroup.APPLICATION
        """
        specifies application based commands.
        """
        VIEW = CommandGroup.VIEW
        """
        specifies view specific commands.
        """
        DOCUMENT = CommandGroup.DOCUMENT
        """
        specifies document specific commands.
        """
        EDIT = CommandGroup.EDIT
        """
        specifies edit specific commands.
        """
        MACRO = CommandGroup.MACRO
        """
        specifies commands used by the built-in Basic.
        """
        OPTIONS = CommandGroup.OPTIONS
        """
        specifies commands to change options.
        """
        MATH = CommandGroup.MATH
        """
        specifies math specific commands.
        """
        NAVIGATOR = CommandGroup.NAVIGATOR
        """
        specifies navigate commands.
        """
        INSERT = CommandGroup.INSERT
        """
        specifies insert commands.
        """
        FORMAT = CommandGroup.FORMAT
        """
        specifies commands that are related to formats.
        """
        TEMPLATE = CommandGroup.TEMPLATE
        """
        specifies commands that are related to templates.
        """
        TEXT = CommandGroup.TEXT
        """
        specifies text specific commands.
        """
        FRAME = CommandGroup.FRAME
        """
        specifies frame specific commands.
        """
        GRAPHIC = CommandGroup.GRAPHIC
        """
        specifies commands that are related to graphical data.
        """
        TABLE = CommandGroup.TABLE
        """
        specifies commands that are related to tables.
        """
        ENUMERATION = CommandGroup.ENUMERATION
        """
        specifies commands that are related to bullets and numbering.
        """
        DATA = CommandGroup.DATA
        """
        specifies commands that are related to data.
        """
        SPECIAL = CommandGroup.SPECIAL
        """
        specifies special commands.
        """
        IMAGE = CommandGroup.IMAGE
        """
        specifies commands that are related to images.
        """
        CHART = CommandGroup.CHART
        """
        specifies chart specific commands.
        """
        EXPLORER = CommandGroup.EXPLORER
        """
        specifies explorer specific commands.
        """
        CONNECTOR = CommandGroup.CONNECTOR
        """
        specifies commands that are related to connectors.
        """
        MODIFY = CommandGroup.MODIFY
        """
        specifies commands that are related to modifications.
        """
        DRAWING = CommandGroup.DRAWING
        """
        specifies commands that are related to drawing.
        """
        CONTROLS = CommandGroup.CONTROLS
        """
        specifies commands that are related to controls.
        """

__all__ = ['CommandGroup', 'CommandGroupEnum']
