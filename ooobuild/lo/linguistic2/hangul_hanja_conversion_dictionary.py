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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.linguistic2
from .conversion_dictionary import ConversionDictionary as ConversionDictionary_8fa111b1

class HangulHanjaConversionDictionary(ConversionDictionary_8fa111b1):
    """
    Service Class

    represents a dictionary for Hangul/Hanja text conversion.
    
    A dictionary implementing this service will be used for Hangul/Hanja conversion. Therefore the locale of the dictionary has to be Korean, and the conversion type com.sun.star.linguistic2.ConversionDictionaryType.HANGUL_HANJA.
    
    Also for a pair (entry) to be added the left part has to be in Hangul and the right in Hanja, and the number of characters for the left part has to be the same as for the right part.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API HangulHanjaConversionDictionary <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1linguistic2_1_1HangulHanjaConversionDictionary.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.HangulHanjaConversionDictionary'
    __ooo_type_name__: str = 'service'



__all__ = ['HangulHanjaConversionDictionary']
