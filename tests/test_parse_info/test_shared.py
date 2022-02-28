import pytest
from pydantic import ValidationError

if __name__ == "__main__":
    pytest.main([__file__])



def test_method_arg():
    from src.parse_info.shared.data.methods.method import ArgDirection
    d = ArgDirection.IN
    assert str(d) == 'in'
    d = ArgDirection('in')
    assert str(d) == 'in'

    d = ArgDirection('out')
    assert str(d) == 'out'

def test_method_raises():
    from src.parse_info.shared.data.methods.raises import MethodRaises
    raises = MethodRaises("long_error", "short_error")
    assert raises.long == "long_error"
    assert raises.short == "short_error"
    

def test_method():
    from src.parse_info.shared.data.methods.method import Method
    from src.parse_info.shared.data.methods.method import ArgDirection
    data = {
        "name": "createWithModel",
        "returns": "None",
        "desc": [],
        "raises": [],
        "args": [
        [
            "Model",
            "XModel_7a6e095c",
            "in"
        ]
        ]
    }
    meth = Method(**data)
    assert meth.name == "createWithModel"
    assert meth.returns == "None"
    assert len(meth.args) == 1
    arg = meth.args[0]
    assert arg.name== "Model"
    assert arg.type == "XModel_7a6e095c"
    assert arg.direction == ArgDirection.IN
    assert arg.direction == 'in'
    assert str(arg.direction) == 'in'

def test_prop():
    from src.parse_info.shared.data.properties.prop import Prop
    data = {
        "name": "Xray",
        "returns": "Yray",
        "desc": ["ray vision.", "night vision"]
    }
    p1 = Prop(**data)
    assert p1.name == "Xray"
    assert p1.returns == "Yray"
    assert len(p1.desc) == 2
    p2 = Prop(
        name="Xray",
        returns="Yray",
        desc=["ray vision.", "night vision"]
    )
    assert p2.name == "Xray"
    assert p2.returns == "Yray"
    p3 = Prop(**p2.dict())
    assert p3.name == "Xray"
    assert p3.returns == "Yray"
    with pytest.raises(ValidationError):
        _ = Prop(
            name=" ",
            returns="Yray",
            desc=["ray vision.", "night vision"]
        )
    with pytest.raises(ValidationError):
        _ = Prop(
            name="XRay",
            returns="",
            desc=["ray vision.", "night vision"]
        )

def test_from_import():
    from src.parse_info.shared.data.from_import import FromImport
    data = {
        "frm": "..uno",
        "imp": "XInterface",
        "az": "XInterface_abc"
    }
    f1 = FromImport(**data)
    assert f1.frm == "..uno"
    assert f1.imp == "XInterface"
    assert f1.az == "XInterface_abc"
    data2 = ("..uno", "XInterface", "XInterface_abc")
    f2 = FromImport(*data2)
    assert f1.frm == f2.frm
    assert f1.imp == f2.imp
    assert f1.az == f2.az
    assert str(f2) == "from ..uno import XInterface as XInterface_abc"
    data3 = ("..uno", "XInterface")
    f3 = FromImport(*data3)
    assert f1.frm == f3.frm
    assert f1.imp == f3.imp
    assert f3.az == None
    assert str(f3) == "from ..uno import XInterface"



def test_base_data():
    from src.parse_info.shared.data.shared_data import BaseData
    data = {
        "name": "AnimateColor",
        "namespace": "com.sun.star.animations",
        "allow_db": True,
        "url": "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1animations_1_1AnimateColor.html",
        "desc": [
            "",
            "**since**",
            "",
            "    LibreOffice 4.1"
        ]
    }
    b = BaseData(**data)
    assert b.allow_db == True
    assert b.name == "AnimateColor"
    assert b.namespace == "com.sun.star.animations"
    assert b.url == data['url']
    assert len(b.desc) == 4
    assert b.desc[1] == data['desc'][1]

    data2 = data.copy()
    
    with pytest.raises(ValidationError):
        data2['namespace'] = "com_sun.star.animations"
        _ = BaseData(**data2)

    data3 = data.copy()
    with pytest.raises(ValidationError):
        data3['name'] = ' '
        _ = BaseData(**data3)
    
    data4 = data.copy()
    with pytest.raises(ValidationError):
        data4['url'] = ''
        _ = BaseData(**data4)

def test_ooo_class():
    from src.parse_info.shared.ooo_class import OooClass
    from src.parse_info.shared.ooo_type import OooType
    from verr import Version
    data = {
        "id": "uno-ooo-parser",
        "version": "0.1.21",
        "libre_office_ver": "7.2",
        "name": "AnimateColor",
        "type": "service",
        "namespace": "com.sun.star.animations"
        }
    ver = Version.parse(data['version'])
    oc = OooClass(**data)
    assert oc.id == data['id']
    assert oc.ver == ver
    assert oc.type == OooType.SERVICE
    assert oc.type == data['type']
    assert str(oc.type) == data['type']
    