import pytest
from pathlib import Path
if __name__ == "__main__":
    pytest.main([__file__])


def test_open_command_argument2(root_path):
    from src.template_helper.models_struct import ModelsStruct
    p = 'lo/ucb/OpenCommandArgument2.json'
    mod = ModelsStruct(json_data=p)
    assert len(mod.parents) == 1
    args = mod.get_class_args()
    assert len(args) > 0
    arg = args[0]
    assert arg.name == "SortingInfo"
    assert arg.default == "UNO_NONE"
    assert arg.type == "typing.Tuple[NumberedSortingInfo_fd0e0de6, ...]"
    fi  = mod.get_full_imports()
    assert len(fi) > 0
