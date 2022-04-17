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
# Namespace: com.sun.star.text
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
    from ..lang.locale import Locale as Locale_70d308fa

class XDefaultNumberingProvider(XInterface_8f010a43):
    """
    provides access to default com.sun.star.text.NumberingRules according to a given locale information.

    See Also:
        `API XDefaultNumberingProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XDefaultNumberingProvider.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.text.XDefaultNumberingProvider']

    def getDefaultContinuousNumberingLevels(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[PropertyValues_d6470ce6, ...]':
        """
        provides access to outline numberings according to a given com.sun.star.lang.Locale.
        
        In contrast to outline numberings the continuous numberings consist of level using the equal settings in all numbering levels.
        """
    def getDefaultOutlineNumberings(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[XIndexAccess_f0910d6d, ...]':
        """
        provides access to outline numberings according to a given com.sun.star.lang.Locale.
        
        Outline numberings usually consist of levels with different settings.
        """

