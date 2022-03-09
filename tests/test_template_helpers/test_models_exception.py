import pytest
from pathlib import Path
if __name__ == "__main__":
    pytest.main([__file__])


def test_exception(root_path):
    from src.template_helper.models_exception import ModelsException
    p = 'lo/uno/Exception.json'
    mod = ModelsException(json_data=p)
    assert len(mod.parents) == 0
    args = mod.get_class_args()
    assert len(args) > 0
    arg = args[0]
    assert arg.name == "Message"
    assert arg.default == ""
    assert arg.type == "str"


def test_deployment_exception(root_path):
    from src.template_helper.models_exception import ModelsException
    p = 'lo/uno/DeploymentException.json'
    mod = ModelsException(json_data=p)
    assert len(mod.parents) > 0
    args = mod.get_class_args()
    assert len(args) == 0
    parent_args = mod.get_parents_class_args()
    assert len(parent_args) > 0
    

def test_authentication_failed_exception(root_path):
    from src.template_helper.models_exception import ModelsException
    p = Path(root_path, 'lo/configuration/backend/AuthenticationFailedException.json')
    mod = ModelsException(json_data=str(p))
    assert len(mod.parents) > 0
    args = mod.get_class_args()
    assert len(args) == 0
    parent_args = mod.get_parents_class_args()
    assert len(parent_args) == 3
    parg = parent_args[0]
    assert parg.name == "Message"
    assert parg.default == ""
    assert parg.type == "str"
    parg = parent_args[1]
    assert parg.name == "Context"
    assert parg.type == "XInterface_8f010a43"
    assert parg.default == "None"
    component = parg.component
    assert component is not None
    assert component.id_component == "com.sun.star.uno.XInterface"
    assert component.name == "XInterface"
    parg = parent_args[2]
    assert parg.name == "BackendException"
    assert parg.type == "object"
    assert parg.default == "None"
    # test cache
    parent_args = mod.get_parents_class_args()
    assert len(parent_args) == 3
    parg = parent_args[0]
    assert parg.name == "Message"
    assert parg.default == ""
    assert parg.type == "str"
    
    # test get_full_import()
    full = mod.get_full_imports()
    assert len(full) == 2
    assert str(
        full[1]) == "from ...uno.x_interface import XInterface as XInterface_8f010a43"
    tpl = ('...uno.x_interface', 'XInterface', 'XInterface_8f010a43')
    assert full[1].as_tuple() == tpl


def test_read_only_open_request(root_path):
    # this exception is LibreOffice Ver 7.2 +
    from src.template_helper.models_exception import ModelsException
    p = 'lo/document/ReadOnlyOpenRequest.json'
    mod = ModelsException(json_data=p)
    assert len(mod.parents) > 0
    args = mod.get_class_args()
    assert len(args) == 1
    parent_args = mod.get_parents_class_args()
    assert len(parent_args) > 0
