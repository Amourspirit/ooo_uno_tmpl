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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.java
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from ..uno.deployment_exception import DeploymentException as DeploymentException_ffd30e2a
from ..uno.x_interface import XInterface as XInterface_8f010a43

class JavaInitializationException(DeploymentException_ffd30e2a):
    """
    Exception Class

    indicates that there is no Java available
    
    It is presumed that Java is a vital part of an office installation. That is, if Java does work for some reason, it is not guaranteed that the office is functional. A JavaInitializationException is therefore caused by some misconfiguration of Java which is closer described by other exceptions in this namespace which inherit JavaInitializationException. These are:
    
    com.sun.star.java.JavaDisabledException com.sun.star.java.JavaNotConfiguredException com.sun.star.java.MissingJavaRuntimeException com.sun.star.java.JavaVMCreationFailureException
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API JavaInitializationException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1java_1_1JavaInitializationException.html>`_
    """

    typeName: Literal['com.sun.star.java.JavaInitializationException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
        """
        ...

__all__ = ['JavaInitializationException']

