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
# Libre Office Version: 7.3
# Namespace: com.sun.star.frame
from .x_dispatch_recorder_supplier import XDispatchRecorderSupplier as XDispatchRecorderSupplier_79301125

class DispatchRecorderSupplier(XDispatchRecorderSupplier_79301125):
    """
    Service Class

    provides a DispatchRecorder
    
    This supplier regulate macro recording of XDispatch.dispatch() calls. For that it encapsulates a reference to a DispatchRecorder. Such recorder is used internally and can be used externally too. A supplier will be available on a Frame if recording was enabled, otherwise not. A frame supports a special property for that. This modular concept of recorder, supplier and frame makes it possible to implement local recording on one frame; global recording by using all currently opened frames or only some of them; and so on.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API DispatchRecorderSupplier <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1DispatchRecorderSupplier.html>`_
    """


