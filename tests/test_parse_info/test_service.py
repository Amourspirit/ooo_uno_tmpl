import pytest
from pathlib import Path
import json
if __name__ == "__main__":
    pytest.main([__file__])



@pytest.fixture(scope="session")
def fixture_uno_control_combo_box_model(fixture_json_path: Path) -> Path:
    return fixture_json_path / 'service' / 'UnoControlComboBoxModel.json'

def _test_open_root(fixture_uno_control_combo_box_model):
    from src.parse_info.ooo_service.ooo_service import OooService
    with open(fixture_uno_control_combo_box_model, 'r') as f:
        f_json = json.load(f)
    serv = OooService(**f_json)
    assert serv is not None
    assert serv.id == 'uno-ooo-parser'


def test_service_writer_args():
    from src.parse_info.ooo_service.writer_args import WriterArgs
    data = {"include_desc": True}
    args = WriterArgs(**data)
    assert args.include_desc == True


def test_service_parser_args():
    from src.parse_info.ooo_service.parser_args import ParserArgs
    data = {
        "sort": True,
        "long_names": True,
        "remove_parent_inherited" : True
        }
    args = ParserArgs(**data)
    assert args.sort == True
    assert args.long_names == True
    assert args.remove_parent_inherited == True
