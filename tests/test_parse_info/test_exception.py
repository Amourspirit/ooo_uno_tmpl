import pytest
from pathlib import Path
import json
if __name__ == "__main__":
    pytest.main([__file__])



@pytest.fixture(scope="session")
def fixture_exception(fixture_json_path: Path) -> Path:
    return fixture_json_path / 'exception' / 'Exception.json'




def test_exception(fixture_exception):
    from src.parse_info.ex.ooo_ex import OooException
    from src.parse_info.shared.ooo_type import OooType

    with open(fixture_exception, 'r') as f:
        f_json = json.load(f)
    obj = OooException(**f_json)
    assert obj is not None
    assert obj.id == 'uno-ooo-parser'
    assert obj.version == "0.1.21"
    assert obj.libre_office_ver == "7.2"
    assert obj.name == "Exception"
    assert obj.type == OooType.EXCEPTION
    assert obj.type == "exception"
    assert obj.namespace == "com.sun.star.uno"
    assert obj.parser_args.sort == True
    assert obj.parser_args.long_names == True
    assert obj.parser_args.remove_parent_inherited == True
    assert obj.writer_args.include_desc == True
    assert obj.data.allow_db == True
    assert obj.data.requires_typing == True
    assert obj.data.name == "Exception"
    assert obj.data.namespace == "com.sun.star.uno"
    assert obj.data.url == "https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1uno_1_1Exception.html"
    assert len(obj.data.from_imports) == 0
    assert len(obj.data.from_imports_typing) == 1
    imp = obj.data.from_imports_typing[0]
    assert imp.frm == ".x_interface"
    assert imp.imp == "XInterface"
    assert imp.az == "XInterface_8f010a43"
    assert len(obj.data.extends_map) == 0
    assert len(obj.data.quote) == 1
    assert obj.data.quote[0] == "XInterface_8f010a43"
    assert len(obj.data.typings) == 0
    assert len(obj.data.full_imports.general) == 0
    assert len(obj.data.full_imports.typing) == 1
    assert obj.data.full_imports.typing[0] == "com.sun.star.uno.XInterface"
    assert len(obj.data.imports) == 0
    assert len(obj.data.extends) == 1
    assert obj.data.extends[0] == "Exception"
    assert len(obj.data.desc) == 3
    assert obj.data.desc[0] == "the base of all UNO exceptions"
    assert obj.data.items.properties is not None
    p = obj.data.items.properties[0]
    assert p.name == "Context"
    assert p.returns == "XInterface_8f010a43"
    assert len(p.desc) == 3
    assert p.raises_get == ""
    assert p.raises_set == ""
    assert obj.data.items.methods is None
