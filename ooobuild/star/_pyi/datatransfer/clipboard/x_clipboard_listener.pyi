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
# Namespace: com.sun.star.datatransfer.clipboard
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .clipboard_event import ClipboardEvent as ClipboardEvent_ed2e1377


class XClipboardListener(XEventListener_c7230c4a):
    """
    Interface to be implemented to receive notifications on clipboard content changes.

    See Also:
        `API XClipboardListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1clipboard_1_1XClipboardListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.datatransfer.clipboard.XClipboardListener']

    def changedContents(self, event: 'ClipboardEvent_ed2e1377') -> None:
        """
        The content of the clipboard has changed.
        """
        ...


