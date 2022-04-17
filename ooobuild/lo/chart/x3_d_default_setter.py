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
# Namespace: com.sun.star.chart
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class X3DDefaultSetter(XInterface_8f010a43):
    """
    makes it easy to set suitable defaults for illumination and rotation for 3D charts

    See Also:
        `API X3DDefaultSetter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart_1_1X3DDefaultSetter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.X3DDefaultSetter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart.X3DDefaultSetter'

    @abstractmethod
    def set3DSettingsToDefault(self) -> None:
        """
        The result may depend on the current chart type and the current shade mode.
        """
    @abstractmethod
    def setDefaultIllumination(self) -> None:
        """
        set suitable defaults for the illumination of the current 3D chart.
        
        The result may dependent on other 3D settings as rotation or shade mode. It may depend on the current chart type also.
        """
    @abstractmethod
    def setDefaultRotation(self) -> None:
        """
        sets a suitable default for the rotation of the current 3D chart.
        
        The result may depend on the current chart type.
        """

__all__ = ['X3DDefaultSetter']

