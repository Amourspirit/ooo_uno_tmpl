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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.frame
# Libre Office Version: 2024.2
import typing
from ..util.url import URL as URL_57ad07b9


class DispatchDescriptor(object):
    """
    Struct Class

    describes a feature to be retrieved by a URL that has to be loaded into a specified frame
    
    For a normal dispatch calls all needed parameters are separated. For optimized remote functionality XDispatch.queryDispatches() it's necessary to pack these parameters in a flat structure which can be used in a simple manner.

    See Also:
        `API DispatchDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1DispatchDescriptor.html>`_
    """
    typeName: str = 'com.sun.star.frame.DispatchDescriptor'

    def __init__(self, FeatureURL: typing.Optional[URL_57ad07b9] = ..., FrameName: typing.Optional[str] = ..., SearchFlags: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            FeatureURL (URL, optional): FeatureURL value.
            FrameName (str, optional): FrameName value.
            SearchFlags (int, optional): SearchFlags value.
        """
        ...

    @property
    def FeatureURL(self) -> URL_57ad07b9:
        """
        specifies the URL of the resource/function
        
        Must be a full parsed URL. Use service com.sun.star.util.URLTransformer for that.
        """
        ...
    @FeatureURL.setter
    def FeatureURL(self, value: URL_57ad07b9) -> None:
        ...
    @property
    def FrameName(self) -> str:
        """
        name of the target frame
        
        Special targets (e.g. \"_blank\", \"_self\") or really existing target names can be used.
        """
        ...
    @FrameName.setter
    def FrameName(self, value: str) -> None:
        ...
    @property
    def SearchFlags(self) -> int:
        """
        describes how the target frame is to be searched
        
        This optional parameter is used if FrameName isn't a special target only.
        """
        ...
    @SearchFlags.setter
    def SearchFlags(self, value: int) -> None:
        ...

