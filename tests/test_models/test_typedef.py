import pytest
from pathlib import Path
import json
if __name__ == "__main__":
    pytest.main([__file__])


@pytest.fixture(scope="session")
def fixture_property_values(fixture_json_path: Path) -> Path:
    return fixture_json_path / 'typedef' / 'PropertyValues.json'


def test_property_values(fixture_property_values):
    from src.model.typedef.model_typedef import ModelTypedef
    from src.model.shared.ooo_type import OooType

    with open(fixture_property_values, 'r') as f:
        f_json = json.load(f)
    obj = ModelTypedef(**f_json)
    assert obj is not None
    assert obj.id == 'uno-ooo-parser'
    assert obj.version == "0.1.23"
    assert obj.libre_office_ver == "7.2"
    assert obj.name == "PropertyValues"
    assert obj.type == OooType.TYPEDEF
    assert obj.type == "typedef"
    assert obj.namespace == "com.sun.star.beans"
    assert obj.parser_args.sort == True
    assert obj.data.allow_db == True
    assert obj.data.requires_typing == True
    assert obj.data.name == "PropertyValues"
    assert obj.data.namespace == "com.sun.star.beans"
    assert obj.data.url == "https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1beans.html#aaf9e99eca0c81d619c590bd13fc27ca2"
    assert len(obj.data.from_imports) == 1
    imp = obj.data.from_imports[0]
    assert imp.frm == ".property_value"
    assert imp.imp == "PropertyValue"
    assert imp.az == None
    assert len(obj.data.quote) == 1
    assert obj.data.quote[0] == "typing.Tuple[PropertyValue, ...]"
    assert len(obj.data.typings) == 1
    assert obj.data.typings[0] == "typing.Tuple[PropertyValue, ...]"
    assert len(obj.data.imports) == 1
    assert obj.data.imports[0] == "PropertyValue"
    assert len(obj.data.desc) == 3
    assert obj.data.desc[0] == "specifies a sequence of PropertyValue instances."
