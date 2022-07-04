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
# Namespace: com.sun.star.awt
from abc import ABC

class UnoControlDialogElement(ABC):
    """
    Service Class

    specifies a set of properties to describe the model of an UnoControl which is embedded in a UnoControlDialogModel.

    See Also:
        `API UnoControlDialogElement <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlDialogElement.html>`_
    """
    @property
    def Height(self) -> int:
        """
        specifies the height of the control.
        """
        ...
    @property
    def Name(self) -> str:
        """
        specifies the name of the control.
        """
        ...
    @property
    def PositionX(self) -> str:
        """
        specifies the horizontal position of the control.
        """
        ...
    @property
    def PositionY(self) -> str:
        """
        specifies the vertical position of the control.
        """
        ...
    @property
    def Step(self) -> int:
        """
        specifies the step of the control.
        """
        ...
    @property
    def TabIndex(self) -> int:
        """
        specifies the tabindex of the control.
        """
        ...
    @property
    def Tag(self) -> str:
        """
        specifies the tag of the control.
        """
        ...
    @property
    def Width(self) -> int:
        """
        specifies the width of the control.
        """
        ...


