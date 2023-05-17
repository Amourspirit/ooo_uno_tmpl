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
# Namespace: com.sun.star.frame
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .dispatch_descriptor import DispatchDescriptor as DispatchDescriptor_b280e62
    from .x_dispatch import XDispatch as XDispatch_98ff0a9b
    from ..util.url import URL as URL_57ad07b9


class XDispatchProvider(XInterface_8f010a43):
    """
    provides XDispatch interfaces for certain functions which are useful at the UI.

    See Also:
        `API XDispatchProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XDispatchProvider.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XDispatchProvider']

    def queryDispatch(self, URL: 'URL_57ad07b9', TargetFrameName: str, SearchFlags: int) -> 'XDispatch_98ff0a9b':
        """
        searches for an XDispatch for the specified URL within the specified target frame.
        """
        ...
    def queryDispatches(self, Requests: 'typing.Tuple[DispatchDescriptor_b280e62, ...]') -> 'typing.Tuple[XDispatch_98ff0a9b, ...]':
        """
        actually this method is redundant to XDispatchProvider.queryDispatch() to avoid multiple remote calls.
        
        It's not allowed to pack it - because every request must match to its real result. Means: don't delete NULL entries inside this list.
        """
        ...


