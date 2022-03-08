import pytest

if __name__ == "__main__":
    pytest.main([__file__])


def test_exception(root_path):
    from src.template_helper.models_exception import ModelExceptions
    p = 'lo/uno/Exception.json'
    mod = ModelExceptions(json_data_file=p)
    assert len(mod.parents) == 0
    args = mod.get_class_args()
    assert len(args) > 0
    arg = args[0]
    assert arg.name == "Message"
    assert arg.default == ""
    assert arg.type == "str"


def test_deployment_exception(root_path):
    from src.template_helper.models_exception import ModelExceptions
    p = 'lo/uno/DeploymentException.json'
    mod = ModelExceptions(json_data_file=p)
    assert len(mod.parents) > 0
    args = mod.get_class_args()
    assert len(args) == 0
    parent_args = mod.get_parents_class_args()
    assert len(parent_args) > 0
    

def test_authentication_failed_exception(root_path):
    from src.template_helper.models_exception import ModelExceptions
    p = 'lo/configuration/backend/AuthenticationFailedException.json'
    mod = ModelExceptions(json_data_file=p)
    assert len(mod.parents) > 0
    args = mod.get_class_args()
    assert len(args) == 0
    parent_args = mod.get_parents_class_args()
    assert len(parent_args) > 0
