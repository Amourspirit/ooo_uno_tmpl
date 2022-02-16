# coding: utf-8
import os
import sys
from tests.mod_types import get_module_types

sys.path.append(os.path.realpath('.'))


MODULE_TYPES = get_module_types()

def pytest_generate_tests(metafunc):
    if metafunc.function.__name__ == "test_imp_singleton" and "singlton_data" in dir(metafunc.module):
        metafunc.parametrize(
            "singlton_data", metafunc.module.singlton_data.__wrapped__(
                MODULE_TYPES))
    elif metafunc.function.__name__ == "test_imp_enum" and "enum_data" in dir(metafunc.module):
        metafunc.parametrize(
            "enum_data", metafunc.module.enum_data.__wrapped__(
                MODULE_TYPES))
    elif metafunc.function.__name__ == "test_imp_const" and "const_data" in dir(metafunc.module):
        metafunc.parametrize(
            "const_data", metafunc.module.const_data.__wrapped__(
                MODULE_TYPES))
    elif metafunc.function.__name__ == "test_imp_ex" and "ex_data" in dir(metafunc.module):
        metafunc.parametrize(
            "ex_data", metafunc.module.ex_data.__wrapped__(
                MODULE_TYPES))
    elif metafunc.function.__name__ == "test_imp_typedef" and "typedef_data" in dir(metafunc.module):
        metafunc.parametrize(
            "typedef_data", metafunc.module.typedef_data.__wrapped__(
                MODULE_TYPES))
    elif metafunc.function.__name__ == "test_imp_struct" and "struct_data" in dir(metafunc.module):
        metafunc.parametrize(
            "struct_data", metafunc.module.struct_data.__wrapped__(
                MODULE_TYPES))
    elif metafunc.function.__name__ == "test_imp_interface" and "interface_data" in dir(metafunc.module):
        metafunc.parametrize(
            "interface_data", metafunc.module.interface_data.__wrapped__(
                MODULE_TYPES))
    elif metafunc.function.__name__ == "test_imp_service" and "service_data" in dir(metafunc.module):
        metafunc.parametrize(
            "service_data", metafunc.module.service_data.__wrapped__(
                MODULE_TYPES))
