import pytest
from pathlib import Path
import json
if __name__ == "__main__":
    pytest.main([__file__])


@pytest.fixture(scope="session")
def fixture_adjustment_event(fixture_json_path: Path) -> Path:
    return fixture_json_path / 'struct' / 'AdjustmentEvent.json'


def test_adjustment_event(fixture_adjustment_event):
    from src.model.struct.model_struct import ModelStruct
    from src.model.shared.ooo_type import OooType

    with open(fixture_adjustment_event, 'r') as f:
        f_json = json.load(f)
    obj = ModelStruct(**f_json)
    assert obj is not None
    assert obj.id == 'uno-ooo-parser'
    assert obj.version == "0.1.21"
    assert obj.libre_office_ver == "7.2"
    assert obj.name == "AdjustmentEvent"
    assert obj.type == OooType.STRUCT
    assert obj.type == "struct"
    assert obj.namespace == "com.sun.star.awt"
    assert obj.parser_args.sort == False
    assert obj.parser_args.long_names == True
    assert obj.parser_args.remove_parent_inherited == True
    assert obj.writer_args.sort == True
    assert obj.writer_args.dynamic_struct == True
    assert obj.writer_args.include_desc == True
    assert obj.data.allow_db == True
    assert obj.data.requires_typing == True
    assert obj.data.name == "AdjustmentEvent"
    assert obj.data.namespace == "com.sun.star.awt"
    assert obj.data.url == "https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1AdjustmentEvent.html"
    assert len(obj.data.from_imports) == 1
    imp = obj.data.from_imports[0]
    assert imp.frm == "..lang.event_object"
    assert imp.imp == "EventObject"
    assert imp.az == "EventObject_a3d70b03"
    assert len(obj.data.from_imports_typing) == 1
    imp = obj.data.from_imports_typing[0]
    assert imp.frm == ".adjustment_type"
    assert imp.imp == "AdjustmentType"
    assert imp.az == "AdjustmentType_bd050c15"
    assert len(obj.data.extends_map) == 1
    assert obj.data.extends_map['com.sun.star.lang.EventObject'] == "EventObject_a3d70b03"
    assert len(obj.data.quote) == 1
    assert len(obj.data.typings) == 0
    assert len(obj.data.imports) == 0
    assert len(obj.data.extends) == 1
    assert obj.data.extends[0] == "com.sun.star.lang.EventObject"
    assert len(obj.data.desc) == 1
    assert obj.data.desc[0] == "adjustment event emitted by adjustable objects."
    assert obj.data.items.properties is not None
    p = obj.data.items.properties[0]
    assert p.name == "Value"
    assert p.returns == "int"
    assert p.desc[0] == "contains the current value in the adjustment event."
    assert obj.data.items.types is None
    assert obj.data.items.methods is None
