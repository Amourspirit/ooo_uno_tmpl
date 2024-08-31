import pytest
if __name__ == "__main__":
    pytest.main([__file__])

from enum import IntFlag
import uno


def test_adjustment_type():
    # test dynamic AdjustmentType class.
    # all dynamic enums ar classes that use enum_helper.UnoEnumMeta as a meta class
    from ooobuild.dyn.awt.adjustment_type import AdjustmentType
    from com.sun.star.awt.AdjustmentType import (
        ADJUST_ABS, ADJUST_LINE, ADJUST_PAGE)

    assert AdjustmentType.__ooo_ns__ == "com.sun.star.awt"
    assert AdjustmentType.__ooo_full_ns__ == "com.sun.star.awt.AdjustmentType"
    assert AdjustmentType.__ooo_type_name__ == "enum"
    assert AdjustmentType.typeName == "com.sun.star.awt.AdjustmentType"

    assert AdjustmentType.ADJUST_ABS == ADJUST_ABS
    assert AdjustmentType.ADJUST_ABS == ADJUST_ABS

    assert AdjustmentType.ADJUST_LINE == ADJUST_LINE
    atype = AdjustmentType("ADJUST_PAGE")
    assert atype == ADJUST_PAGE

    atype = AdjustmentType(ADJUST_LINE)
    assert atype == ADJUST_LINE

    with pytest.raises(TypeError):
        AdjustmentType(10)

    with pytest.raises(TypeError):
        AdjustmentType("ADJUST")



def test_font_slant():
    from ooo.helper.enum_helper import UnoEnumMeta
    class FontSlant(metaclass=UnoEnumMeta, type_name="com.sun.star.awt.FontSlant", name_space="com.sun.star.awt"):
        """Dynamically created class that represents ``com.sun.star.awt.FontSlant`` Enum. Class loosely mimics Enum"""
        pass
    
    fs = FontSlant.ITALIC
    assert fs.value == "ITALIC"

