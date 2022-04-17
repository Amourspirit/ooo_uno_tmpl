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
# Namespace: com.sun.star.awt
from typing_extensions import Literal
from abc import ABC

class XMessageBox(ABC):
    """
    gives access to a message box.

    See Also:
        `API XMessageBox <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XMessageBox.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XMessageBox']

    def execute(self) -> int:
        """
        shows the message box.
        """
    @property
    def CaptionText(self) -> str:
        """
        the caption text.
        """

    @property
    def MessageText(self) -> str:
        """
        the message text.
        """


