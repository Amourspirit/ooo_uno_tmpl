# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from .x_model2 import XModel2 as XModel2_83fc098e
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73


class XModel3(XModel2_83fc098e):
    """
    extends interface XModel2 with optimised read access getArgs().

    See Also:
        `API XModel3 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XModel3.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XModel3'

    def getArgs2(self, requestedArgs: typing.Tuple[str, ...]) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        Provides optimised read access (so we don't need to fetch expensive properties that we are not interested in) on currently representation of the com.sun.star.document.MediaDescriptor of this model which describes the model and its state.
        
        Returns only the selected args.
        """
        ...


