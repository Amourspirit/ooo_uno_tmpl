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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6

class XReferenceMarksSupplier(XInterface_8f010a43):
    """
    provides access to the reference marks within this context (i.e.
    
    document).
    
    A reference mark is used to refer to text positions in a text document.

    See Also:
        `API XReferenceMarksSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XReferenceMarksSupplier.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.text.XReferenceMarksSupplier']

    def getReferenceMarks(self) -> 'XNameAccess_e2ab0cf6':
        """
        """
        ...


