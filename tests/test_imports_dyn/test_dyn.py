# coding: utf-8
import pytest
if __name__ == "__main__":
    # import os
    # import sys
    # sys.path.append(os.path.realpath('..'))
    pytest.main([__file__])

def test_dyn():
    from build.dyn.graphic.graphic_type import GraphicType
    from build.dyn.graphic.graphic_type import GraphicTypeEnum
    e = GraphicTypeEnum.VECTOR
    assert e.value == GraphicType.VECTOR
