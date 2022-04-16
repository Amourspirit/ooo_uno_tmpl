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
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .text_markup_descriptor import TextMarkupDescriptor as TextMarkupDescriptor_1dcb0f01

class XMultiTextMarkup(ABC):
    """
    provides functionality to apply multiple text markups in one call.
    
    **since**
    
        OOo 3.0.1

    See Also:
        `API XMultiTextMarkup <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XMultiTextMarkup.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XMultiTextMarkup'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XMultiTextMarkup'

    @abstractmethod
    def commitMultiTextMarkup(self, aMarkups: 'typing.Tuple[TextMarkupDescriptor_1dcb0f01, ...]') -> None:
        """
        submits multiple new markup ranges.
        
        The main use of this function will probably be for proofreading to allow for setting the markup of all found errors in a sentence in a single call. For this the sequence needs to provide the markups for all errors along with the markup for the identified sentence boundaries. The order of those entries is arbitrary.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XMultiTextMarkup']

