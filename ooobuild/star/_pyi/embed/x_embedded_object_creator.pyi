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
# Namespace: com.sun.star.embed
from typing_extensions import Literal
from .x_embed_object_creator import XEmbedObjectCreator as XEmbedObjectCreator_14880e61
from .x_embed_object_factory import XEmbedObjectFactory as XEmbedObjectFactory_14770e69
from .x_link_creator import XLinkCreator as XLinkCreator_b9b20bbb
from .x_link_factory import XLinkFactory as XLinkFactory_b9a10bc3

class XEmbeddedObjectCreator(XEmbedObjectCreator_14880e61, XEmbedObjectFactory_14770e69, XLinkCreator_b9b20bbb, XLinkFactory_b9a10bc3):
    """
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XEmbeddedObjectCreator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XEmbeddedObjectCreator.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.embed.XEmbeddedObjectCreator']


