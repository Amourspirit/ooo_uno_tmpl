# coding: utf-8
# this is a auto generated file generated by Cheetah
from ...base.const import ConstIntFlagsBase


class ImageDrawMode(ConstIntFlagsBase):
    """
    defines modes how an image is drawn onto a device
    
    **Since**
    
       LibreOffice 4.1

    See Also:
        `API ImageDrawMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1ImageDrawMode.html>`_
    """
    DEACTIVE = int('0x0004', 16)
    """
    the image is drawn as being deactivated.
    """
    DISABLE = int('0x0001', 16)
    """
    the image is drawn as if it represented a feature whose state is disabled.
    """
    HIGHLIGHT = int('0x0002', 16)
    """
    the image is drawn as being highlighted.
    """
    NONE = int('0x0000', 16)
    """
    the image is drawn as is, without any color transformation.
    """
    SEMITRANSPARENT = int('0x0010', 16)
    """
    the image is drawn semi-transparent.
    """
