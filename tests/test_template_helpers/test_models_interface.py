import pytest
import json
from pathlib import Path
if __name__ == "__main__":
    pytest.main([__file__])


def test_x_animate(root_path):
    from src.template_helper.models_interface import ModelsInterface
    p = 'lo/animations/XAnimate.json'
    mod = ModelsInterface(json_data=p)
    assert len(mod.parents) == 1
    args = mod.get_class_args()
    assert len(args) > 0
    arg = args[0]
    assert arg.name == "Values"
    assert arg.default == "None"
    assert arg.type == "typing.Tuple[object, ...]"
    assert arg.p_type.origin == "sequence< any >"
    full_imp = [x.as_tuple()
                for x in mod.get_full_imports()]
    assert len(full_imp) > 0


def test_x_animate_json(root_path):
    from src.template_helper.models_interface import ModelsInterface
    p = 'lo/animations/XAnimate.json'
    pj = Path(root_path, p)
    with open(pj) as file:
        jdata =json.load(file)
    mod = ModelsInterface(json_data=jdata)
    assert len(mod.parents) == 1
    args = mod.get_class_args()
    assert len(args) > 0
    arg = args[0]
    assert arg.name == "Values"
    assert arg.default == "None"
    assert arg.type == "typing.Tuple[object, ...]"
    assert arg.p_type.origin == "sequence< any >"

def test_x_child(root_path):
    from src.template_helper.models_interface import ModelsInterface
    p = 'lo/container/XChild.json'
    mod = ModelsInterface(json_data=p)
    assert len(mod.parents) == 1
    args = mod.get_class_args()
    assert len(args) == 0