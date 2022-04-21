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
# Namespace: com.sun.star.frame
from typing_extensions import Literal
import typing
from .x_storable import XStorable as XStorable_998f0aa7
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XStorable2(XStorable_998f0aa7):
    """
    extends XStorable.

    See Also:
        `API XStorable2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XStorable2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XStorable2']

    def storeSelf(self, lArguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        stores the data to the URL from which it was loaded.
        
        Only objects which know their locations can be stored.
        
        This is an extension of the XStorable.store(). This method allows to specify some additional parameters for storing process.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
        """

