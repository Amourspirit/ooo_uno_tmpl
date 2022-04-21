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
# Libre Office Version: 7.2
# Namespace: com.sun.star.report
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.report import SectionPageBreak as SectionPageBreak
    if hasattr(SectionPageBreak, '_constants') and isinstance(SectionPageBreak._constants, dict):
        SectionPageBreak._constants['__ooo_ns__'] = 'com.sun.star.report'
        SectionPageBreak._constants['__ooo_full_ns__'] = 'com.sun.star.report.SectionPageBreak'
        SectionPageBreak._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global SectionPageBreakEnum
        ls = [f for f in dir(SectionPageBreak) if not callable(getattr(SectionPageBreak, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(SectionPageBreak, name)
        SectionPageBreakEnum = IntEnum('SectionPageBreakEnum', _dict)
    build_enum()
else:
    from ...lo.report.section_page_break import SectionPageBreak as SectionPageBreak

    class SectionPageBreakEnum(IntEnum):
        """
        Enum of Const Class SectionPageBreak

        Specifies that page breaks are allowed inside this section.
        """
        NONE = SectionPageBreak.NONE
        """
        Page breaks will never be inserted.
        
        If the section doesn't fit on a page than the content will be cut.
        """
        SECTION = SectionPageBreak.SECTION
        """
        If the section doesn't fit on page than a page break will be inserted as long as the section fits.
        
        Inner sections will doesn't contain further page breaks.
        """
        AUTO = SectionPageBreak.AUTO
        """
        If the section doesn't fit on page than a page break will be inserted as long as the section fits.
        """

__all__ = ['SectionPageBreak', 'SectionPageBreakEnum']
