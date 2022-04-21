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
from .x_package import XPackage as XPackage_cb1f0c4d

class VersionException(Exception_85530a09):
    """
    Exception Class

    describes version clashes of a deployment unit.
    
    This exception is intended to be used with an com.sun.star.task.XInteractionHandler.
    
    **since**
    
        OOo 2.1

    See Also:
        `API VersionException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1deployment_1_1VersionException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.deployment'
    __ooo_full_ns__: str = 'com.sun.star.deployment.VersionException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.deployment.VersionException'
    __pyunostruct__: str = 'com.sun.star.deployment.VersionException'

    typeName: str = 'com.sun.star.deployment.VersionException'
    """Literal Constant ``com.sun.star.deployment.VersionException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, NewVersion: typing.Optional[str] = '', NewDisplayName: typing.Optional[str] = '', Deployed: typing.Optional[XPackage_cb1f0c4d] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            NewVersion (str, optional): NewVersion value.
            NewDisplayName (str, optional): NewDisplayName value.
            Deployed (XPackage, optional): Deployed value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "NewVersion": NewVersion,
            "NewDisplayName": NewDisplayName,
            "Deployed": Deployed,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._new_version = kwargs["NewVersion"]
        self._new_display_name = kwargs["NewDisplayName"]
        self._deployed = kwargs["Deployed"]
        inst_keys = ('NewVersion', 'NewDisplayName', 'Deployed')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def NewVersion(self) -> str:
        """
        the version of the extension which is being installed.
        """
        return self._new_version
    
    @NewVersion.setter
    def NewVersion(self, value: str) -> None:
        self._new_version = value

    @property
    def NewDisplayName(self) -> str:
        """
        the display name of the extension which is being installed.
        """
        return self._new_display_name
    
    @NewDisplayName.setter
    def NewDisplayName(self, value: str) -> None:
        self._new_display_name = value

    @property
    def Deployed(self) -> XPackage_cb1f0c4d:
        """
        represents the already installed version of the deployment unit.
        
        Must not be NULL.
        """
        return self._deployed
    
    @Deployed.setter
    def Deployed(self, value: XPackage_cb1f0c4d) -> None:
        self._deployed = value


__all__ = ['VersionException']

