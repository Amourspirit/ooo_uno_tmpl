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
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing


class ContextInformation(object):
    """
    Struct Class

    provides information about a certain stack frame.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API ContextInformation <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1ContextInformation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.ContextInformation'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.script.ContextInformation'
    """Literal Constant ``com.sun.star.script.ContextInformation``"""

    def __init__(self, LocalVariableNames: typing.Optional[typing.Tuple[str, ...]] = (), Name: typing.Optional[str] = '', SourceCode: typing.Optional[str] = '', StartLine: typing.Optional[int] = 0, StartColumn: typing.Optional[int] = 0, EndLine: typing.Optional[int] = 0, EndColumn: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            LocalVariableNames (typing.Tuple[str, ...], optional): LocalVariableNames value.
            Name (str, optional): Name value.
            SourceCode (str, optional): SourceCode value.
            StartLine (int, optional): StartLine value.
            StartColumn (int, optional): StartColumn value.
            EndLine (int, optional): EndLine value.
            EndColumn (int, optional): EndColumn value.
        """
        super().__init__()

        if isinstance(LocalVariableNames, ContextInformation):
            oth: ContextInformation = LocalVariableNames
            self.LocalVariableNames = oth.LocalVariableNames
            self.Name = oth.Name
            self.SourceCode = oth.SourceCode
            self.StartLine = oth.StartLine
            self.StartColumn = oth.StartColumn
            self.EndLine = oth.EndLine
            self.EndColumn = oth.EndColumn
            return

        kargs = {
            "LocalVariableNames": LocalVariableNames,
            "Name": Name,
            "SourceCode": SourceCode,
            "StartLine": StartLine,
            "StartColumn": StartColumn,
            "EndLine": EndLine,
            "EndColumn": EndColumn,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._local_variable_names = kwargs["LocalVariableNames"]
        self._name = kwargs["Name"]
        self._source_code = kwargs["SourceCode"]
        self._start_line = kwargs["StartLine"]
        self._start_column = kwargs["StartColumn"]
        self._end_line = kwargs["EndLine"]
        self._end_column = kwargs["EndColumn"]


    @property
    def LocalVariableNames(self) -> typing.Tuple[str, ...]:
        """
        Get all names of the local variable in this context.
        """
        return self._local_variable_names
    
    @LocalVariableNames.setter
    def LocalVariableNames(self, value: typing.Tuple[str, ...]) -> None:
        self._local_variable_names = value

    @property
    def Name(self) -> str:
        """
        Full qualified name to address the module or function associated with the context.
        
        If the module or function can't be addressed by name, e.g., in case that a runtime generated eval-module is executed, this string is empty
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def SourceCode(self) -> str:
        """
        Source code of the Module, that is associated with the context.
        
        If the source can be accessed using the ModuleName or if the source is unknown (executing compiled code) this string can be empty.
        """
        return self._source_code
    
    @SourceCode.setter
    def SourceCode(self, value: str) -> None:
        self._source_code = value

    @property
    def StartLine(self) -> int:
        """
        contains the first line in the module's source code associated with the context.
        
        If \"name\" addresses a function, all line and column values are nevertheless given relative to the module's source. If source code is not available, this value addresses a binary position in the compiled code.
        """
        return self._start_line
    
    @StartLine.setter
    def StartLine(self, value: int) -> None:
        self._start_line = value

    @property
    def StartColumn(self) -> int:
        """
        contains the first column in the StartLine associated with the context.
        """
        return self._start_column
    
    @StartColumn.setter
    def StartColumn(self, value: int) -> None:
        self._start_column = value

    @property
    def EndLine(self) -> int:
        """
        contains the last line in the module's source code associated with the context.
        """
        return self._end_line
    
    @EndLine.setter
    def EndLine(self, value: int) -> None:
        self._end_line = value

    @property
    def EndColumn(self) -> int:
        """
        contains the first column in the EndLine that is NOT associated with the context.
        """
        return self._end_column
    
    @EndColumn.setter
    def EndColumn(self, value: int) -> None:
        self._end_column = value


__all__ = ['ContextInformation']
