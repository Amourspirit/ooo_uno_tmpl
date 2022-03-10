import pytest
from pathlib import Path
import json
if __name__ == "__main__":
    pytest.main([__file__])



@pytest.fixture(scope="session")
def fixture_the_introspection(fixture_json_path: Path) -> Path:
    return fixture_json_path / 'singleton' / 'theIntrospection.json'


def test_the_introspection(fixture_the_introspection):
    from src.model.singleton.model_singleton import ModelSingleton
    from src.model.shared.ooo_type import OooType

    with open(fixture_the_introspection, 'r') as f:
        f_json = json.load(f)
    obj = ModelSingleton(**f_json)
    assert obj is not None
    assert obj.id == 'uno-ooo-parser'
    assert obj.version == "0.1.21"
    assert obj.libre_office_ver == "7.2"
    assert obj.name == "theIntrospection"
    assert obj.type == OooType.SINGLETON
    assert obj.type == "singleton"
    assert obj.namespace == "com.sun.star.beans"
    assert obj.parser_args.sort == True
    assert obj.parser_args.long_names == True
    assert obj.parser_args.remove_parent_inherited == True
    assert obj.writer_args.include_desc == True
    assert obj.data.allow_db == True
    assert obj.data.requires_typing == False
    assert obj.data.name == "theIntrospection"
    assert obj.data.namespace == "com.sun.star.beans"
    assert obj.data.url == "https://api.libreoffice.org/docs/idl/ref/singletoncom_1_1sun_1_1star_1_1beans_1_1theIntrospection.html"
    assert len(obj.data.from_imports) == 1
    imp = obj.data.from_imports[0]
    assert imp.frm == ".x_introspection"
    assert imp.imp == "XIntrospection"
    assert imp.az == "XIntrospection_d5510cda"
    assert len(obj.data.from_imports_typing) == 0
    assert len(obj.data.extends_map) == 1
    assert obj.data.extends_map['com.sun.star.beans.XIntrospection'] == "XIntrospection_d5510cda"
    assert len(obj.data.quote) == 0
    assert len(obj.data.typings) == 0
    assert len(obj.data.full_imports.general) == 1
    assert obj.data.full_imports.general[0] == "com.sun.star.beans.XIntrospection"
    assert len(obj.data.full_imports.typing) == 0
    assert len(obj.data.imports) == 0
    assert len(obj.data.extends) == 1
    assert obj.data.extends[0] == "com.sun.star.beans.XIntrospection"
    assert len(obj.data.desc) == 9
    assert obj.data.desc[0] == "provides functionality to get information about an object's properties and methods."
    assert obj.data.items.properties is None
    assert obj.data.items.types is None
    assert obj.data.items.methods is None
