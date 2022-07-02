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
# Libre Office Version: 7.2
# Namespace: com.sun.star.xml.crypto.sax
from typing_extensions import Literal
from ....uno.x_interface import XInterface as XInterface_8f010a43

class XBlockerMonitor(XInterface_8f010a43):
    """
    Interface of Blocker Monitor.
    
    This interface is used to manipulate a blocker.

    See Also:
        `API XBlockerMonitor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1sax_1_1XBlockerMonitor.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.crypto.sax.XBlockerMonitor']

    def setBlockerId(self, id: int) -> None:
        """
        Configures the blocker's id.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...


