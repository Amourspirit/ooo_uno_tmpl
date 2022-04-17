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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.i18n
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.i18n import KNumberFormatUsage as KNumberFormatUsage
    if hasattr(KNumberFormatUsage, '_constants') and isinstance(KNumberFormatUsage._constants, dict):
        KNumberFormatUsage._constants['__ooo_ns__'] = 'com.sun.star.i18n'
        KNumberFormatUsage._constants['__ooo_full_ns__'] = 'com.sun.star.i18n.KNumberFormatUsage'
        KNumberFormatUsage._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global KNumberFormatUsageEnum
        ls = [f for f in dir(KNumberFormatUsage) if not callable(getattr(KNumberFormatUsage, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(KNumberFormatUsage, name)
        KNumberFormatUsageEnum = IntEnum('KNumberFormatUsageEnum', _dict)
    build_enum()
else:
    from ...lo.i18n.k_number_format_usage import KNumberFormatUsage as KNumberFormatUsage

    class KNumberFormatUsageEnum(IntEnum):
        """
        Enum of Const Class KNumberFormatUsage

        Category of number format code.
        """
        DATE = KNumberFormatUsage.DATE
        """
        Date format, for example, \"YYYY-MM-DD\".
        """
        TIME = KNumberFormatUsage.TIME
        """
        Time format, for example, \"HH:MM:SS\".
        """
        DATE_TIME = KNumberFormatUsage.DATE_TIME
        """
        Mixed date/time format, for example, \"YYYY-MM-DD HH:MM:SS\".
        """
        FIXED_NUMBER = KNumberFormatUsage.FIXED_NUMBER
        """
        Numeric format, for example, \"#,##0.00\".
        """
        FRACTION_NUMBER = KNumberFormatUsage.FRACTION_NUMBER
        """
        Fractional format, for example, \"# ??/??\".
        """
        PERCENT_NUMBER = KNumberFormatUsage.PERCENT_NUMBER
        """
        Percent format, for example, \"0.00%\".
        """
        SCIENTIFIC_NUMBER = KNumberFormatUsage.SCIENTIFIC_NUMBER
        """
        Scientific format, for example, \"0.00E+00\".
        """
        CURRENCY = KNumberFormatUsage.CURRENCY
        """
        Currency format, for example, \"#,##0.00 [$EUR]\".
        """

__all__ = ['KNumberFormatUsage', 'KNumberFormatUsageEnum']
