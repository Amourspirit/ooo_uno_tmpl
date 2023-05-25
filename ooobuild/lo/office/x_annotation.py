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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.office
from __future__ import annotations
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from ..geometry.real_point2_d import RealPoint2D as RealPoint2D_d6e70c78
    from ..geometry.real_size2_d import RealSize2D as RealSize2D_ca1a0c09
    from ..text.x_text import XText as XText_690408ca
    from ..util.date_time import DateTime as DateTime_84de09d3

class XAnnotation(XPropertySet_bc180bfa, XComponent_98dc0ab5):
    """
    This interface gives access to an annotation inside a document.

    See Also:
        `API XAnnotation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1office_1_1XAnnotation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.office'
    __ooo_full_ns__: str = 'com.sun.star.office.XAnnotation'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.office.XAnnotation'

    @abstractproperty
    def Anchor(self) -> object:
        """
        a reference to the document content this annotation is anchored to.
        """
        ...

    @abstractproperty
    def Author(self) -> str:
        """
        stores the full name of the author who created this annotation.
        """
        ...

    @abstractproperty
    def DateTime(self) -> DateTime_84de09d3:
        """
        stores the date and time this annotation was last edited.
        """
        ...

    @abstractproperty
    def Initials(self) -> str:
        """
        stores the initials of the author who created this annotation.
        """
        ...

    @abstractproperty
    def Position(self) -> RealPoint2D_d6e70c78:
        """
        this is an optional position that gives the user interface a hint where the annotation should be rendered.
        
        This could be an offset to the annotations anchor.
        """
        ...

    @abstractproperty
    def Size(self) -> RealSize2D_ca1a0c09:
        """
        this is an optional size that gives the user interface a hint how large the annotation should be rendered.
        """
        ...

    @abstractproperty
    def TextRange(self) -> XText_690408ca:
        """
        gives access to the annotations text.
        """
        ...


__all__ = ['XAnnotation']


