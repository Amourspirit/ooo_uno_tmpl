import pytest
from pathlib import Path
import json
if __name__ == "__main__":
    pytest.main([__file__])


@pytest.fixture(scope="session")
def fixture_module_links(fixture_json_path: Path) -> Path:
    return fixture_json_path / 'module_links' / 'module_links.json'



def test_open_root(fixture_module_links):
    from src.model.links.model_module_links import ModelModuleLinks
    from src.model.shared.ooo_type import OooType

    with open(fixture_module_links, 'r') as f:
        f_json = json.load(f)
    obj = ModelModuleLinks(**f_json)
    assert obj.id == 'uno-ooo-parser'
    assert obj.version == "0.1.19"
    assert obj.libre_office_ver == "7.2"
    assert obj.name == "com.sun.star.awt"
    assert obj.namespace == "com.sun.star.awt"
    assert obj.type == OooType.MODULE_LINKS
    assert obj.type == "module_links"
    assert obj.url_base == "https://api.libreoffice.org/docs/idl/ref"
    assert len(obj.data.modules) == 3
    assert len(obj.data.enums) == 8
    itm = obj.data.enums[0]
    assert itm.name == "AdjustmentType"
    assert itm.href == "namespacecom_1_1sun_1_1star_1_1awt.html#ae54d0c7f4237b639c3f45caa306457fd"
    assert len(obj.data.constants) == 39
    itm = obj.data.constants[0]
    assert itm.name == "CharSet"
    assert itm.href == "namespacecom_1_1sun_1_1star_1_1awt_1_1CharSet.html"
    assert len(obj.data.typedef) == 0
    assert len(obj.data.classes.service) == 100
    itm = obj.data.classes.service[0]
    assert itm.name == "AccessibleButton"
    assert itm.href == "servicecom_1_1sun_1_1star_1_1awt_1_1AccessibleButton.html"
    assert len(obj.data.classes.struct) == 30
    itm = obj.data.classes.struct[0]
    assert itm.name == "ActionEvent"
    assert itm.href == "structcom_1_1sun_1_1star_1_1awt_1_1ActionEvent.html"
    assert len(obj.data.classes.exception) == 1
    itm = obj.data.classes.exception[0]
    assert itm.name == "PrinterException"
    assert itm.href == "exceptioncom_1_1sun_1_1star_1_1awt_1_1PrinterException.html"
    assert len(obj.data.classes.interface) == 118
    itm = obj.data.classes.interface[0]
    assert itm.name == "XActionListener"
    assert itm.href == "interfacecom_1_1sun_1_1star_1_1awt_1_1XActionListener.html"
