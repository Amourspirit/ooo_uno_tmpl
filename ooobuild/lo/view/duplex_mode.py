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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.view


class DuplexMode(object):
    """
    Const Class

    These constants specify available duplex modes.

    See Also:
        `API DuplexMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1view_1_1DuplexMode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.view'
    __ooo_full_ns__: str = 'com.sun.star.view.DuplexMode'
    __ooo_type_name__: str = 'const'

    UNKNOWN = 0
    """
    specifies an unknown duplex mode.
    """
    OFF = 1
    """
    specifies that there is no duplex mode enabled
    """
    LONGEDGE = 2
    """
    specifies a long edge duplex mode
    """
    SHORTEDGE = 3
    """
    specifies a short edge duplex mode
    """

__all__ = ['DuplexMode']
