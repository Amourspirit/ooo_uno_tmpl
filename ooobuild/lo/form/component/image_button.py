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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.form.component
import typing
from abc import abstractproperty
from ...awt.uno_control_image_control_model import UnoControlImageControlModel as UnoControlImageControlModel_7b36111c
from ..form_control_model import FormControlModel as FormControlModel_e2990d22
from ..x_image_producer_supplier import XImageProducerSupplier as XImageProducerSupplier_37df0f8f
if typing.TYPE_CHECKING:
    from ..form_button_type import FormButtonType as FormButtonType_c92d0c6e

class ImageButton(UnoControlImageControlModel_7b36111c, FormControlModel_e2990d22, XImageProducerSupplier_37df0f8f):
    """
    Service Class

    This service specifies the control model for a clickable button which is represented by an image.
    
    The image to be displayed is determined by com.sun.star.awt.UnoControlImageControlModel.ImageURL property specifies the URL of an image to be displayed.

    See Also:
        `API ImageButton <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1ImageButton.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.ImageButton'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ButtonType(self) -> 'FormButtonType_c92d0c6e':
        """
        describes the action to be executed by the button when pressed.
        """
        ...

    @abstractproperty
    def TargetFrame(self) -> str:
        """
        describes the frame, where to open the document specified by the TargetURL.
        
        This property is evaluated if the button is of type URL.
        
        As always, there is a number of target names which have a special meaning, and force a special com.sun.star.frame.Frame to be used.
        """
        ...

    @abstractproperty
    def TargetURL(self) -> str:
        """
        specifies the URL, which should be opened if the button was clicked.
        
        This property is evaluated if the button is of type URL.
        """
        ...


__all__ = ['ImageButton']

