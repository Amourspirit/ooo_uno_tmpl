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
# Namespace: com.sun.star.logging


class LogLevel(object):
    """
    Const Class

    specifies levels to distinguish between severities of logged events
    
    **since**
    
        OOo 2.3

    See Also:
        `API LogLevel <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1logging_1_1LogLevel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.logging'
    __ooo_full_ns__: str = 'com.sun.star.logging.LogLevel'
    __ooo_type_name__: str = 'const'

    OFF = 2147483647
    """
    specifies that no messages are to be logged at all
    
    This level can be set at an XLogger to completely prevent logging. You will usually not use it with a concrete log event.
    """
    SEVERE = 1000
    """
    denotes a serious failure to be logged
    """
    WARNING = 900
    """
    denotes a potential problem to be logged
    """
    INFO = 800
    """
    denotes an informational message to be logged
    """
    CONFIG = 700
    """
    denotes a static configuration message to be logged
    """
    FINE = 500
    """
    denotes basic tracing information to be logged
    """
    FINER = 400
    """
    denotes more fine-grained tracing information to be logged
    """
    FINEST = 300
    """
    denotes highly detailed tracing information to be logged
    """
    ALL = -2147483648
    """
    specifies that all messages should be logged
    
    This level can be set at an XLogger to enable logging of absolutely all events. You will usually not use it with a concrete log event.
    """

__all__ = ['LogLevel']