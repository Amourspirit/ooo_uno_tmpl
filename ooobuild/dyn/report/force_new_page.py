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
# Namespace: com.sun.star.report
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.report import ForceNewPage as ForceNewPage
    if hasattr(ForceNewPage, '_constants') and isinstance(ForceNewPage._constants, dict):
        ForceNewPage._constants['__ooo_ns__'] = 'com.sun.star.report'
        ForceNewPage._constants['__ooo_full_ns__'] = 'com.sun.star.report.ForceNewPage'
        ForceNewPage._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global ForceNewPageEnum
        ls = [f for f in dir(ForceNewPage) if not callable(getattr(ForceNewPage, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(ForceNewPage, name)
        ForceNewPageEnum = IntEnum('ForceNewPageEnum', _dict)
    build_enum()
else:
    from ...lo.report.force_new_page import ForceNewPage as ForceNewPage

    class ForceNewPageEnum(IntEnum):
        """
        Enum of Const Class ForceNewPage

        Specifies if the section will be printed on a separate page.
        
        This does not apply to page header or page footer.
        """
        NONE = ForceNewPage.NONE
        """
        The current section is printed on the current page.
        """
        BEFORE_SECTION = ForceNewPage.BEFORE_SECTION
        """
        The current section is printed at the top of a new page.
        """
        AFTER_SECTION = ForceNewPage.AFTER_SECTION
        """
        The next section following the current section is printed at the top of a new page.
        """
        BEFORE_AFTER_SECTION = ForceNewPage.BEFORE_AFTER_SECTION
        """
        The current section is printed at the top of a new page as well as the next section.
        """

__all__ = ['ForceNewPage', 'ForceNewPageEnum']
