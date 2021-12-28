# coding: utf-8
# this is a auto generated file generated by Cheetah
from ...base.const import ConstIntBase


class MessageBoxButtons(ConstIntBase):
    """
    defines constants for the possible message box button combinations.

    See Also:
        `API MessageBoxButtons <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1MessageBoxButtons.html>`_
    """
    BUTTONS_ABORT_IGNORE_RETRY = int('0x6', 16)
    """
    specifies a message box with "ABORT", "IGNORE" and "RETRY" button.
    """
    BUTTONS_OK = int('0x1', 16)
    """
    specifies a message with "OK" button.
    """
    BUTTONS_OK_CANCEL = int('0x2', 16)
    """
    specifies a message box with "OK" and "CANCEL" button.
    """
    BUTTONS_RETRY_CANCEL = int('0x5', 16)
    """
    specifies a message box with "RETRY" and "CANCEL" button.
    """
    BUTTONS_YES_NO = int('0x3', 16)
    """
    specifies a message box with "YES" and "NO" button.
    """
    BUTTONS_YES_NO_CANCEL = int('0x4', 16)
    """
    specifies a message box with "YES", "NO" and "CANCEL" button.
    """
    DEFAULT_BUTTON_CANCEL = int('0x20000', 16)
    """
    specifies that CANCEL is the default button.
    """
    DEFAULT_BUTTON_IGNORE = int('0x60000', 16)
    """
    specifies that IGNORE is the default button.
    """
    DEFAULT_BUTTON_NO = int('0x50000', 16)
    """
    specifies that NO is the default button.
    """
    DEFAULT_BUTTON_OK = int('0x10000', 16)
    """
    specifies that OK is the default button.
    """
    DEFAULT_BUTTON_RETRY = int('0x30000', 16)
    """
    specifies that RETRY is the default button.
    """
    DEFAULT_BUTTON_YES = int('0x40000', 16)
    """
    specifies that YES is the default button.
    """
