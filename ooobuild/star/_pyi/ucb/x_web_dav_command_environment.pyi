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
# Libre Office Version: 7.2
# Namespace: com.sun.star.ucb
from typing_extensions import Literal
import typing
from .x_command_environment import XCommandEnvironment as XCommandEnvironment_fb330dee
if typing.TYPE_CHECKING:
    from ..beans.string_pair import StringPair as StringPair_a4bc0b14
    from .web_davhttp_method import WebDAVHTTPMethod as WebDAVHTTPMethod_cbd50bdc

class XWebDAVCommandEnvironment(XCommandEnvironment_fb330dee):
    """
    A command environment that can be used to deal with WebDAV/HTTP specific commands.

    See Also:
        `API XWebDAVCommandEnvironment <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XWebDAVCommandEnvironment.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ucb.XWebDAVCommandEnvironment']

    def getUserRequestHeaders(self, aURI: str, eMethod: 'WebDAVHTTPMethod_cbd50bdc') -> 'typing.Tuple[StringPair_a4bc0b14, ...]':
        """
        This method gets called while assembling a WebDAV/HTTP request.
        
        The returned headername-headervalue pairs will be appended to the list of request headers before the request is dispatched.
        """

