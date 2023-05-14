# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.report
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ReportPrintOption(metaclass=UnoConstMeta, type_name="com.sun.star.report.ReportPrintOption", name_space="com.sun.star.report"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.report.ReportPrintOption``"""
        pass

    class ReportPrintOptionEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.report.ReportPrintOption", name_space="com.sun.star.report"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.report.ReportPrintOption`` as Enum values"""
        pass

else:
    from ...lo.report.report_print_option import ReportPrintOption as ReportPrintOption

    class ReportPrintOptionEnum(IntEnum):
        """
        Enum of Const Class ReportPrintOption

        Specifies whether a page header or footer is printed on the same page as the report header or report footer.
        """
        ALL_PAGES = ReportPrintOption.ALL_PAGES
        """
        The page header/footer is printed on all pages.
        """
        NOT_WITH_REPORT_HEADER = ReportPrintOption.NOT_WITH_REPORT_HEADER
        """
        The page header/footer is not printed on the same page as the report header.
        """
        NOT_WITH_REPORT_FOOTER = ReportPrintOption.NOT_WITH_REPORT_FOOTER
        """
        The page header/footer is not printed on the same page as the report footer.
        """
        NOT_WITH_REPORT_HEADER_FOOTER = ReportPrintOption.NOT_WITH_REPORT_HEADER_FOOTER
        """
        The page header/footer is not printed on the same page as the report header or footer.
        """

__all__ = ['ReportPrintOption', 'ReportPrintOptionEnum']
