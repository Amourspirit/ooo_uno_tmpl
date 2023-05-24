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
# Namespace: com.sun.star.io
from __future__ import annotations
import typing

from .x_active_data_sink import XActiveDataSink as XActiveDataSink_b8d00ba3
from .x_text_input_stream import XTextInputStream as XTextInputStream_c7ae0c59


class XTextInputStream2(XActiveDataSink_b8d00ba3, XTextInputStream_c7ae0c59):
    """
    Provides a unified interface for the new-style service TextInputStream.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XTextInputStream2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XTextInputStream2.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.io.XTextInputStream2'


