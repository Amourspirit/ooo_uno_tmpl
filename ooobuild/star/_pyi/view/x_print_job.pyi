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
# Namespace: com.sun.star.view
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_printable import XPrintable as XPrintable_9a5b0abc


class XPrintJob(XInterface_8f010a43):
    """
    allows for getting information about a print job.
    
    XPrintJob is implemented by print jobs that are created by classes that implement XPrintable. It gives information about the context of the print job.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XPrintJob <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1view_1_1XPrintJob.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.view.XPrintJob']

    def cancelJob(self) -> None:
        """
        """
        ...
    def getPrintOptions(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        returns the PrintOptions used for the print job
        """
        ...
    def getPrintable(self) -> 'XPrintable_9a5b0abc':
        """
        returns the printed object used for the print job
        """
        ...
    def getPrinter(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        returns the Printer used for the print job
        """
        ...


