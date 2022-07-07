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


def test_focus_change_reason():
    # FocusChangeReason is Flags Enum
    from ooobuild.dyn.awt.focus_change_reason import FocusChangeReason
    from ooobuild.dyn.awt.focus_change_reason import FocusChangeReasonEnum
    assert FocusChangeReason.__ooo_ns__ == 'com.sun.star.awt'
    assert FocusChangeReason.__ooo_full_ns__ == 'com.sun.star.awt.FocusChangeReason'
    assert FocusChangeReason.__ooo_type_name__ == 'const'
    e = FocusChangeReasonEnum.AROUND | FocusChangeReasonEnum.CURSOR
    assert FocusChangeReasonEnum.AROUND & e == FocusChangeReasonEnum.AROUND
    assert FocusChangeReasonEnum.CURSOR & e == FocusChangeReasonEnum.CURSOR

def test_simple_flags() -> None:
    class Simple(IntFlag):
        VALUE = 1
        DATETIME = 2
        STRING = 4
    
    flags = Simple.VALUE | Simple.STRING
    new_flags = Simple(flags)
    assert new_flags == flags

def test_cell_flags() -> None:
    from ooobuild.dyn.sheet.cell_flags import CellFlagsEnum
    flags = CellFlagsEnum.VALUE | CellFlagsEnum.STRING
    new_flags = CellFlagsEnum(flags)
    assert new_flags == flags
