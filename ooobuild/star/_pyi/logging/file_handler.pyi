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
# Namespace: com.sun.star.logging
import typing
from .x_log_handler import XLogHandler as XLogHandler_c7f80c27
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3

class FileHandler(XLogHandler_c7f80c27):
    """
    Service Class

    specifies a component implementing a log handler whose output channel is a file.
    
    The handler will use the Encoding attribute of XLogHandler to determine how to encode strings before actually writing them to the output file.
    
    **since**
    
        OOo 2.3

    See Also:
        `API FileHandler <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1logging_1_1FileHandler.html>`_
    """
    def create(self, FileURL: str) -> None:
        """
        creates a log handler whose output is directed to a file given by URL.
        """
    def createWithSettings(self, Settings: 'typing.Tuple[NamedValue_a37a0af3, ...]') -> None:
        """
        creates an instance of the log handler, using generic settings
        
        The following settings are recognized and supported:
        
        Additionally, a setting name FileURL is recognized. It must be of type string, and denotes the file URL to which the handler's output should be directed.
        
        At least the URL argument must be present in the settings.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """


