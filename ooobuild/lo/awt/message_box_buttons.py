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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.awt


class MessageBoxButtons(object):
    """
    Const Class

    defines constants for the possible message box button combinations.

    See Also:
        `API MessageBoxButtons <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1MessageBoxButtons.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.MessageBoxButtons'
    __ooo_type_name__: str = 'const'

    BUTTONS_OK = 1
    """
    specifies a message with \"OK\" button.
    """
    BUTTONS_OK_CANCEL = 2
    """
    specifies a message box with \"OK\" and \"CANCEL\" button.
    """
    BUTTONS_YES_NO = 3
    """
    specifies a message box with \"YES\" and \"NO\" button.
    """
    BUTTONS_YES_NO_CANCEL = 4
    """
    specifies a message box with \"YES\", \"NO\" and \"CANCEL\" button.
    """
    BUTTONS_RETRY_CANCEL = 5
    """
    specifies a message box with \"RETRY\" and \"CANCEL\" button.
    """
    BUTTONS_ABORT_IGNORE_RETRY = 6
    """
    specifies a message box with \"ABORT\", \"IGNORE\" and \"RETRY\" button.
    """
    DEFAULT_BUTTON_OK = 65536
    """
    specifies that OK is the default button.
    """
    DEFAULT_BUTTON_CANCEL = 131072
    """
    specifies that CANCEL is the default button.
    """
    DEFAULT_BUTTON_RETRY = 196608
    """
    specifies that RETRY is the default button.
    """
    DEFAULT_BUTTON_YES = 262144
    """
    specifies that YES is the default button.
    """
    DEFAULT_BUTTON_NO = 327680
    """
    specifies that NO is the default button.
    """
    DEFAULT_BUTTON_IGNORE = 393216
    """
    specifies that IGNORE is the default button.
    """

__all__ = ['MessageBoxButtons']