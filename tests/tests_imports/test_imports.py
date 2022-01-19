# coding: utf-8
import pytest
if __name__ == "__main__":
    # import os
    # import sys
    # sys.path.append(os.path.realpath('..'))
    pytest.main([__file__])
from tests.tests_imports.import_check import ImportCheck


@pytest.fixture(scope='session')
def singlton_data(module_types):
    lst = module_types["singleton"]
    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        results.append(name)
    return results


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
def typedef_data(module_types):
    lst = module_types["typedef"]
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
def test_imp_singleton(singlton_data: str):
    # https://github.com/pytest-dev/pytest/issues/6374
    imc = ImportCheck()
    assert imc.load_import(singlton_data) == True


def test_imp_enum(enum_data: str):
    imc = ImportCheck()
    assert imc.load_import(enum_data) == True


def test_imp_const(const_data: str):
    imc = ImportCheck()
    assert imc.load_import(const_data) == True


def test_imp_ex(ex_data: str):
    imc = ImportCheck()
    assert imc.load_import(ex_data) == True


def test_imp_typedef(typedef_data: str):
    imc = ImportCheck()
    assert imc.load_import(typedef_data) == True


def test_imp_struct(struct_data: str):
    imc = ImportCheck()
    assert imc.load_import(struct_data) == True
