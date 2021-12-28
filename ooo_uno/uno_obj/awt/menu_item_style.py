# coding: utf-8
# this is a auto generated file generated by Cheetah
from ...base.const import ConstIntFlagsBase


class MenuItemStyle(ConstIntFlagsBase):
    """
    These values are used to specify the properties of a menu item.

    See Also:
        `API MenuItemStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1MenuItemStyle.html>`_
    """
    AUTOCHECK = 4
    """
    specifies to check this item automatically on select.
    """
    CHECKABLE = 1
    """
    specifies an item which can be checked independently.
    """
    RADIOCHECK = 2
    """
    specifies an item which can be checked dependent on the neighbouring items.
    """
