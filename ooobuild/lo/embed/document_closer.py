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
# Namespace: com.sun.star.embed
from __future__ import annotations
import typing
from abc import abstractmethod
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from ..frame.x_frame import XFrame as XFrame_7a570956

class DocumentCloser(XComponent_98dc0ab5):
    """
    Service Class

    The main task of this service is to close an office document frame embedded in an application running in another process correctly.
    
    The usual usage of this service is to create it, initialize with document frame, and to dispose the service. While disposing the service will do all the required actions to let the frame be closed using com.sun.star.util.XCloseable.close( true ). Thus in case there is a code that prevents closing of the frame the code automatically becomes the owner of the frame.
    
    In addition the code will disconnect the VCL window the frame is based on from the container system window.

    See Also:
        `API DocumentCloser <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1embed_1_1DocumentCloser.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.DocumentCloser'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def DocumentCloserCtor1(self, xFrame: XFrame_7a570956) -> None:
        """
        is used to initialize the object on it's creation.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.frame.DoubleInitializationException: ``DoubleInitializationException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['DocumentCloser']

