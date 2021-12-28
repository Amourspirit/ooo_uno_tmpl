# coding: utf-8
# this is a auto generated file generated by Cheetah
from ...base.const import ConstIntBase


class ImagePosition(ConstIntBase):
    """
    specifies the position of an image, relative to another object

    See Also:
        `API ImagePosition <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1ImagePosition.html>`_
    """
    AboveCenter = 7
    """
    specifies that the image should be positioned above and horizontally centered to the other object
    """
    AboveLeft = 6
    """
    specifies that the image should be positioned above and left-aligned to the other object
    """
    AboveRight = 8
    """
    specifies that the image should be positioned above and right-aligned to the other object
    """
    BelowCenter = 10
    """
    specifies that the image should be positioned below and horizontally centered to the other object
    """
    BelowLeft = 9
    """
    specifies that the image should be positioned below and left-aligned to the other object
    """
    BelowRight = 11
    """
    specifies that the image should be positioned below and right-aligned centered to the other object
    """
    Centered = 12
    """
    specifies that the image should be horizontally and vertically centered to the other object.
    """
    LeftBottom = 2
    """
    specifies that the image should be positioned at the left of, and bottom-aligned to, the other object
    """
    LeftCenter = 1
    """
    specifies that the image should be positioned at the left of, and vertically centered to, the other object
    """
    LeftTop = 0
    """
    specifies that the image should be positioned at the left of, and top-aligned to, the other object
    """
    RightBottom = 5
    """
    specifies that the image should be positioned at the right of, and bottom-aligned to, the other object
    """
    RightCenter = 4
    """
    specifies that the image should be positioned at the right of, and vertically centered to, the other object
    """
    RightTop = 3
    """
    specifies that the image should be positioned at the right of, and top-aligned to, the other object
    """
