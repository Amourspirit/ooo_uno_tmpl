
import pytest
if __name__ == "__main__":
    pytest.main([__file__])
import uno


def test_accessible_relation_type_const_meta():
    from ooo.helper.enum_helper import UnoConstMeta
    try:
        from com.sun.star.accessibility import AccessibleRelationType as UnoAccessibleRelationType
    except ImportError:
        pass

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

    class AccessibleRelationType(metaclass=UnoConstMeta, type_name=ns, name_space="com.sun.star.accessibility"):
        pass

    assert AccessibleRelationType.INVALID == UnoAccessibleRelationType.INVALID
    assert AccessibleRelationType.INVALID == UnoAccessibleRelationType.INVALID
    for value in values:
        const1 = getattr(AccessibleRelationType, value)
        const2 = getattr(UnoAccessibleRelationType, value)
        assert const1 == const2

def test_accessible_relation_type_const():
    from ooobuild.dyn.accessibility.accessible_relation_type import AccessibleRelationType
    try:
        from com.sun.star.accessibility import AccessibleRelationType as UnoAccessibleRelationType
    except ImportError:
        pass

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

    assert AccessibleRelationType.INVALID == UnoAccessibleRelationType.INVALID
    assert AccessibleRelationType.INVALID == UnoAccessibleRelationType.INVALID
    for value in values:
        const1 = getattr(AccessibleRelationType, value)
        const2 = getattr(UnoAccessibleRelationType, value)
        assert const1 == const2

def test_font_weight_const_enum():
    # just enum class, not IntEnum or FlagEnum
    from ooobuild.dyn.awt.font_weight import FontWeightEnum
    from com.sun.star.awt import FontWeight

    assert FontWeightEnum.BLACK.value == FontWeight.BLACK
    assert FontWeightEnum.BOLD.value == FontWeight.BOLD
    assert FontWeightEnum.DONTKNOW.value == FontWeight.DONTKNOW
    assert FontWeightEnum.LIGHT.value == FontWeight.LIGHT
    assert FontWeightEnum.NORMAL.value == FontWeight.NORMAL
    assert FontWeightEnum.SEMIBOLD.value == FontWeight.SEMIBOLD
    assert FontWeightEnum.SEMILIGHT.value == FontWeight.SEMILIGHT
    assert FontWeightEnum.THIN.value == FontWeight.THIN
    assert FontWeightEnum.ULTRABOLD.value == FontWeight.ULTRABOLD
    assert FontWeightEnum.ULTRALIGHT.value == FontWeight.ULTRALIGHT