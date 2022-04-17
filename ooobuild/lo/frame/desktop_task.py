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
# Libre Office Version: 7.3
# Namespace: com.sun.star.frame
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_desktop_task import XDesktopTask as XDesktopTask_bb4c0bd8
from .x_frames_supplier import XFramesSupplier as XFramesSupplier_e12a0d1d
from .x_window_arranger import XWindowArranger as XWindowArranger_e1820d15
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e
    from ..awt.size import Size as Size_576707ef

class DesktopTask(XPropertySet_bc180bfa, XDesktopTask_bb4c0bd8, XFramesSupplier_e12a0d1d, XWindowArranger_e1820d15):
    """
    Service Class

    use the Frame service instead of this
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API DesktopTask <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1DesktopTask.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.DesktopTask'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def IsAlwaysVisible(self) -> bool:
        """
        """

    @abstractproperty
    def IsDesktop(self) -> bool:
        """
        """

    @abstractproperty
    def IsFloating(self) -> bool:
        """
        """

    @abstractproperty
    def IsVisible(self) -> bool:
        """
        use th visible state of the frame container window instead of this
        """

    @abstractproperty
    def Position(self) -> 'Point_5fb2085e':
        """
        use the position of the frame container window instead of this
        """

    @abstractproperty
    def Size(self) -> 'Size_576707ef':
        """
        use the size of the frame container window instead of this
        """

    @abstractproperty
    def Title(self) -> str:
        """
        use property Frame.Title instead of that
        """



__all__ = ['DesktopTask']

