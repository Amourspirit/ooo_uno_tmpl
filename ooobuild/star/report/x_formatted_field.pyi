# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.report
from __future__ import annotations
import typing

from .x_report_control_model import XReportControlModel as XReportControlModel_2d800f4a
if typing.TYPE_CHECKING:
    from ..util.x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier_3afb0fb7


class XFormattedField(XReportControlModel_2d800f4a):
    """
    describes a control which can be used for displaying values with an arbitrary formatting.

    See Also:
        `API XFormattedField <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XFormattedField.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.report.XFormattedField'

    @property
    def FormatKey(self) -> int:
        """
        specifies the format to be used when formatting the field input and output.
        
        This value is meaningful relative to the FormatsSupplier attribute only.
        """
        ...
    @FormatKey.setter
    def FormatKey(self, value: int) -> None:
        ...
    @property
    def FormatsSupplier(self) -> XNumberFormatsSupplier_3afb0fb7:
        """
        supplies the formats the field should work with.
        """
        ...
    @FormatsSupplier.setter
    def FormatsSupplier(self, value: XNumberFormatsSupplier_3afb0fb7) -> None:
        ...

