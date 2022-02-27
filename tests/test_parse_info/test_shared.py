import pytest
from pathlib import Path

from src.parse_info.shared.data.methods.method import ArgDirection

if __name__ == "__main__":
    pytest.main([__file__])

def test_method_raises():
    from src.parse_info.shared.data.methods.raises import MethodRaises
    raises = MethodRaises("long_error", "short_error")
    assert raises.long == "long_error"
    assert raises.short == "short_error"
    

def test_method():
    from src.parse_info.shared.data.methods.method import Method
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
    assert meth.raises.is_valid() == False
