
import pytest
from enum import IntEnum

if __name__ == "__main__":
    pytest.main([__file__])


def test_accessible_relation_type_enum_meta():
    from ooo.helper.enum_helper import ConstEnumMeta
    ns = "com.sun.star.accessibility.AccessibleRelationType"
    # import uno
    values = (
        "INVALID",
        "CONTENT_FLOWS_FROM",
        "CONTENT_FLOWS_TO",
        "CONTROLLED_BY",
        "CONTROLLER_FOR",
        "LABEL_FOR",
        "LABELED_BY",
        "MEMBER_OF",
        "SUB_WINDOW_OF",
        "NODE_CHILD_OF",
        "DESCRIBED_BY",
    )

    class AccessibleRelationTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name=ns, name_space="com.sun.star.accessibility"):
        pass

    from ooobuild.dyn.accessibility.accessible_relation_type import AccessibleRelationType

    assert AccessibleRelationTypeEnum.INVALID.value == AccessibleRelationType.INVALID
    assert AccessibleRelationTypeEnum.INVALID.value == AccessibleRelationType.INVALID
    for value in values:
        const1 = getattr(AccessibleRelationTypeEnum, value)
        const2 = getattr(AccessibleRelationType, value)
        assert const1.value == const2


def test_accessible_relation_type_enum():
    from ooobuild.dyn.accessibility.accessible_relation_type import AccessibleRelationType
    from ooobuild.dyn.accessibility.accessible_relation_type import AccessibleRelationTypeEnum
    values = (
        "INVALID",
        "CONTENT_FLOWS_FROM",
        "CONTENT_FLOWS_TO",
        "CONTROLLED_BY",
        "CONTROLLER_FOR",
        "LABEL_FOR",
        "LABELED_BY",
        "MEMBER_OF",
        "SUB_WINDOW_OF",
        "NODE_CHILD_OF",
        "DESCRIBED_BY",
    )

    assert AccessibleRelationTypeEnum.INVALID.value == AccessibleRelationType.INVALID
    assert AccessibleRelationTypeEnum.INVALID.value == AccessibleRelationType.INVALID
    for value in values:
        const1 = getattr(AccessibleRelationTypeEnum, value)
        const2 = getattr(AccessibleRelationType, value)
        assert const1.value == const2


def test_message_box_results_int():
    from ooobuild.dyn.awt.message_box_results import MessageBoxResultsEnum
    result = MessageBoxResultsEnum(1)
    assert result.value == 1
    assert MessageBoxResultsEnum.OK == result


def test_message_box_results_str():
    from ooobuild.dyn.awt.message_box_results import MessageBoxResultsEnum
    assert MessageBoxResultsEnum.OK.value == 1
    result = MessageBoxResultsEnum("OK")
    assert result.value == 1
    assert result == MessageBoxResultsEnum.OK


def test_message_box_results_enum():
    from ooobuild.dyn.awt.message_box_results import MessageBoxResultsEnum
    result = MessageBoxResultsEnum(MessageBoxResultsEnum.OK)
    assert result.value == 1
    assert result == MessageBoxResultsEnum.OK


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


def test_cell_flags() -> None:
    from ooobuild.dyn.sheet.cell_flags import CellFlagsEnum
    flags = CellFlagsEnum.VALUE | CellFlagsEnum.STRING
    new_flags = CellFlagsEnum(flags)
    assert new_flags == flags
    new_flags = CellFlagsEnum(flags.value)
    assert new_flags == flags
