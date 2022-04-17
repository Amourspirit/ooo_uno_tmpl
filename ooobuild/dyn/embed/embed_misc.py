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
# Namespace: com.sun.star.embed
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.embed import EmbedMisc as EmbedMisc
    if hasattr(EmbedMisc, '_constants') and isinstance(EmbedMisc._constants, dict):
        EmbedMisc._constants['__ooo_ns__'] = 'com.sun.star.embed'
        EmbedMisc._constants['__ooo_full_ns__'] = 'com.sun.star.embed.EmbedMisc'
        EmbedMisc._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global EmbedMiscEnum
        ls = [f for f in dir(EmbedMisc) if not callable(getattr(EmbedMisc, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(EmbedMisc, name)
        EmbedMiscEnum = IntFlag('EmbedMiscEnum', _dict)
    build_enum()
else:
    from ...lo.embed.embed_misc import EmbedMisc as EmbedMisc

    class EmbedMiscEnum(IntFlag):
        """
        Enum of Const Class EmbedMisc

        The constant set contains flags describing miscellaneous characteristics of embedded objects.
        
        The constant values can be combined with \"or\" operation. The first 32 bits are reserved for MS values, they are added because this API is going to be used to embed MS OLE objects into OOo documents, so there should be a possibility to transfer all the possible MS flags to container. In case own specific values should be added those bits can not be used.
        """
        MS_EMBED_RECOMPOSEONRESIZE = EmbedMisc.MS_EMBED_RECOMPOSEONRESIZE
        """
        means that the object wish to regenerate view representation if it's view in the container is resized.
        """
        MS_EMBED_ONLYICONIC = EmbedMisc.MS_EMBED_ONLYICONIC
        """
        The object has no view representation except icon.
        """
        MS_EMBED_INSERTNOTREPLACE = EmbedMisc.MS_EMBED_INSERTNOTREPLACE
        """
        If the object is generated from a selection, the selection should not be removed, the object should be inserted beside the selection.
        """
        MS_EMBED_STATIC = EmbedMisc.MS_EMBED_STATIC
        """
        The object is a static object that contains only representation.
        """
        MS_EMBED_CANTLINKINSIDE = EmbedMisc.MS_EMBED_CANTLINKINSIDE
        MS_EMBED_CANLINKBYOLE1 = EmbedMisc.MS_EMBED_CANLINKBYOLE1
        MS_EMBED_ISLINKOBJECT = EmbedMisc.MS_EMBED_ISLINKOBJECT
        MS_EMBED_INSIDEOUT = EmbedMisc.MS_EMBED_INSIDEOUT
        MS_EMBED_ACTIVATEWHENVISIBLE = EmbedMisc.MS_EMBED_ACTIVATEWHENVISIBLE
        MS_EMBED_RENDERINGISDEVICEINDEPENDENT = EmbedMisc.MS_EMBED_RENDERINGISDEVICEINDEPENDENT
        MS_EMBED_INVISIBLEATRUNTIME = EmbedMisc.MS_EMBED_INVISIBLEATRUNTIME
        MS_EMBED_ALWAYSRUN = EmbedMisc.MS_EMBED_ALWAYSRUN
        MS_EMBED_ACTSLIKEBUTTON = EmbedMisc.MS_EMBED_ACTSLIKEBUTTON
        MS_EMBED_ACTSLIKELABEL = EmbedMisc.MS_EMBED_ACTSLIKELABEL
        MS_EMBED_NOUIACTIVATE = EmbedMisc.MS_EMBED_NOUIACTIVATE
        MS_EMBED_ALIGNABLE = EmbedMisc.MS_EMBED_ALIGNABLE
        MS_EMBED_SIMPLEFRAME = EmbedMisc.MS_EMBED_SIMPLEFRAME
        MS_EMBED_SETCLIENTSITEFIRST = EmbedMisc.MS_EMBED_SETCLIENTSITEFIRST
        MS_EMBED_IMEMODE = EmbedMisc.MS_EMBED_IMEMODE
        MS_EMBED_IGNOREACTIVATEWHENVISIBLE = EmbedMisc.MS_EMBED_IGNOREACTIVATEWHENVISIBLE
        MS_EMBED_WANTSTOMENUMERGE = EmbedMisc.MS_EMBED_WANTSTOMENUMERGE
        MS_EMBED_SUPPORTSMULTILEVELUNDO = EmbedMisc.MS_EMBED_SUPPORTSMULTILEVELUNDO
        EMBED_ACTIVATEIMMEDIATELY = EmbedMisc.EMBED_ACTIVATEIMMEDIATELY
        EMBED_NEVERRESIZE = EmbedMisc.EMBED_NEVERRESIZE
        EMBED_NEEDSSIZEONLOAD = EmbedMisc.EMBED_NEEDSSIZEONLOAD
        """
        The object needs the size to be provided from the container after it is loaded to function in optimal way.
        """

__all__ = ['EmbedMisc', 'EmbedMiscEnum']
