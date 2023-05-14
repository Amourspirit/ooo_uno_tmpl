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
# Namespace: com.sun.star.accessibility
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43


class AccessibleRelation(object):
    """
    Struct Class

    An AccessibleRelation object defines a one-to-many relation.
    
    The represented relation points from the implementing object to a set of target objects.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleRelation <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1accessibility_1_1AccessibleRelation.html>`_
    """
    typeName: Literal['com.sun.star.accessibility.AccessibleRelation']

    def __init__(self, TargetSet: typing.Optional[typing.Tuple[XInterface_8f010a43, ...]] = ..., RelationType: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            TargetSet (typing.Tuple[XInterface, ...], optional): TargetSet value.
            RelationType (int, optional): RelationType value.
        """
        ...


    @property
    def TargetSet(self) -> typing.Tuple[XInterface_8f010a43, ...]:
        """
        Set of objects that are the relation's targets.
        
        The content of this set is undefined if the relation's type is INVALID. The set must not contain references to one object more than once.
        """
        ...

    @TargetSet.setter
    def TargetSet(self, value: typing.Tuple[XInterface_8f010a43, ...]) -> None:
        ...

    @property
    def RelationType(self) -> int:
        """
        Type of the relation.
        
        Its value has to be one of the constants defined by AccessibleRelationType. If that value is INVALID then the whole relation is regarded as invalid. The content of the TargetSet is then undefined.
        """
        ...

    @RelationType.setter
    def RelationType(self, value: int) -> None:
        ...

