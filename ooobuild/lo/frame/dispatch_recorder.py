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
# Libre Office Version: 7.4
# Namespace: com.sun.star.frame
from .x_dispatch_recorder import XDispatchRecorder as XDispatchRecorder_fbd70dd1

class DispatchRecorder(XDispatchRecorder_fbd70dd1):
    """
    Service Class

    provides functionality to record XDispatch.dispatch() requests
    
    It records all necessary parameters of a call XDispatch.dispatch() and generate code which can be executed at later time to run same operations again. Which code will be generated depends from real implementation. So it's possible to generate e.g. Java/Basic or may Perl code. By using of a DispatchRecorderSupplier, which is available on a property of a Frame.DispatchRecorderSupplier, it's possible to change such code generation for further requests or disable it in general by setting this property to NULL.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API DispatchRecorder <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1DispatchRecorder.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.DispatchRecorder'
    __ooo_type_name__: str = 'service'



__all__ = ['DispatchRecorder']

