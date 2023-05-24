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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.presentation
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoEnumMeta
    class ClickAction(metaclass=UnoEnumMeta, type_name="com.sun.star.presentation.ClickAction", name_space="com.sun.star.presentation"):
        """Dynamically created class that represents ``com.sun.star.presentation.ClickAction`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.presentation.ClickAction import BOOKMARK as CLICK_ACTION_BOOKMARK
        from com.sun.star.presentation.ClickAction import DOCUMENT as CLICK_ACTION_DOCUMENT
        from com.sun.star.presentation.ClickAction import FIRSTPAGE as CLICK_ACTION_FIRSTPAGE
        from com.sun.star.presentation.ClickAction import INVISIBLE as CLICK_ACTION_INVISIBLE
        from com.sun.star.presentation.ClickAction import LASTPAGE as CLICK_ACTION_LASTPAGE
        from com.sun.star.presentation.ClickAction import MACRO as CLICK_ACTION_MACRO
        from com.sun.star.presentation.ClickAction import NEXTPAGE as CLICK_ACTION_NEXTPAGE
        from com.sun.star.presentation.ClickAction import NONE as CLICK_ACTION_NONE
        from com.sun.star.presentation.ClickAction import PREVPAGE as CLICK_ACTION_PREVPAGE
        from com.sun.star.presentation.ClickAction import PROGRAM as CLICK_ACTION_PROGRAM
        from com.sun.star.presentation.ClickAction import SOUND as CLICK_ACTION_SOUND
        from com.sun.star.presentation.ClickAction import STOPPRESENTATION as CLICK_ACTION_STOPPRESENTATION
        from com.sun.star.presentation.ClickAction import VANISH as CLICK_ACTION_VANISH
        from com.sun.star.presentation.ClickAction import VERB as CLICK_ACTION_VERB

        class ClickAction(uno.Enum):
            """
            Enum Class


            See Also:
                `API ClickAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1presentation.html#a85fe75121d351785616b75b2c5661d8f>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.presentation.ClickAction', value)

            __ooo_ns__: str = 'com.sun.star.presentation'
            __ooo_full_ns__: str = 'com.sun.star.presentation.ClickAction'
            __ooo_type_name__: str = 'enum'

            BOOKMARK = CLICK_ACTION_BOOKMARK
            """
            The presentation jumps to a bookmark.
            """
            DOCUMENT = CLICK_ACTION_DOCUMENT
            """
            The presentation jumps to another document.
            """
            FIRSTPAGE = CLICK_ACTION_FIRSTPAGE
            """
            The presentation continues with the first page.
            """
            INVISIBLE = CLICK_ACTION_INVISIBLE
            """
            The object renders itself invisible after a click.
            """
            LASTPAGE = CLICK_ACTION_LASTPAGE
            """
            The presentation continues with the last page.
            """
            MACRO = CLICK_ACTION_MACRO
            """
            A star basic macro is executed after the click.
            """
            NEXTPAGE = CLICK_ACTION_NEXTPAGE
            """
            The presentation jumps to the next page.
            """
            NONE = CLICK_ACTION_NONE
            """
            use no animation effects.

            use no fade effects.

            No action is performed on click.
            """
            PREVPAGE = CLICK_ACTION_PREVPAGE
            """
            The presentation jumps to the previous page.
            """
            PROGRAM = CLICK_ACTION_PROGRAM
            """
            Another program is executed after a click.
            """
            SOUND = CLICK_ACTION_SOUND
            """
            A sound is played after a click.
            """
            STOPPRESENTATION = CLICK_ACTION_STOPPRESENTATION
            """
            The presentation is stopped after the click.
            """
            VANISH = CLICK_ACTION_VANISH
            """
            The object vanishes with its effect.
            """
            VERB = CLICK_ACTION_VERB
            """
            An OLE verb is performed on this object.
            """
    else:
        # keep document generators happy
        from ...lo.presentation.click_action import ClickAction as ClickAction


__all__ = ['ClickAction']
