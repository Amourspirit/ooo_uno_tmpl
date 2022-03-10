# coding: utf-8
import pytest
if __name__ == "__main__":
    # import os
    # import sys
    # sys.path.append(os.path.realpath('..'))
    pytest.main([__file__])
from tests.import_check import ImportCheck

def test_single():
    # from ooobuild.lo.document.filter_options_request import FilterOptionsRequest
    ns = "ooobuild.lo.document.filter_options_request.FilterOptionsRequest"
    imc = ImportCheck()
    assert imc.load_import(ns) == True
