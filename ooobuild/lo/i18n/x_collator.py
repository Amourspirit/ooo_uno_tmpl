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
# Namespace: com.sun.star.i18n
from __future__ import annotations
import typing
import uno
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XCollator(XInterface_8f010a43):
    """
    provides locale-sensitive collation algorithms for string comparison.

    See Also:
        `API XCollator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XCollator.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.XCollator'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.i18n.XCollator'

    @abstractmethod
    def compareString(self, aStr1: str, aStr2: str) -> int:
        """
        Compare 2 strings in specific locale and algorithm.
        """
        ...
    @abstractmethod
    def compareSubstring(self, aStr1: str, nOff1: int, nLen1: int, aStr2: str, nOff2: int, nLen2: int) -> int:
        """
        Compare 2 substrings in specific locale and algorithm.
        """
        ...
    @abstractmethod
    def listCollatorAlgorithms(self, aLocale: Locale_70d308fa) -> typing.Tuple[str, ...]:
        """
        List all collator algorithms for a given locale.
        """
        ...
    @abstractmethod
    def listCollatorOptions(self, aAlgorithmName: str) -> uno.ByteSequence:
        """
        List all end user collator options for a given algorithm.
        """
        ...
    @abstractmethod
    def loadCollatorAlgorithm(self, aAlgorithmName: str, aLocale: Locale_70d308fa, nCollatorOptions: int) -> int:
        """
        Load a particular collator algorithm for the locale.
        """
        ...
    @abstractmethod
    def loadCollatorAlgorithmWithEndUserOption(self, aAlgorithmName: str, aLocale: Locale_70d308fa, aCollatorOptions: uno.ByteSequence) -> None:
        """
        Load a collator algorithm with options chosen by end user.
        """
        ...
    @abstractmethod
    def loadDefaultCollator(self, aLocale: Locale_70d308fa, nCollatorOptions: int) -> int:
        """
        Load the collator with default algorithm defined in locale data.
        """
        ...

__all__ = ['XCollator']


