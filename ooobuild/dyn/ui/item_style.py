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
# Namespace: com.sun.star.ui
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.ui import ItemStyle as ItemStyle
    if hasattr(ItemStyle, '_constants') and isinstance(ItemStyle._constants, dict):
        ItemStyle._constants['__ooo_ns__'] = 'com.sun.star.ui'
        ItemStyle._constants['__ooo_full_ns__'] = 'com.sun.star.ui.ItemStyle'
        ItemStyle._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global ItemStyleEnum
        ls = [f for f in dir(ItemStyle) if not callable(getattr(ItemStyle, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(ItemStyle, name)
        ItemStyleEnum = IntEnum('ItemStyleEnum', _dict)
    build_enum()
else:
    from ...lo.ui.item_style import ItemStyle as ItemStyle

    class ItemStyleEnum(IntEnum):
        """
        Enum of Const Class ItemStyle

        specifies styles which influence the appearance and the behavior of an user interface item.
        
        These styles are only valid if the item describes a toolbar or statusbar item. The style values can be combined with the OR operator. Styles which are not valid for an item will be ignored by the implementation.There are two styles where only one value is valid: Alignment:
        
        Drawing:
        
        **since**
        
            OOo 2.0
        """
        ALIGN_LEFT = ItemStyle.ALIGN_LEFT
        """
        specifies how the output of the item is aligned in the bounding box of the user interface element.
        
        This style is only valid for an item which describes a statusbar item. Draw item with a left aligned output.
        """
        ALIGN_CENTER = ItemStyle.ALIGN_CENTER
        """
        specifies how the output of the item is aligned in the bounding box of the user interface element.
        
        This style is only valid for an item which describes a statusbar item. Draw item with a centered aligned output.
        """
        ALIGN_RIGHT = ItemStyle.ALIGN_RIGHT
        """
        specifies how the output of the item is aligned in the bounding box of the user interface element.
        
        This style is only valid for an item which describes a statusbar item. Draw item with a right aligned output.
        """
        DRAW_OUT3D = ItemStyle.DRAW_OUT3D
        """
        specifies how the implementation should draw the item.
        
        This style is only valid for an item which describes a statusbar item. Draw item with an embossed 3D effect.
        """
        DRAW_IN3D = ItemStyle.DRAW_IN3D
        """
        specifies how the implementation should draw the item.
        
        This style is only valid for an item which describes a statusbar item. Draw item with an impressed 3D effect.
        """
        DRAW_FLAT = ItemStyle.DRAW_FLAT
        """
        specifies how the implementation should draw the item.
        
        This style is only valid for an item which describes a statusbar item. Draw item without an 3D effect.
        """
        OWNER_DRAW = ItemStyle.OWNER_DRAW
        """
        specifies whether or not an item is displayed using an external function.
        
        This style is only valid if the item describes a statusbar item.
        """
        AUTO_SIZE = ItemStyle.AUTO_SIZE
        """
        specifies whether or not the size of the item is set automatically by the parent user interface element.
        
        This style is only valid if the item describes a toolbar or statusbar item.
        """
        RADIO_CHECK = ItemStyle.RADIO_CHECK
        """
        determines whether the item unchecks neighbor entries which have also this style set.
        
        This style is only valid if the item describes a toolbar item.
        """
        ICON = ItemStyle.ICON
        """
        specifies if an icon is placed on left side of the text, like an entry in a taskbar.
        
        This style is only valid if the item describes a toolbar item and visible if style of the toolbar is set to symboltext.
        
        This style can also be used for custom toolbars and menus, in a custom toolbar an item's Style setting can used to override the toolbar container setting, the style can be bitwise OR-ed with com.sun.star.ui.ItemStyle.TEXT to define text, text+icon or icon only is to be displayed. Similarly for menu items, an items Style can override the application setting to display either text or icon (note: for menu an icon only setting interpreted as icon+text)
        """
        DROP_DOWN = ItemStyle.DROP_DOWN
        """
        specifies that the item supports a dropdown menu or toolbar for additional functions.
        
        This style is only valid if the item describes a toolbar item.
        """
        REPEAT = ItemStyle.REPEAT
        """
        indicates that the item continues to execute the command while you click and hold the mouse button.
        
        This style is only valid if the item describes a toolbar item.
        """
        DROPDOWN_ONLY = ItemStyle.DROPDOWN_ONLY
        """
        indicates that the item only supports a dropdown menu or toolbar for additional functions.
        
        There is no function on the button itself.
        
        This style is only valid if the item describes a toolbar item.
        """
        TEXT = ItemStyle.TEXT
        """
        indicates if icon, text or text+icon is displayed for the item.
        
        This style can be used for custom toolbars and menus, in a custom toolbar an item's Style setting can used to override the toolbar container setting, the style can be bitwise OR-ed with com.sun.star.ui.ItemStyle.ICON to define text, text+icon or icon only is to be displayed. Similarly for menu items, an items Style can override the application setting to display either text or icon (note: for menu an icon only setting interpreted as icon+text)
        """
        MANDATORY = ItemStyle.MANDATORY
        """
        marks always visible element which can not be removed when statusbar width is not sufficient.
        
        **since**
        
            LibreOffice 6.1
        """

__all__ = ['ItemStyle', 'ItemStyleEnum']
