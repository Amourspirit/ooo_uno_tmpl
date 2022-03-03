import pytest

def test_val_type_enum():
    from src.parser.enumerations.value_type import ValTypeEnum
    e = ValTypeEnum('INTEGER')
    assert e == ValTypeEnum.INTEGER