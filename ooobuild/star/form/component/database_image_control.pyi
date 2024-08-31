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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.form.component
from __future__ import annotations
from ...awt.uno_control_image_control_model import UnoControlImageControlModel as UnoControlImageControlModel_7b36111c
from ..data_aware_control_model import DataAwareControlModel as DataAwareControlModel_27110ef8
from ..x_image_producer_supplier import XImageProducerSupplier as XImageProducerSupplier_37df0f8f

class DatabaseImageControl(UnoControlImageControlModel_7b36111c, DataAwareControlModel_27110ef8, XImageProducerSupplier_37df0f8f):
    """
    Service Class

    specifies the model of a control used for displaying images stored in a database.
    
    As every com.sun.star.form.DataAwareControlModel, an image control can be bound to a database field. This means that for instance with every record change, the content of the database field is taken, interpreted as image, and displayed in the control.Unlike other more text-based controls, it does not interpret the content of the field as text or double, but as binary stream (see com.sun.star.sdb.XColumn.getBinaryStream()).
    
    Usually, an image control model can be bound to binary columns only, namely com.sun.star.sdbc.DataType.BINARY, com.sun.star.sdbc.DataType.VARBINARY, com.sun.star.sdbc.DataType.LONGVARBINARY, com.sun.star.sdbc.DataType.OTHER, com.sun.star.sdbc.DataType.LONGVARCHAR
    
    Note that besides taking the image to be displayed from the bound field, there is another option. The com.sun.star.awt.UnoControlImageControlModel.ImageURL property specifies the URL of an image to be displayed. If this property is changed from outside, the respective file is loaded and set as image source.
    
    In a usual data form, the scenario will be as follows:

    See Also:
        `API DatabaseImageControl <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1DatabaseImageControl.html>`_
    """
    @property
    def ReadOnly(self) -> bool:
        """
        indicates if it is possible to change the image being displayed.
        """
        ...
    @ReadOnly.setter
    def ReadOnly(self, value: bool) -> None:
        ...

