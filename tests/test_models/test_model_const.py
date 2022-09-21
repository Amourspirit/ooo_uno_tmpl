import pytest
from pathlib import Path
import json
if __name__ == "__main__":
    pytest.main([__file__])


@pytest.fixture(scope="session")
def fixture_accessible_event_id(fixture_json_path: Path) -> Path:
    return fixture_json_path / 'const' / 'AccessibleEventId.json'


def test_accessible_event_id(fixture_accessible_event_id: Path) -> Path:
    from src.model.constant.model_const import ModelConst
    from src.model.shared.ooo_type import OooType
    from src.parser.enumerations.value_type import ValTypeEnum

    with open(fixture_accessible_event_id, 'r') as f:
        f_json = json.load(f)
    obj = ModelConst(**f_json)
    assert obj is not None
    assert obj.id == 'uno-ooo-parser'
    assert obj.version == "0.1.23"
    assert obj.libre_office_ver == "7.2"
    assert obj.name == "AccessibleEventId"
    assert obj.type == OooType.CONST
    assert obj.type == "const"
    assert obj.namespace == "com.sun.star.accessibility"
    assert obj.parser_args.sort == False
    assert obj.parser_args.remove_parent_inherited == True
    assert obj.writer_args.hex == False
    assert obj.writer_args.flags == False
    assert obj.writer_args.include_desc == True
    assert obj.data.allow_db == True
    assert obj.data.requires_typing == False
    assert obj.data.name == "AccessibleEventId"
    assert obj.data.namespace == "com.sun.star.accessibility"
    assert obj.data.url == "https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1accessibility_1_1AccessibleEventId.html"
    assert obj.data.flags == False
    assert len(obj.data.from_imports) == 0
    assert len(obj.data.quote) == 0
    assert len(obj.data.typings) == 0
    assert len(obj.data.desc) == 7
    assert obj.data.desc[0] == "These constants identify the type of AccessibleEventObject objects."
    assert len(obj.data.items) == 41
    itm = obj.data.items[0]
    assert itm.name == 'NAME_CHANGED'
    assert itm.type == 'int'
    assert itm.value_type == ValTypeEnum.INTEGER
    assert itm.value == 1
