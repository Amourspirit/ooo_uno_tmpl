import pytest
from pathlib import Path
import json
if __name__ == "__main__":
    pytest.main([__file__])



@pytest.fixture(scope="session")
def fixture_uno_control_combo_box_model(fixture_json_path: Path) -> Path:
    return fixture_json_path / 'service' / 'UnoControlComboBoxModel.json'


@pytest.fixture(scope="session")
def fixture_read_only_access(fixture_json_path: Path) -> Path:
    return fixture_json_path / 'service' / 'ReadOnlyAccess.json'


def test_open_root(fixture_uno_control_combo_box_model):
    from src.parse_info.service.ooo_service import OooService
    from src.parse_info.shared.ooo_type import OooType
    from src.parse_info.shared.data.from_import import FromImport
    from src.parse_info.shared.data.properties.prop import Prop

    with open(fixture_uno_control_combo_box_model, 'r') as f:
        f_json = json.load(f)
    srv = OooService(**f_json)
    assert srv is not None
    assert srv.id == 'uno-ooo-parser'
    assert srv.version == "0.1.21"
    assert srv.libre_office_ver == "7.2"
    assert srv.name == "UnoControlComboBoxModel"
    assert srv.type == OooType.SERVICE
    assert srv.type == "service"
    assert srv.namespace == "com.sun.star.awt"
    assert srv.parser_args.sort == True
    assert srv.parser_args.long_names == True
    assert srv.parser_args.remove_parent_inherited == True
    assert srv.writer_args.include_desc == True
    assert srv.data.allow_db == True
    assert srv.data.requires_typing == True
    assert srv.data.name == "UnoControlComboBoxModel"
    assert srv.data.namespace == "com.sun.star.awt"
    assert srv.data.url == "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlComboBoxModel.html"
    assert len(srv.data.from_imports) == 2
    frm: FromImport = srv.data.from_imports[0]
    assert frm.frm == ".uno_control_model"
    assert frm.imp == "UnoControlModel"
    assert frm.az == "UnoControlModel_c8ce0c58"
    assert len(srv.data.from_imports_typing) == 2
    frm_typing: FromImport = srv.data.from_imports_typing[0]
    assert frm_typing.frm == ".font_descriptor"
    assert frm_typing.imp == "FontDescriptor"
    assert frm_typing.az == "FontDescriptor_bc110c0a"
    assert srv.data.extends_map["com.sun.star.awt.UnoControlModel"] == "UnoControlModel_c8ce0c58"
    assert srv.data.extends_map["com.sun.star.awt.XItemList"] == "XItemList_83fb09d7"
    assert len(srv.data.quote) == 4
    assert len(srv.data.typings) == 2
    assert len(srv.data.full_imports.general) == 2
    assert len(srv.data.full_imports.typing) == 2
    assert len(srv.data.imports) == 0
    assert len(srv.data.extends) == 2
    assert srv.data.extends[0] == "com.sun.star.awt.UnoControlModel"
    assert len(srv.data.desc) == 5
    assert srv.data.desc[0] == "specifies the standard model of a UnoControlComboBox."
    assert srv.data.items.properties is not None
    assert srv.data.items.methods is None
    assert len(srv.data.items.properties) == 23
    p: Prop = srv.data.items.properties[0]
    assert p.name == "Align"
    assert p.returns == 'int'
    assert p.raises_get == ""
    assert p.raises_set == ""
    assert len(p.desc) == 1


def test_read_only_access(fixture_read_only_access):
    from src.parse_info.service.ooo_service import OooService
    from src.parse_info.shared.ooo_type import OooType
    from src.parse_info.shared.data.from_import import FromImport
    from src.parse_info.shared.data.methods.method import Method
    from src.parse_info.shared.data.methods.method import ArgDirection

    with open(fixture_read_only_access, 'r') as f:
        f_json = json.load(f)
    srv = OooService(**f_json)
    assert srv is not None
    assert srv.id == 'uno-ooo-parser'
    assert srv.version == "0.1.21"
    assert srv.libre_office_ver == "7.2"
    assert srv.name == "ReadOnlyAccess"
    assert srv.type == OooType.SERVICE
    assert srv.type == "service"
    assert str(srv.type) == "service"
    assert srv.namespace == "com.sun.star.configuration"
    assert srv.parser_args.sort == True
    assert srv.parser_args.long_names == True
    assert srv.parser_args.remove_parent_inherited == True
    assert srv.writer_args.include_desc == True
    assert srv.data.allow_db == True
    assert srv.data.requires_typing == False
    assert srv.data.name == "ReadOnlyAccess"
    assert srv.data.namespace == "com.sun.star.configuration"
    assert srv.data.url == "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1ReadOnlyAccess.html"
    assert len(srv.data.from_imports) == 1
    frm: FromImport = srv.data.from_imports[0]
    assert frm.frm == "..container.x_hierarchical_name_access"
    assert frm.imp == "XHierarchicalNameAccess"
    assert frm.az == "XHierarchicalNameAccess_9e2611b5"
    assert len(srv.data.from_imports_typing) == 0
    assert srv.data.extends_map["com.sun.star.container.XHierarchicalNameAccess"] == "XHierarchicalNameAccess_9e2611b5"
    assert len(srv.data.quote) == 0
    assert len(srv.data.typings) == 0
    assert len(srv.data.full_imports.general) == 1
    assert len(srv.data.full_imports.typing) == 0
    assert len(srv.data.imports) == 0
    assert len(srv.data.extends) == 1
    assert srv.data.extends[0] == "com.sun.star.container.XHierarchicalNameAccess"
    assert len(srv.data.desc) == 7
    assert srv.data.desc[0] == "Provides easy read-only access to the complete configuration."
    assert srv.data.items.properties is None
    assert srv.data.items.methods is not None
    assert len(srv.data.items.methods) == 1
    m: Method = srv.data.items.methods[0]
    assert m.name == "create"
    assert m.returns == "None"
    assert len(m.raises) == 0
    assert len(m.args) == 1
    arg = m.args[0]
    assert arg.name == "locale"
    assert arg.type == "str"
    assert arg.direction == ArgDirection.IN
    assert arg.direction == 'in'
    assert str(arg.direction) == 'in'

def test_service_writer_args():
    from src.parse_info.shared.args.writer_args import WriterArgs
    data = {"include_desc": True}
    args = WriterArgs(**data)
    assert args.include_desc == True


def test_service_parser_args():
    from src.parse_info.shared.args.parser_args import ParserArgs
    data = {
        "sort": True,
        "long_names": True,
        "remove_parent_inherited" : True
        }
    args = ParserArgs(**data)
    assert args.sort == True
    assert args.long_names == True
    assert args.remove_parent_inherited == True
    args = ParserArgs(True, True, True)
    assert args.sort == True
    assert args.long_names == True
    assert args.remove_parent_inherited == True
