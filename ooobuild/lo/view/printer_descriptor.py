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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.view
import typing
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from .paper_format import PaperFormat as PaperFormat_a5340b24
    from .paper_orientation import PaperOrientation as PaperOrientation_e36f0d47

class PrinterDescriptor(ABC):
    """
    Service Class

    describes a printer by specifying the queue name and some settings.
    
    This service may be represented by a com.sun.star.beans.PropertyValue[].

    See Also:
        `API PrinterDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1view_1_1PrinterDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.view'
    __ooo_full_ns__: str = 'com.sun.star.view.PrinterDescriptor'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CanSetPaperFormat(self) -> bool:
        """
        indicates, whether the printer allows changes to PrinterDescriptor.PaperFormat.
        """
        ...

    @abstractproperty
    def CanSetPaperOrientation(self) -> bool:
        """
        indicates, whether the printer allows changes to PrinterDescriptor.PaperOrientation.
        """
        ...

    @abstractproperty
    def CanSetPaperSize(self) -> bool:
        """
        indicates if the printer allows changes to PrinterDescriptor.PaperSize.
        """
        ...

    @abstractproperty
    def IsBusy(self) -> bool:
        """
        indicates, whether the printer is busy or not.
        """
        ...

    @abstractproperty
    def Name(self) -> str:
        """
        specifies the name of the printer queue to be used.
        
        Which printer queues are available, can be figured out with the system library of the used programming language/environment.
        """
        ...

    @abstractproperty
    def PaperFormat(self) -> 'PaperFormat_a5340b24':
        """
        specifies a predefined paper size or if the paper size is a user-defined size.
        
        Setting this property may change the value of PrinterDescriptor.PaperSize.
        """
        ...

    @abstractproperty
    def PaperOrientation(self) -> 'PaperOrientation_e36f0d47':
        """
        specifies the orientation of the paper.
        """
        ...

    @abstractproperty
    def PaperSize(self) -> 'Size_576707ef':
        """
        specifies the size of the paper in 100th mm.
        
        Setting this property may change the value of PrinterDescriptor.PaperFormat.
        """
        ...



__all__ = ['PrinterDescriptor']

