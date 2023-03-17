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
# Libre Office Version: 7.4
# Namespace: com.sun.star.deployment
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from .x_package import XPackage as XPackage_cb1f0c4d
    from .x_package_type_info import XPackageTypeInfo as XPackageTypeInfo_3bc70f7b
    from ..ucb.x_command_environment import XCommandEnvironment as XCommandEnvironment_fb330dee

class XPackageRegistry(ABC):
    """
    Interface to bind a UNO package.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XPackageRegistry <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1deployment_1_1XPackageRegistry.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.deployment.XPackageRegistry']

    def bindPackage(self, url: str, mediaType: str, removed: bool, identifier: str, xCmdEnv: 'XCommandEnvironment_fb330dee') -> 'XPackage_cb1f0c4d':
        """
        binds a package URL to a XPackage handle.
        
        The returned UNO package handle ought to late-initialize itself, thus the process of binding must not be an expensive operation, because it is not abortable.
        
        Calling the function several time with the same parameters must result in returning the same object.
        
        The file or folder at the location where url points to may not exist or it was replaced. This can happen, for example, when a bundled extension was removed by the setup and a user later starts OOo. Then the user data may still contain all registration data of that extension, but the actual extension files do not exist anymore. The registration data must then be cleaned of all the remains of that extension. To do that one creates an XPackage object on behalf of that extension and calls XPackage.revokePackage(). The parameter removed indicates this case. The returned object may not rely on the file or folder to which refers url. Instead it must use previously saved data to successfully carry out the revocation of this object (XPackage.revokePackage()).
        
        The implementation must ensure that there is only one instance of XPackage for the same url at any time. Therefore calling bindPackage() again with the same url but different mediaType (the exception is, if previously an empty string was provided to cause the determination of the media type) or removed parameters will cause an exception. A com.sun.star.lang.IllegalArgumentException will be thrown in case of a different mediaType parameter and a InvalidRemovedParameterException is thrown if the removed parameter is different.
        
        The identifier parameter must be provided when removed = true. If not, then an com.sun.star.lang.IllegalArgumentException will be thrown.

        Raises:
            DeploymentException: ``DeploymentException``
            InvalidRemovedParameterException: ``InvalidRemovedParameterException``
            com.sun.star.ucb.CommandFailedException: ``CommandFailedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getSupportedPackageTypes(self) -> 'typing.Tuple[XPackageTypeInfo_3bc70f7b, ...]':
        """
        gets the supported XPackageTypeInfos.
        """
        ...
    def packageRemoved(self, url: str, mediaType: str) -> None:
        """

        Raises:
            DeploymentException: ``DeploymentException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


