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
# Singleton Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.util
# Libre Office Version: 7.3
from .x_path_settings import XPathSettings as XPathSettings_bc930bfc


class thePathSettings(XPathSettings_bc930bfc):
    """
    Singleton Class

    Supports read/write access and listener for the paths properties that the Office uses.
    
    The property names of the Office paths/directories are an exactly match to the configuration entries found in the file (org/openoffice/Office/Common.xml).
    This service supports the usage of path variables to define paths that a relative to other office or system directories. See PathSubstitution
    
    Prior to LibreOffice 4.3, this singleton was only available as a (single-instance) PathSettings service.
    
    **since**
    
        LibreOffice 4.3

    See Also:
        `API thePathSettings <https://api.libreoffice.org/docs/idl/ref/singletoncom_1_1sun_1_1star_1_1util_1_1thePathSettings.html>`_
    """


