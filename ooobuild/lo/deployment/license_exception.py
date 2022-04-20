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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.deployment
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class LicenseException(Exception_85530a09):
    """
    Exception Class

    A LicenseException reflects the necessity of someone agreeing to a license.
    
    **since**
    
        OOo 2.0.4

    See Also:
        `API LicenseException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1deployment_1_1LicenseException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.deployment'
    __ooo_full_ns__: str = 'com.sun.star.deployment.LicenseException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.deployment.LicenseException'
    __pyunostruct__: str = 'com.sun.star.deployment.LicenseException'

    typeName: str = 'com.sun.star.deployment.LicenseException'
    """Literal Constant ``com.sun.star.deployment.LicenseException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, ExtensionName: typing.Optional[str] = '', Text: typing.Optional[str] = '', AcceptBy: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            ExtensionName (str, optional): ExtensionName value.
            Text (str, optional): Text value.
            AcceptBy (str, optional): AcceptBy value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "ExtensionName": ExtensionName,
            "Text": Text,
            "AcceptBy": AcceptBy,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._extension_name = kwargs["ExtensionName"]
        self._text = kwargs["Text"]
        self._accept_by = kwargs["AcceptBy"]
        inst_keys = ('ExtensionName', 'Text', 'AcceptBy')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def ExtensionName(self) -> str:
        """
        name of the extension.
        
        The display name of the extension. See XPackage.getDisplayName()
        """
        return self._extension_name
    
    @ExtensionName.setter
    def ExtensionName(self, value: str) -> None:
        self._extension_name = value

    @property
    def Text(self) -> str:
        """
        contains the text of the license.
        """
        return self._text
    
    @Text.setter
    def Text(self, value: str) -> None:
        self._text = value

    @property
    def AcceptBy(self) -> str:
        """
        contains the value of the attribute /description/registration/simple-license/@accept-by from the description.xml
        """
        return self._accept_by
    
    @AcceptBy.setter
    def AcceptBy(self, value: str) -> None:
        self._accept_by = value


__all__ = ['LicenseException']

