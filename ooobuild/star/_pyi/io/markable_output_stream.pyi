# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.io
from .x_active_data_source import XActiveDataSource as XActiveDataSource_d1900c7f
from .x_connectable import XConnectable as XConnectable_980a0a96
from .x_markable_stream import XMarkableStream as XMarkableStream_b9bc0bc3
from .x_output_stream import XOutputStream as XOutputStream_a4e00b35

class MarkableOutputStream(XActiveDataSource_d1900c7f, XConnectable_980a0a96, XMarkableStream_b9bc0bc3, XOutputStream_a4e00b35):
    """
    Service Class

    allows to set marks in an outputstream and to later jump back to these marks.
    
    The implementation stores the data as long as marks exists and later writes these data into the output stream, that has been set previously at the XActiveDataSource interface.

    See Also:
        `API MarkableOutputStream <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1io_1_1MarkableOutputStream.html>`_
    """


