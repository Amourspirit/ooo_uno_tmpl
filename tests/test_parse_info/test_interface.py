import pytest
from pathlib import Path
import json
if __name__ == "__main__":
    pytest.main([__file__])



@pytest.fixture(scope="session")
def fixture_xinterface(fixture_json_path: Path) -> Path:
    return fixture_json_path / 'interface' / 'XInterface.json'


@pytest.fixture(scope="session")
def fixture_xstyle_settings(fixture_json_path: Path) -> Path:
    return fixture_json_path / 'interface' / 'XStyleSettings.json'

def test_open_root(fixture_xinterface):
    from src.parse_info.interface.ooo_interface import OooInterface
    from src.parse_info.shared.ooo_type import OooType
    from src.parse_info.shared.data.methods.method import ArgDirection
    from src.parse_info.shared.data.methods.method import Method

    with open(fixture_xinterface, 'r') as f:
        f_json = json.load(f)
    obj = OooInterface(**f_json)
    assert obj is not None
    assert obj.id == 'uno-ooo-parser'
    assert obj.version == "0.1.21"
    assert obj.libre_office_ver == "7.2"
    assert obj.name == "XInterface"
    assert obj.type == OooType.INTERFACE
    assert obj.type == "interface"
    assert obj.namespace == "com.sun.star.uno"
    assert obj.parser_args.sort == True
    assert obj.parser_args.long_names == True
    assert obj.parser_args.remove_parent_inherited == True
    assert obj.writer_args.include_desc == True
    assert obj.data.allow_db == True
    assert obj.data.requires_typing == False
    assert obj.data.name == "XInterface"
    assert obj.data.namespace == "com.sun.star.uno"
    assert obj.data.url == "https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface.html"
    assert len(obj.data.from_imports) == 0
    assert len(obj.data.from_imports_typing) == 0
    assert len(obj.data.extends_map) == 0
    assert len(obj.data.quote) == 0
    assert len(obj.data.typings) == 0
    assert len(obj.data.full_imports.general) == 0
    assert len(obj.data.full_imports.typing) == 0
    assert len(obj.data.imports) == 0
    assert len(obj.data.extends) == 0
    assert len(obj.data.desc) == 11
    assert obj.data.desc[0] == "base interface of all UNO interfaces"
    assert obj.data.items.properties is None
    assert obj.data.items.methods is not None
    assert len(obj.data.items.methods) == 3
    m: Method = obj.data.items.methods[1]
    assert m.name == "queryInterface"
    assert m.returns == "object"
    assert len(m.raises) == 0
    assert len(m.args) == 1
    arg = m.args[0]
    assert arg.name == "aType"
    assert arg.type == "object"
    assert arg.direction == ArgDirection.IN
    assert arg.direction == 'in'
    assert str(arg.direction) == 'in'


def test_xstyle_settings(fixture_xstyle_settings):
    from src.parse_info.interface.ooo_interface import OooInterface
    from src.parse_info.shared.ooo_type import OooType
    from src.parse_info.shared.data.from_import import FromImport
    from src.parse_info.shared.data.methods.method import Method
    from src.parse_info.shared.data.properties.prop import Prop
    from src.parse_info.shared.data.methods.method import ArgDirection

    with open(fixture_xstyle_settings, 'r') as f:
        f_json = json.load(f)
    obj = OooInterface(**f_json)
    assert obj is not None
    assert obj.id == 'uno-ooo-parser'
    assert obj.version == "0.1.21"
    assert obj.libre_office_ver == "7.2"
    assert obj.name == "XStyleSettings"
    assert obj.type == OooType.INTERFACE
    assert obj.type == "interface"
    assert str(obj.type) == "interface"
    assert obj.namespace == "com.sun.star.awt"
    assert obj.parser_args.sort == True
    assert obj.parser_args.long_names == True
    assert obj.parser_args.remove_parent_inherited == True
    assert obj.writer_args.include_desc == True
    assert obj.data.allow_db == True
    assert obj.data.requires_typing == True
    assert obj.data.name == "XStyleSettings"
    assert obj.data.namespace == "com.sun.star.awt"
    assert obj.data.url == "https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XStyleSettings.html"
    assert len(obj.data.from_imports) == 0
    assert len(obj.data.from_imports_typing) == 3
    frm: FromImport = obj.data.from_imports_typing[0]
    assert frm.frm == ".font_descriptor"
    assert frm.imp == "FontDescriptor"
    assert frm.az == "FontDescriptor_bc110c0a"
    assert len(obj.data.extends_map) == 0
    assert len(obj.data.quote) == 3
    assert len(obj.data.typings) == 0
    assert len(obj.data.full_imports.general) == 0
    assert len(obj.data.full_imports.typing) == 3
    assert len(obj.data.imports) == 0
    assert len(obj.data.extends) == 0
    assert len(obj.data.desc) == 5
    assert obj.data.desc[0] == "provides access to certain style settings within an OpenOffice.org component, such as a window, or within OpenOffice.org as a whole."
    assert obj.data.items.properties is not None
    assert obj.data.items.methods is not None
    assert len(obj.data.items.properties) == 53
    p: Prop = obj.data.items.properties[0]
    assert p.name == "ActiveBorderColor"
    assert p.returns == 'Color_68e908c5'
    assert p.raises_get == ""
    assert p.raises_set == ""
    assert p.desc[0] == "specifies the color of the border of active windows"
    assert len(obj.data.items.methods) == 2
    m: Method = obj.data.items.methods[0]
    assert m.name == "addStyleChangeListener"
    assert m.returns == "None"
    assert m.desc[0] == "registers a listener to be notified when the style settings change"
    assert len(m.raises) == 0
    assert len(m.args) == 1
    arg = m.args[0]
    assert arg.name == "Listener"
    assert arg.type == "XStyleChangeListener_ad50e49"
    assert arg.direction == ArgDirection.IN
    assert arg.direction == 'in'
    assert str(arg.direction) == 'in'
