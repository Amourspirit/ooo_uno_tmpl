# coding: utf-8
import pytest

if __name__ == "__main__":
    # import os
    # import sys
    # sys.path.append(os.path.realpath('..'))
    pytest.main([__file__])
from tests.import_check import ImportCheck


@pytest.fixture(scope="session")
def singlton_data(module_types):
    lst = module_types["singleton"]
    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        results.append(name)
    return results


@pytest.fixture(scope="session")
def enum_data(module_types):
    lst = module_types["enum"]
    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        results.append(name)
    return results


@pytest.fixture(scope="session")
def const_data(module_types):
    lst = module_types["const"]
    no_check = ("ooobuild.dyn.drawing.canvas_feature.CanvasFeature",)
    # com.sun.star.drawing.CanvasFeature contains a reserved keyword of python (None)
    # It can be imported com.sun.star.drawing import CanvasFeature
    # but trying to access CanvasFeature.None_ will result in a syntax error.
    # After import it is possible to access the value via the getattr(CanvasFeature, "None")
    # which as a value of 0
    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        if name in no_check:
            continue
        results.append(name)
    return results


@pytest.fixture(scope="session")
def ex_data(module_types):
    lst = module_types["exception"]
    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        results.append(name)
    return results


@pytest.fixture(scope="session")
def typedef_data(module_types):
    lst = module_types["typedef"]
    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        results.append(name)
    return results


@pytest.fixture(scope="session")
def struct_data(module_types):
    lst = module_types["struct"]
    results = []
    no_check = (
        "ooobuild.dyn.beans.defaulted.Defaulted",
        "ooobuild.dyn.beans.optional.Optional",
        "ooobuild.dyn.beans.pair.Pair",
        "ooobuild.dyn.beans.ambiguous.Ambiguous",
    )
    # Generally the above exclusion are not real import of uno. They are more like generics.
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        if name in no_check:
            continue
        results.append(name)
    return results


@pytest.fixture(scope="session")
def interface_data(module_types):
    lst = module_types["interface"]
    no_check = ("ooobuild.dyn.accessibility.x_accessible_state_set.XAccessibleStateSet",)
    # I created a bug report for this issue:
    # https://bugs.documentfoundation.org/show_bug.cgi?id=152476
    # Import stopped working in LibreOffice 7.5

    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        if name in no_check:
            continue
        results.append(name)
    return results


@pytest.fixture(scope="session")
def service_data(module_types):
    lst = module_types["service"]
    results = []
    for data in lst:
        name = f"{data['ns']}.{data['c_name']}.{data['name']}"
        results.append(name)
    return results


def test_imp_singleton(singlton_data: str, monkeypatch):
    monkeypatch.setenv("ooouno_ignore_runtime", "True")
    # https://github.com/pytest-dev/pytest/issues/6374
    imc = ImportCheck()
    assert imc.load_import(singlton_data, True) == True


def test_imp_enum(enum_data: str, monkeypatch):
    monkeypatch.setenv("ooouno_ignore_runtime", "True")
    imc = ImportCheck()
    assert imc.load_import(enum_data, True) == True


def test_imp_const(const_data: str, monkeypatch):
    monkeypatch.setenv("ooouno_ignore_runtime", "True")
    imc = ImportCheck()
    assert imc.load_import(const_data) == True
    const_enum = const_data + "Enum"
    assert imc.load_import(const_enum, True) == True


def test_imp_ex(ex_data: str, monkeypatch):
    monkeypatch.setenv("ooouno_ignore_runtime", "True")
    imc = ImportCheck()
    assert imc.load_import(ex_data, True) == True


def test_imp_typedef(typedef_data: str, monkeypatch):
    monkeypatch.setenv("ooouno_ignore_runtime", "True")
    imc = ImportCheck()
    assert imc.load_import(typedef_data, True) == True


def test_imp_struct(struct_data: str, monkeypatch):
    monkeypatch.setenv("ooouno_ignore_runtime", "True")
    imc = ImportCheck()
    assert imc.load_import(struct_data, True) == True


def test_imp_interface(interface_data: str, monkeypatch):
    monkeypatch.setenv("ooouno_ignore_runtime", "True")
    from typing import TYPE_CHECKING

    assert TYPE_CHECKING == False
    imc = ImportCheck()
    assert imc.load_import(interface_data, True) == True


def test_imp_service(service_data: str, monkeypatch):
    monkeypatch.setenv("ooouno_ignore_runtime", "True")
    imc = ImportCheck()
    assert imc.load_import(service_data, True) == True


def _test_generic():
    ns = "build.uno_obj.text.text_view_cursor.TextViewCursor"
    imc = ImportCheck()
    assert imc.load_import(ns, True) == True
