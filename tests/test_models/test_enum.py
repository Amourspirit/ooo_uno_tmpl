import pytest
from pathlib import Path
import json
if __name__ == "__main__":
    pytest.main([__file__])


@pytest.fixture(scope="session")
def fixture_adjustment_type(fixture_json_path: Path) -> Path:
    return fixture_json_path / 'enum' / 'AdjustmentType.json'


def test_adjustment_type(fixture_adjustment_type):
    from src.model.enumeration.model_enum import ModelEnum
    from src.model.shared.ooo_type import OooType

    with open(fixture_adjustment_type, 'r') as f:
        f_json = json.load(f)
    obj = ModelEnum(**f_json)
    assert obj is not None
    assert obj.id == 'uno-ooo-parser'
    assert obj.version == "0.1.23"
    assert obj.libre_office_ver == "7.2"
    assert obj.name == "AdjustmentType"
    assert obj.type == OooType.ENUM
    assert obj.type == "enum"
    assert obj.namespace == "com.sun.star.awt"
    assert obj.parser_args.sort == True
    assert obj.writer_args.include_desc == True
    assert obj.data.allow_db == True
    assert obj.data.name == "AdjustmentType"
    assert obj.data.namespace == "com.sun.star.awt"
    assert obj.data.url == "https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#ae54d0c7f4237b639c3f45caa306457fd"
    assert len(obj.data.quote) == 0
    assert len(obj.data.typings) == 0
    assert obj.data.desc == ""
    assert len(obj.data.items) == 3
    itm = obj.data.items[0]
    assert itm.name == "ADJUST_ABS"
    assert itm.value == "ADJUST_ABS"
    assert itm.desc[0] == "adjustment is originated by dragging the thumb."
