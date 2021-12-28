# coding: utf-8
# this is a auto generated file generated by Cheetah
from ...base.const import ConstIntBase


class LineEndFormat(ConstIntBase):
    """
    specifies that line ends are to be represented by a carriage return character (\\r)

    See Also:
        `API LineEndFormat <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1LineEndFormat.html>`_
    """
    CARRIAGE_RETURN = 0
    """
    specifies that line ends are to be represented by a carriage return character (\\r)
    """
    CARRIAGE_RETURN_LINE_FEED = 2
    """
    specifies that line ends are to be represented by a line feed character (\\n), followed by a carriage return character (\\r).
    """
    LINE_FEED = 1
    """
    specifies that line ends are to be represented by a line feed character (\\n)
    """
