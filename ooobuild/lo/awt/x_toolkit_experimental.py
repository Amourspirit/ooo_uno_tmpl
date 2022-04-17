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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from .x_toolkit3 import XToolkit3 as XToolkit3_84a409c5

class XToolkitExperimental(XToolkit3_84a409c5):
    """
    Work in progress, don't use unless you know what you are doing.
    
    **since**
    
        LibreOffice 6.0

    See Also:
        `API XToolkitExperimental <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XToolkitExperimental.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XToolkitExperimental'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XToolkitExperimental'

    @abstractmethod
    def getOpenGLBufferSwapCounter(self) -> int:
        """
        Get the number of OpenGL buffer swaps.
        """
    @abstractmethod
    def getRecordingAndClear(self) -> 'typing.Tuple[str, ...]':
        """
        Query time logs and clear recording.
        
        First line is the time of the recorded operations in seconds, next ones are the log lines. A log line contains the thread ID, time stamp, profile zone ID and \"start\" or \"stop\".
        
        **since**
        
            LibreOffice 6.0
        """
    @abstractmethod
    def pause(self, nMilliseconds: int) -> None:
        """
        Pause the main thread of LibreOffice for the requested amount of time.
        """
    @abstractmethod
    def processEventsToIdle(self) -> None:
        """
        Process all pending idle events.
        """
    @abstractmethod
    def setDeterministicScheduling(self, bDeterministicMode: bool) -> None:
        """
        Turn on or off deterministic scheduling (off is the default).
        """
    @abstractmethod
    def startRecording(self) -> None:
        """
        Start time logging.
        
        **since**
        
            LibreOffice 6.0
        """
    @abstractmethod
    def stopRecording(self) -> None:
        """
        Stop time logging.
        
        **since**
        
            LibreOffice 6.0
        """

__all__ = ['XToolkitExperimental']
