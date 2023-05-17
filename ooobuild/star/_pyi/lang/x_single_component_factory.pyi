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
# Namespace: com.sun.star.lang
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..uno.x_component_context import XComponentContext as XComponentContext_e2e10d4a


class XSingleComponentFactory(XInterface_8f010a43):
    """
    Factory interface to create instances of an implementation of a service specification.

    See Also:
        `API XSingleComponentFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XSingleComponentFactory.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.lang.XSingleComponentFactory']

    def createInstanceWithArgumentsAndContext(self, Arguments: 'typing.Tuple[object, ...]', Context: 'XComponentContext_e2e10d4a') -> 'XInterface_8f010a43':
        """
        Creates an instance of a component and initializes the new instance with the given arguments and context.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    def createInstanceWithContext(self, Context: 'XComponentContext_e2e10d4a') -> 'XInterface_8f010a43':
        """
        Creates an instance of a service implementation.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...


