
import pytest
from enum import Enum, IntEnum
if __name__ == "__main__":
    pytest.main([__file__])

import uno


def test_accessible_relation_type_enum_meta():
    from ooo.helper.enum_helper import ConstEnumMeta
    ns = "com.sun.star.accessibility.AccessibleRelationType"
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