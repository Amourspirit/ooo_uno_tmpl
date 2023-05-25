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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.report.meta
from __future__ import annotations
import typing

from ...container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
from ...lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from .x_function_category import XFunctionCategory as XFunctionCategory_59e21055
    from .x_function_description import XFunctionDescription as XFunctionDescription_8d8d119b


class XFunctionManager(XIndexAccess_f0910d6d, XComponent_98dc0ab5):
    """
    identifies a XFunctionManager which allows to retrieve the meta data of all supported functions.

    See Also:
        `API XFunctionManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1meta_1_1XFunctionManager.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.report.meta.XFunctionManager'

    def getCategory(self, position: int) -> XFunctionCategory_59e21055:
        """
        same as getByIndex.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def getFunctionByName(self, name: str) -> XFunctionDescription_8d8d119b:
        """
        get the function description by name

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...



