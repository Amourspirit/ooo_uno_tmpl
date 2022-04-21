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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing
from .rectangle import Rectangle as Rectangle_84b109e9


class DockingData(object):
    """
    Struct Class

    data returned by docking handler

    See Also:
        `API DockingData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1DockingData.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.DockingData'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.DockingData'
    """Literal Constant ``com.sun.star.awt.DockingData``"""

    def __init__(self, TrackingRectangle: typing.Optional[Rectangle_84b109e9] = UNO_NONE, bFloating: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            TrackingRectangle (Rectangle, optional): TrackingRectangle value.
            bFloating (bool, optional): bFloating value.
        """
        super().__init__()

        if isinstance(TrackingRectangle, DockingData):
            oth: DockingData = TrackingRectangle
            self.TrackingRectangle = oth.TrackingRectangle
            self.bFloating = oth.bFloating
            return

        kargs = {
            "TrackingRectangle": TrackingRectangle,
            "bFloating": bFloating,
        }
        if kargs["TrackingRectangle"] is UNO_NONE:
            kargs["TrackingRectangle"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._tracking_rectangle = kwargs["TrackingRectangle"]
        self._b_floating = kwargs["bFloating"]


    @property
    def TrackingRectangle(self) -> Rectangle_84b109e9:
        """
        specifies the position and size where the window would be placed if the user releases the mouse
        """
        return self._tracking_rectangle
    
    @TrackingRectangle.setter
    def TrackingRectangle(self, value: Rectangle_84b109e9) -> None:
        self._tracking_rectangle = value

    @property
    def bFloating(self) -> bool:
        """
        specifies that the window should be floating (TRUE) or docked (FALSE)
        """
        return self._b_floating
    
    @bFloating.setter
    def bFloating(self, value: bool) -> None:
        self._b_floating = value


__all__ = ['DockingData']
