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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.util
from __future__ import annotations
import typing
from .x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier_3afb0fb7
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class NumberFormatsSupplier(XNumberFormatsSupplier_3afb0fb7):
    """
    Service Class

    provides an supplier of number formats
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API NumberFormatsSupplier <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1util_1_1NumberFormatsSupplier.html>`_
    """
    def createWithDefaultLocale(self) -> None:
        """
        Create using default locale.
        """
        ...
    def createWithLocale(self, Locale: Locale_70d308fa) -> None:
        """
        Create using specific locale.
        """
        ...

