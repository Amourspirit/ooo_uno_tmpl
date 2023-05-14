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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.i18n
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class NumberFormatIndex(metaclass=UnoConstMeta, type_name="com.sun.star.i18n.NumberFormatIndex", name_space="com.sun.star.i18n"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.i18n.NumberFormatIndex``"""
        pass

    class NumberFormatIndexEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.i18n.NumberFormatIndex", name_space="com.sun.star.i18n"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.i18n.NumberFormatIndex`` as Enum values"""
        pass

else:
    from ...lo.i18n.number_format_index import NumberFormatIndex as NumberFormatIndex

    class NumberFormatIndexEnum(IntEnum):
        """
        Enum of Const Class NumberFormatIndex

        Do NOT insert any new values! Locale data number format creation must match these values! Number formatter internals must match these values!
        
        Number format indices to be passed as the index argument to XNumberFormatCode.getFormatCode() or com.sun.star.util.XNumberFormatTypes.getFormatIndex().
        
        Each locale can support up to about 5000 arbitrary format codes. But for backward compatibility reasons, each locale MUST support some predefined format codes. These predefined format codes are accessed through indices as the following, and the locale data format code definitions in i18npool/source/localedata/data/*.xml MUST have matching entries in the form
        
        <FormatElement formatindex=\"0\">
        
        (see also FormatElement.formatIndex()).
        
        The index values are also used to define the enum NfIndexTableOffset in file svtools/inc/zforlist.hxx
        
        Note: This index has nothing to do with the index key used internally by the number formatter.
        
        Date formats may have a comment of DIN/EN/ISO, meaning
        
        Some names of date format constants indicate a special behavior of those formats in StarOffice 5.2 or older. Those are:
        """
        NUMBER_START = NumberFormatIndex.NUMBER_START
        """
        Start of simple numerical formats (first format)
        """
        NUMBER_STANDARD = NumberFormatIndex.NUMBER_STANDARD
        """
        The \"General\" standard format formatindex=\"0\".
        """
        NUMBER_INT = NumberFormatIndex.NUMBER_INT
        """
        0 Integer number formatindex=\"1\"
        """
        NUMBER_DEC2 = NumberFormatIndex.NUMBER_DEC2
        """
        0.00 Decimal number with 2 decimals formatindex=\"2\"
        """
        NUMBER_1000INT = NumberFormatIndex.NUMBER_1000INT
        """
        #,##0 Integer number with group separator formatindex=\"3\"
        """
        NUMBER_1000DEC2 = NumberFormatIndex.NUMBER_1000DEC2
        """
        #,##0.00 Decimal number with group separator formatindex=\"4\"
        """
        NUMBER_SYSTEM = NumberFormatIndex.NUMBER_SYSTEM
        """
        #,##0.00 In SO5/Win this format was retrieved from the Regional Settings formatindex=\"5\"
        """
        NUMBER_END = NumberFormatIndex.NUMBER_END
        """
        End of simple numerical formats (last format)
        """
        SCIENTIFIC_START = NumberFormatIndex.SCIENTIFIC_START
        """
        Start of Scientific formats (first format)
        """
        SCIENTIFIC_000E000 = NumberFormatIndex.SCIENTIFIC_000E000
        """
        0.00E+000 Number in scientific notation with exponent in 3 digit placeholders formatindex=\"6\"
        """
        SCIENTIFIC_000E00 = NumberFormatIndex.SCIENTIFIC_000E00
        """
        0.00E+00 Number in scientific notation with exponent in 2 digit placeholders formatindex=\"7\"
        """
        SCIENTIFIC_END = NumberFormatIndex.SCIENTIFIC_END
        """
        End of Scientific formats (last format)
        """
        PERCENT_START = NumberFormatIndex.PERCENT_START
        """
        Start of Percent formats (first format)
        """
        PERCENT_INT = NumberFormatIndex.PERCENT_INT
        """
        0% Percentage format, rounded to integer formatindex=\"8\"
        """
        PERCENT_DEC2 = NumberFormatIndex.PERCENT_DEC2
        """
        0.00% Percentage format, rounded to 2 decimals formatindex=\"9\"
        """
        PERCENT_END = NumberFormatIndex.PERCENT_END
        """
        End of Percent formats (last format)
        """
        FRACTION_START = NumberFormatIndex.FRACTION_START
        """
        Start of Fraction formats (first format)
        """
        FRACTION_1 = NumberFormatIndex.FRACTION_1
        FRACTION_2 = NumberFormatIndex.FRACTION_2
        FRACTION_END = NumberFormatIndex.FRACTION_END
        """
        End of Fraction formats (last format)
        """
        CURRENCY_START = NumberFormatIndex.CURRENCY_START
        """
        Start of Currency formats (first format)
        """
        CURRENCY_1000INT = NumberFormatIndex.CURRENCY_1000INT
        """
        #,##0 DM Integer currency format with group separator formatindex=\"12\"
        """
        CURRENCY_1000DEC2 = NumberFormatIndex.CURRENCY_1000DEC2
        """
        #,##0.00 DM Decimal currency format with group separator formatindex=\"13\"
        """
        CURRENCY_1000INT_RED = NumberFormatIndex.CURRENCY_1000INT_RED
        """
        #,##0 DM Integer currency format with negative in red formatindex=\"14\"
        """
        CURRENCY_1000DEC2_RED = NumberFormatIndex.CURRENCY_1000DEC2_RED
        """
        #,##0.00 DM Decimal currency format with negative in red formatindex=\"15\"
        """
        CURRENCY_1000DEC2_CCC = NumberFormatIndex.CURRENCY_1000DEC2_CCC
        """
        #,##0.00 DEM Currency in ISO-4217 abbreviation format formatindex=\"16\"
        """
        CURRENCY_1000DEC2_DASHED = NumberFormatIndex.CURRENCY_1000DEC2_DASHED
        """
        #,##0.– DM Currency format with dash representing 0 in decimals formatindex=\"17\"
        """
        CURRENCY_END = NumberFormatIndex.CURRENCY_END
        """
        End of Currency formats (last format)
        """
        DATE_START = NumberFormatIndex.DATE_START
        """
        Start of Date formats (first format)
        """
        DATE_SYSTEM_SHORT = NumberFormatIndex.DATE_SYSTEM_SHORT
        """
        08.10.97 see also DATE_SYSTEM_... explanation formatindex=\"18\"
        """
        DATE_SYSTEM_LONG = NumberFormatIndex.DATE_SYSTEM_LONG
        """
        Wednesday, 8.
        
        October 1997 see also DATE_SYSTEM_... explanation formatindex=\"19\"
        """
        DATE_SYS_DDMMYY = NumberFormatIndex.DATE_SYS_DDMMYY
        """
        08.10.97 see also DATE_SYS_... explanation formatindex=\"20\"
        """
        DATE_SYS_DDMMYYYY = NumberFormatIndex.DATE_SYS_DDMMYYYY
        """
        08.10.1997 see also DATE_SYS_...
        
        explanation Note: When editing already existing date data this format is forced in order to always edit the full century. formatindex=\"21\"
        """
        DATE_SYS_DMMMYY = NumberFormatIndex.DATE_SYS_DMMMYY
        DATE_SYS_DMMMYYYY = NumberFormatIndex.DATE_SYS_DMMMYYYY
        DATE_DIN_DMMMYYYY = NumberFormatIndex.DATE_DIN_DMMMYYYY
        DATE_SYS_DMMMMYYYY = NumberFormatIndex.DATE_SYS_DMMMMYYYY
        DATE_DIN_DMMMMYYYY = NumberFormatIndex.DATE_DIN_DMMMMYYYY
        DATE_SYS_NNDMMMYY = NumberFormatIndex.DATE_SYS_NNDMMMYY
        """
        Wed, 8. Oct 97 see also DATE_SYS_... explanation formatindex=\"27\".
        """
        DATE_DEF_NNDDMMMYY = NumberFormatIndex.DATE_DEF_NNDDMMMYY
        """
        Wed 08.Oct 97 see also DATE_DEF_... explanation formatindex=\"28\".
        """
        DATE_SYS_NNDMMMMYYYY = NumberFormatIndex.DATE_SYS_NNDMMMMYYYY
        """
        Wed, 8. October 1997 see also DATE_SYS_... explanation formatindex=\"29\".
        """
        DATE_SYS_NNNNDMMMMYYYY = NumberFormatIndex.DATE_SYS_NNNNDMMMMYYYY
        """
        Wednesday, 8. October 1997 formatindex=\"30\".
        """
        DATE_DIN_MMDD = NumberFormatIndex.DATE_DIN_MMDD
        """
        10-08 DIN/EN formatindex=\"31\"
        """
        DATE_DIN_YYMMDD = NumberFormatIndex.DATE_DIN_YYMMDD
        """
        97-10-08 DIN/EN formatindex=\"32\"
        """
        DATE_DIN_YYYYMMDD = NumberFormatIndex.DATE_DIN_YYYYMMDD
        """
        1997-10-08 DIN/EN/ISO formatindex=\"33\"
        """
        DATE_SYS_MMYY = NumberFormatIndex.DATE_SYS_MMYY
        """
        10.97 see also DATE_SYS_... explanation formatindex=\"34\"
        """
        DATE_SYS_DDMMM = NumberFormatIndex.DATE_SYS_DDMMM
        """
        08.Oct see also DATE_SYS_... explanation formatindex=\"35\"
        """
        DATE_MMMM = NumberFormatIndex.DATE_MMMM
        """
        October formatindex=\"36\".
        """
        DATE_QQJJ = NumberFormatIndex.DATE_QQJJ
        """
        4th quarter 97 formatindex=\"37\"
        """
        DATE_WW = NumberFormatIndex.DATE_WW
        """
        week of year formatindex=\"38\"
        """
        DATE_END = NumberFormatIndex.DATE_END
        """
        End of Date formats (last format)
        """
        TIME_START = NumberFormatIndex.TIME_START
        """
        Start of Time formats (first format)
        """
        TIME_HHMM = NumberFormatIndex.TIME_HHMM
        """
        HH:MM Time format with hour and minute formatindex=\"39\".
        """
        TIME_HHMMSS = NumberFormatIndex.TIME_HHMMSS
        """
        HH:MM:SS Time format with hour, minute and second formatindex=\"40\".
        """
        TIME_HHMMAMPM = NumberFormatIndex.TIME_HHMMAMPM
        """
        HH:MM AM/PM Time format with hour, minute and morning/afternoon notation formatindex=\"41\".
        """
        TIME_HHMMSSAMPM = NumberFormatIndex.TIME_HHMMSSAMPM
        """
        HH:MM:SS AM/PM Time format with hour, minute, second and morning/afternoon notation formatindex=\"42\".
        """
        TIME_HH_MMSS = NumberFormatIndex.TIME_HH_MMSS
        """
        [HH]:MM:SS Time format with amount of hours formatindex=\"43\"
        """
        TIME_MMSS00 = NumberFormatIndex.TIME_MMSS00
        """
        MM:SS,00 Time format with second in fraction formatindex=\"44\".
        """
        TIME_HH_MMSS00 = NumberFormatIndex.TIME_HH_MMSS00
        """
        [HH]:MM:SS,00 Time format with amount of hours and seconds with fraction formatindex=\"45\"
        """
        TIME_END = NumberFormatIndex.TIME_END
        """
        End of Time formats (last format)
        """
        DATETIME_START = NumberFormatIndex.DATETIME_START
        """
        Start of DateTime formats (first format)
        """
        DATETIME_SYSTEM_SHORT_HHMM = NumberFormatIndex.DATETIME_SYSTEM_SHORT_HHMM
        """
        08.10.97 01:23 Date/time format formatindex=\"46\"
        """
        DATETIME_SYS_DDMMYYYY_HHMMSS = NumberFormatIndex.DATETIME_SYS_DDMMYYYY_HHMMSS
        """
        08.10.1997 01:23:45 Date/time format with second Note: When editing already existing date/time data this format is forced in order to always edit the full century.
        
        formatindex=\"47\"
        """
        DATETIME_END = NumberFormatIndex.DATETIME_END
        """
        End of DateTime formats (last format)
        """
        BOOLEAN = NumberFormatIndex.BOOLEAN
        """
        BOOLEAN format.
        """
        TEXT = NumberFormatIndex.TEXT
        """
        Text format.
        """
        INDEX_TABLE_ENTRIES = NumberFormatIndex.INDEX_TABLE_ENTRIES
        """
        count of built-in format codes.
        """

__all__ = ['NumberFormatIndex', 'NumberFormatIndexEnum']
