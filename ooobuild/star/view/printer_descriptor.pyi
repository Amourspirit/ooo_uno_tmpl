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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.view
from __future__ import annotations
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from com.sun.star.view.PaperFormat import PaperFormatProto
    from com.sun.star.view.PaperOrientation import PaperOrientationProto

class PrinterDescriptor(ABC):
    """
    Service Class

    describes a printer by specifying the queue name and some settings.
    
    This service may be represented by a com.sun.star.beans.PropertyValue[].

    See Also:
        `API PrinterDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1view_1_1PrinterDescriptor.html>`_
    """
    @property
    def CanSetPaperFormat(self) -> bool:
        """
        indicates, whether the printer allows changes to PrinterDescriptor.PaperFormat.
        """
        ...
    @CanSetPaperFormat.setter
    def CanSetPaperFormat(self, value: bool) -> None:
        ...
    @property
    def CanSetPaperOrientation(self) -> bool:
        """
        indicates, whether the printer allows changes to PrinterDescriptor.PaperOrientation.
        """
        ...
    @CanSetPaperOrientation.setter
    def CanSetPaperOrientation(self, value: bool) -> None:
        ...
    @property
    def CanSetPaperSize(self) -> bool:
        """
        indicates if the printer allows changes to PrinterDescriptor.PaperSize.
        """
        ...
    @CanSetPaperSize.setter
    def CanSetPaperSize(self, value: bool) -> None:
        ...
    @property
    def IsBusy(self) -> bool:
        """
        indicates, whether the printer is busy or not.
        """
        ...
    @IsBusy.setter
    def IsBusy(self, value: bool) -> None:
        ...
    @property
    def Name(self) -> str:
        """
        specifies the name of the printer queue to be used.
        
        Which printer queues are available, can be figured out with the system library of the used programming language/environment.
        """
        ...
    @Name.setter
    def Name(self, value: str) -> None:
        ...
    @property
    def PaperFormat(self) -> PaperFormatProto:
        """
        specifies a predefined paper size or if the paper size is a user-defined size.
        
        Setting this property may change the value of PrinterDescriptor.PaperSize.
        """
        ...
    @PaperFormat.setter
    def PaperFormat(self, value: PaperFormatProto) -> None:
        ...
    @property
    def PaperOrientation(self) -> PaperOrientationProto:
        """
        specifies the orientation of the paper.
        """
        ...
    @PaperOrientation.setter
    def PaperOrientation(self, value: PaperOrientationProto) -> None:
        ...
    @property
    def PaperSize(self) -> Size_576707ef:
        """
        specifies the size of the paper in 100th mm.
        
        Setting this property may change the value of PrinterDescriptor.PaperFormat.
        """
        ...
    @PaperSize.setter
    def PaperSize(self, value: Size_576707ef) -> None:
        ...

