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
# Namespace: com.sun.star.text
from .text_frame import TextFrame as TextFrame_90410a5d

class ChainedTextFrame(TextFrame_90410a5d):
    """
    Service Class

    extends a TextFrame which shares the same Text with other ChainedTextFrame instances that will make the text flow through the chained frames.
    
    The text flows in the next frame if there is no space left in the current frame.

    See Also:
        `API ChainedTextFrame <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1ChainedTextFrame.html>`_
    """
    @property
    def ChainNextName(self) -> str:
        """
        name of the previous frame in the chain
        
        An empty string indicates that there is no previous frame.
        """
        ...
    @ChainNextName.setter
    def ChainNextName(self, value: str) -> None:
        ...
    @property
    def ChainPrevName(self) -> str:
        """
        name of the next frame in the chain
        
        An empty string indicates that there is no next frame.
        """
        ...
    @ChainPrevName.setter
    def ChainPrevName(self, value: str) -> None:
        ...

