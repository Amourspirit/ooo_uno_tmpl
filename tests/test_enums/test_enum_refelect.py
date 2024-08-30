import pytest
if __name__ == "__main__":
    pytest.main([__file__])

from enum import IntFlag
import uno


def test_refelect_adjustment_type():
    # from ooo.helper.enums.enum_type_description_comp import EnumTypeDescriptionComp
    from ooo.helper.enums.enum_helper import EnumHelper

    type_name = "com.sun.star.awt.AdjustmentType"

    name_space, enum_name = type_name.rsplit(sep=".", maxsplit=1)

    info = EnumHelper.get_enum_info(type_name)
    assert info
    AdjustmentType =info.create_dynamic_enum(enum_name)
    assert AdjustmentType
    AdjustmentType.__module__ = type_name
    AdjustmentType.typeName = type_name
    AdjustmentType.__ooo_type_name__ = "enum"
    AdjustmentType.__ooo_full_ns__ = type_name
    AdjustmentType.__ooo_ns__ = name_space
    AdjustmentType.__ooo_enum_name__ = enum_name

    assert AdjustmentType.__ooo_ns__ == "com.sun.star.awt"
    assert AdjustmentType.__ooo_full_ns__ == "com.sun.star.awt.AdjustmentType"
    assert AdjustmentType.__ooo_type_name__ == "enum"
    assert AdjustmentType.__ooo_enum_name__ == "AdjustmentType"
    assert AdjustmentType.typeName == "com.sun.star.awt.AdjustmentType"


def test_enum_gen_dynamic_enum():
    from ooo.helper import enum_helper

    type_name = "com.sun.star.awt.AdjustmentType"

    AdjustmentType = enum_helper.gen_dynamic_enum(type_name)
    assert AdjustmentType.__ooo_ns__ == "com.sun.star.awt"
    assert AdjustmentType.__ooo_full_ns__ == "com.sun.star.awt.AdjustmentType"
    assert AdjustmentType.__ooo_type_name__ == "enum"
    assert AdjustmentType.__ooo_enum_name__ == "AdjustmentType"
    assert AdjustmentType.typeName == "com.sun.star.awt.AdjustmentType"

    assert AdjustmentType.ADJUST_LINE.value == "ADJUST_LINE"
    assert AdjustmentType.ADJUST_PAGE.value == "ADJUST_PAGE"
    assert AdjustmentType.ADJUST_ABS.value == "ADJUST_ABS"

    e = AdjustmentType.ADJUST_LINE
    assert e.name == "ADJUST_LINE"
    assert e.value == "ADJUST_LINE"

    e = AdjustmentType("ADJUST_PAGE")
    assert e.name == "ADJUST_PAGE"
    assert e.value == "ADJUST_PAGE"

    e = AdjustmentType(AdjustmentType.ADJUST_LINE)
    assert e.name == "ADJUST_LINE"
    assert e.value == "ADJUST_LINE"

    e = AdjustmentType(AdjustmentType.ADJUST_LINE.value)
    assert e.name == "ADJUST_LINE"
    assert e.value == "ADJUST_LINE"
