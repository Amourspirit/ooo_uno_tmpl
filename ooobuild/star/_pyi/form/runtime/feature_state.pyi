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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.form.runtime
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class FeatureState(object):
    """
    Struct Class

    encapsulates the state of a FormFeature
    
    **since**
    
        OOo 2.2

    See Also:
        `API FeatureState <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1form_1_1runtime_1_1FeatureState.html>`_
    """
    typeName: Literal['com.sun.star.form.runtime.FeatureState']

    def __init__(self, Enabled: typing.Optional[bool] = ..., State: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Enabled (bool, optional): Enabled value.
            State (object, optional): State value.
        """
        ...


    @property
    def Enabled(self) -> bool:
        """
        determines whether the respective feature is enabled (i.e.
        
        available) in the current state of the form.
        """
        ...

    @Enabled.setter
    def Enabled(self, value: bool) -> None:
        ...

    @property
    def State(self) -> object:
        """
        determines the state of the feature.
        
        The concrete semantics depends on the concrete FormFeature.
        """
        ...

    @State.setter
    def State(self, value: object) -> None:
        ...

