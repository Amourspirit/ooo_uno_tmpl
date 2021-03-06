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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.chart
from typing_extensions import Literal


class ChartSymbolType(object):
    """
    Const

    These values specify the type of the symbol used for data points.
    
    This only applies to diagrams that use symbols like line diagrams.
    
    The default symbols are currently:

    See Also:
        `API ChartSymbolType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart_1_1ChartSymbolType.html>`_
    """
    NONE: Literal[-3]
    """
    No symbol is used.
    """
    AUTO: Literal[-2]
    """
    The symbol is selected automatically.
    
    The size of symbol will be dynamic and the type depends on the data row number.
    """
    BITMAPURL: Literal[-1]
    """
    Take a Bitmap from a URL and use this as symbol.
    
    The bitmap given by the URL set in the property ChartDataPointProperties.SymbolBitmapURL is copied so that the graphic is embedded.
    """
    SYMBOL0: Literal[0]
    """
    The default symbol for row 0 is used.
    """
    SYMBOL1: Literal[1]
    """
    The default symbol for row 1 is used.
    """
    SYMBOL2: Literal[2]
    """
    The default symbol for row 2 is used.
    """
    SYMBOL3: Literal[3]
    """
    The default symbol for row 3 is used.
    """
    SYMBOL4: Literal[4]
    """
    The default symbol for row 4 is used.
    """
    SYMBOL5: Literal[5]
    """
    The default symbol for row 5 is used.
    """
    SYMBOL6: Literal[6]
    """
    The default symbol for row 6 is used.
    """
    SYMBOL7: Literal[7]
    """
    The default symbol for row 7 is used.
    """

