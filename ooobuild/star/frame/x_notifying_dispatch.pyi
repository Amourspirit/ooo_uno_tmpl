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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from .x_dispatch import XDispatch as XDispatch_98ff0a9b
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_dispatch_result_listener import XDispatchResultListener as XDispatchResultListener_582b1060
    from ..util.url import URL as URL_57ad07b9


class XNotifyingDispatch(XDispatch_98ff0a9b):
    """
    dispatch with guaranteed notify (instead of XDispatch)

    See Also:
        `API XNotifyingDispatch <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XNotifyingDispatch.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XNotifyingDispatch'

    def dispatchWithNotification(self, URL: URL_57ad07b9, Arguments: typing.Tuple[PropertyValue_c9610c73, ...], Listener: XDispatchResultListener_582b1060) -> None:
        """
        Do the same like XDispatch.dispatch() but notifies listener in every case.
        
        Should be used if result must be known.
        """
        ...


