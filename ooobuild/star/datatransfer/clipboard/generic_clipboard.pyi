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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.datatransfer.clipboard
from __future__ import annotations
from .x_clipboard_ex import XClipboardEx as XClipboardEx_c626128a
from .x_clipboard_notifier import XClipboardNotifier as XClipboardNotifier_3e4e150d
from ...lang.x_component import XComponent as XComponent_98dc0ab5
from ...lang.x_initialization import XInitialization as XInitialization_d46c0cca

class GenericClipboard(XClipboardEx_c626128a, XClipboardNotifier_3e4e150d, XComponent_98dc0ab5, XInitialization_d46c0cca):
    """
    Service Class

    A generic clipboard service is a simple container for transferable objects.

    See Also:
        `API GenericClipboard <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1datatransfer_1_1clipboard_1_1GenericClipboard.html>`_
    """
    ...

