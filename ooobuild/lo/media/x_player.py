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
# Namespace: com.sun.star.media
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from .x_frame_grabber import XFrameGrabber as XFrameGrabber_c56f0c00
    from .x_player_window import XPlayerWindow as XPlayerWindow_c7130c45

class XPlayer(ABC):
    """
    is the multimedia stream handling interface.
    
    This allows to perform every basic operation on videos and sounds.

    See Also:
        `API XPlayer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1media_1_1XPlayer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.media'
    __ooo_full_ns__: str = 'com.sun.star.media.XPlayer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.media.XPlayer'

    @abstractmethod
    def createFrameGrabber(self) -> XFrameGrabber_c56f0c00:
        """
        gets a frame grabber for this stream.
        """
        ...
    @abstractmethod
    def createPlayerWindow(self, aArguments: typing.Tuple[object, ...]) -> XPlayerWindow_c7130c45:
        """
        gets a new player window for this stream control
        """
        ...
    @abstractmethod
    def getDuration(self) -> float:
        """
        gets the stream length
        """
        ...
    @abstractmethod
    def getMediaTime(self) -> float:
        """
        gets the current position of the cursor in the stream
        """
        ...
    @abstractmethod
    def getPreferredPlayerWindowSize(self) -> Size_576707ef:
        """
        gets the preferred window size
        """
        ...
    @abstractmethod
    def getVolumeDB(self) -> int:
        """
        gets the current audio volume in decibel
        """
        ...
    @abstractmethod
    def isMute(self) -> bool:
        """
        gets whether the volume is temporarily down to 0 or not.
        """
        ...
    @abstractmethod
    def isPlaybackLoop(self) -> bool:
        """
        indicates whether the stream reading will restart after the end of the stream.
        """
        ...
    @abstractmethod
    def isPlaying(self) -> bool:
        """
        indicates whether the stream is played or not.
        """
        ...
    @abstractmethod
    def setMediaTime(self, fTime: float) -> None:
        """
        sets the new cursor position in the media stream.
        
        After using this method the stream is stopped.
        """
        ...
    @abstractmethod
    def setMute(self, bSet: bool) -> None:
        """
        sets the volume to 0 or to its previous value.
        """
        ...
    @abstractmethod
    def setPlaybackLoop(self, bSet: bool) -> None:
        """
        sets whether the stream reading should restart at the stream start after the end of the stream.
        """
        ...
    @abstractmethod
    def setVolumeDB(self, nDB: int) -> None:
        """
        sets the audio volume in decibel.
        """
        ...
    @abstractmethod
    def start(self) -> None:
        """
        starts reading the stream from the current position.
        """
        ...
    @abstractmethod
    def stop(self) -> None:
        """
        stops reading the stream and leave the cursor at its current position.
        """
        ...

__all__ = ['XPlayer']

