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
# Libre Office Version: 7.2
# Namespace: com.sun.star.presentation
import typing
from ..awt.x_window import XWindow as XWindow_713b0924
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..frame.controller import Controller as Controller_a5330b37
if typing.TYPE_CHECKING:
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9

class OutlineView(Controller_a5330b37, XWindow_713b0924, XPropertySet_bc180bfa):
    """
    Service Class

    This component integrates an outline view to a presentation document into the desktop.
    
    In an outline view, the textual contents of presentation text objects from all presentation pages are presented as a continuous outline text.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API OutlineView <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1presentation_1_1OutlineView.html>`_
    """
    @property
    def VisibleArea(self) -> 'Rectangle_84b109e9':
        """
        This is the area that is currently visible.
        """


