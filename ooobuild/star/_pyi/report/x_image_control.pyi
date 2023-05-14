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
# Namespace: com.sun.star.report
from typing_extensions import Literal
from ..form.x_image_producer_supplier import XImageProducerSupplier as XImageProducerSupplier_37df0f8f
from .x_report_control_model import XReportControlModel as XReportControlModel_2d800f4a

class XImageControl(XImageProducerSupplier_37df0f8f, XReportControlModel_2d800f4a):
    """
    
    **since**
    
        OOo 3.2

    See Also:
        `API XImageControl <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XImageControl.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.report.XImageControl']

    @property
    def ImageURL(self) -> str:
        """
        specifies a URL to an image to use for the control.
        """
        ...
    @ImageURL.setter
    def ImageURL(self, value: str) -> None:
        ...
    @property
    def PreserveIRI(self) -> bool:
        """
        Specifies that the IRI given in the data field should be preserved, otherwise the content will be inserted in the resulting report document.
        
        If the data field contains something different as string then this attribute will be ignored.
        """
        ...
    @PreserveIRI.setter
    def PreserveIRI(self, value: bool) -> None:
        ...
    @property
    def ScaleMode(self) -> int:
        """
        defines how to scale the image
        
        If this property is present, it supersedes the ScaleImage property.
        
        The value of this property is one of the com.sun.star.awt.ImageScaleMode constants.
        
        **since**
        
            OOo 3.2
        """
        ...
    @ScaleMode.setter
    def ScaleMode(self, value: int) -> None:
        ...

