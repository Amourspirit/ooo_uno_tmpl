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
# Namespace: com.sun.star.task
from typing_extensions import Literal
from .x_interaction_continuation import XInteractionContinuation as XInteractionContinuation_5af0108e

class XInteractionPassword(XInteractionContinuation_5af0108e):
    """
    A continuation to get a password from interaction helper.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XInteractionPassword <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XInteractionPassword.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.task.XInteractionPassword']

    def getPassword(self) -> str:
        """
        Get result password from the continuation.
        """
        ...
    def setPassword(self, aPasswd: str) -> None:
        """
        Store result password to the continuation.
        """
        ...


