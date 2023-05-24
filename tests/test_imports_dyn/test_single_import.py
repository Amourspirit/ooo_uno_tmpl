# coding: utf-8
import pytest
if __name__ == "__main__":
    # import os
    # import sys
    # sys.path.append(os.path.realpath('..'))
    pytest.main([__file__])
from tests.import_check import ImportCheck

def test_single(monkeypatch):
    monkeypatch.setenv("ooouno_ignore_runtime", "True")
    # from ooobuild.lo.document.filter_options_request import FilterOptionsRequest
    # ns = "ooobuild.lo.document.filter_options_request.FilterOptionsRequest"
    # ooobuild/dyn/chart2/x_chart_type_template.py
    ns = "ooobuild.dyn.script.cannot_convert_exception.CannotConvertException"
    # ns = "ooobuild.dyn.chart2.x_chart_type.XChartType"
    # ns = "ooobuild.dyn.chart2.x_chart_type_template.XChartTypeTemplate"
    import uno
    imc = ImportCheck()
    assert imc.load_import(ns, True) == True
