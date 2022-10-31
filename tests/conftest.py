# coding: utf-8
import pytest
import logging
from pathlib import Path


@pytest.fixture(scope="session")
def fixture_path(app_root: Path) -> Path:
    return app_root / "tests" / "fixture"


@pytest.fixture(scope="session")
def test_log():
    log = get_logger("test", log_file="test.log", log_level=logging.DEBUG, add_handler_file=False)
    return log


@pytest.fixture(scope="session")
def fixture_json_path(fixture_path: Path) -> Path:
    return fixture_path / "json"


@pytest.fixture(scope="session")
def dyn_struct_generic():
    return (
        "ooobuild.dyn.beans.ambiguous.Ambiguous",
        "ooobuild.dyn.beans.defaulted.Defaulted",
        "ooobuild.dyn.beans.optional.Optional",
        "ooobuild.dyn.beans.pair.Pair",
    )


from src.logger.log_handle import get_logger
