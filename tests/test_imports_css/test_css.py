# coding: utf-8
import pytest
if __name__ == "__main__":
    # import os
    # import sys
    # sys.path.append(os.path.realpath('..'))
    pytest.main([__file__])
from tests.import_check import ImportCheck


@pytest.fixture(scope='session')
def module_data(modules):
    return modules


def test_imp_mod(module_data: str):
    imc = ImportCheck()
    assert imc.load_import(module_data) == True
