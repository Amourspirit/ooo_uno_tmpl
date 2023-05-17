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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.document
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from abc import ABC


class XUndoAction(ABC):
    """
    represents a single (undoable) action on a document
    
    **since**
    
        OOo 3.4

    See Also:
        `API XUndoAction <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XUndoAction.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.document.XUndoAction']

    def redo(self) -> None:
        """
        repeats the action represented by the instance, after it had previously been reverted.

        Raises:
            com.sun.star.document.UndoFailedException: ``UndoFailedException``
        """
        ...
    def undo(self) -> None:
        """
        reverts the action represented by the instance

        Raises:
            com.sun.star.document.UndoFailedException: ``UndoFailedException``
        """
        ...

    @property
    def Title(self) -> str:
        """
        is the human-readable, localized description of the action.
        """
        ...
    @Title.setter
    def Title(self, value: str) -> None:
        ...

