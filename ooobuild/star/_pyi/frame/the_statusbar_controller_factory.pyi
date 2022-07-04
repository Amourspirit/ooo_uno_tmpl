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
# Namespace: com.sun.star.frame
# Libre Office Version: 7.3
from .xui_controller_factory import XUIControllerFactory as XUIControllerFactory_25e60f05


class theStatusbarControllerFactory(XUIControllerFactory_25e60f05):
    """
    Singleton Class

    specifies a factory that creates instances of registered status bar controller.
    
    A status bar controller can be registered for a command URL and a model service name. A status bar will automatically create a status bar controller if it contains a registered command URL.
    
    Prior to LibreOffice 4.3, this singleton was only available as a (single-instance) StatusbarControllerFactory service.
    
    **since**
    
        LibreOffice 4.3

    See Also:
        `API theStatusbarControllerFactory <https://api.libreoffice.org/docs/idl/ref/singletoncom_1_1sun_1_1star_1_1frame_1_1theStatusbarControllerFactory.html>`_
    """
    ...


