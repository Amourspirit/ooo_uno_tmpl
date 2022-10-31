# coding: utf-8
from typing import Tuple
import pytest
if __name__ == "__main__":
    # import os
    # import sys
    # sys.path.append(os.path.realpath('..'))
    pytest.main([__file__])
from tests.import_check import ImportCheck


@pytest.fixture(scope='session')
def enum_data(module_types):
    lst = module_types["enum"]
    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        results.append(name)
    return results


@pytest.fixture(scope='session')
def const_data(module_types):
    lst = module_types["const"]
    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        results.append(name)
    return results


@pytest.fixture(scope='session')
def ex_data(module_types):
    lst = module_types["exception"]
    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        results.append(name)
    return results


@pytest.fixture(scope='session')
def struct_data(module_types):
    lst = module_types["struct"]
    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        results.append(name)
    return results


@pytest.fixture(scope='session')
def interface_data(module_types):
    lst = module_types["interface"]
    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        results.append(name)
    return results


def test_imp_enum(enum_data: str, monkeypatch):
    monkeypatch.setenv('ooouno_ignore_runtime', 'False')
    imc = ImportCheck()
    assert imc.load_import(enum_data, True) == True


def test_imp_ex(ex_data: str, monkeypatch):
    monkeypatch.setenv('ooouno_ignore_runtime', 'False')
    imc = ImportCheck()
    assert imc.load_import(ex_data, True) == True


def test_imp_const(const_data: str, monkeypatch):
    monkeypatch.setenv('ooouno_ignore_runtime', 'False')
    imc = ImportCheck()
    assert imc.load_import(const_data, True) == True


def test_imp_struct(struct_data: str,dyn_struct_generic: Tuple[str, ...], monkeypatch):
    if struct_data in dyn_struct_generic:
        return
    monkeypatch.setenv('ooouno_ignore_runtime', 'False')
    imc = ImportCheck()
    assert imc.load_import(struct_data, True) == True


def test_imp_interface(interface_data: str, monkeypatch):
    monkeypatch.setenv('ooouno_ignore_runtime', 'False')
    imc = ImportCheck()
    assert imc.load_import(interface_data, True) == True
