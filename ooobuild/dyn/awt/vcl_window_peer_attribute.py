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
# Namespace: com.sun.star.awt
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.awt import VclWindowPeerAttribute as VclWindowPeerAttribute
    if hasattr(VclWindowPeerAttribute, '_constants') and isinstance(VclWindowPeerAttribute._constants, dict):
        VclWindowPeerAttribute._constants['__ooo_ns__'] = 'com.sun.star.awt'
        VclWindowPeerAttribute._constants['__ooo_full_ns__'] = 'com.sun.star.awt.VclWindowPeerAttribute'
        VclWindowPeerAttribute._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global VclWindowPeerAttributeEnum
        ls = [f for f in dir(VclWindowPeerAttribute) if not callable(getattr(VclWindowPeerAttribute, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(VclWindowPeerAttribute, name)
        VclWindowPeerAttributeEnum = IntEnum('VclWindowPeerAttributeEnum', _dict)
    build_enum()
else:
    from ...lo.awt.vcl_window_peer_attribute import VclWindowPeerAttribute as VclWindowPeerAttribute

    class VclWindowPeerAttributeEnum(IntEnum):
        """
        Enum of Const Class VclWindowPeerAttribute

        specifies attributes for the VCL window implementation.
        
        IMPORTANT: These constants have to be disjunct with constants in WindowAttribute.
        
        .. deprecated::
        
            Class is deprecated.
        """
        HSCROLL = VclWindowPeerAttribute.HSCROLL
        VSCROLL = VclWindowPeerAttribute.VSCROLL
        LEFT = VclWindowPeerAttribute.LEFT
        CENTER = VclWindowPeerAttribute.CENTER
        RIGHT = VclWindowPeerAttribute.RIGHT
        SPIN = VclWindowPeerAttribute.SPIN
        SORT = VclWindowPeerAttribute.SORT
        DROPDOWN = VclWindowPeerAttribute.DROPDOWN
        DEFBUTTON = VclWindowPeerAttribute.DEFBUTTON
        READONLY = VclWindowPeerAttribute.READONLY
        CLIPCHILDREN = VclWindowPeerAttribute.CLIPCHILDREN
        NOBORDER = VclWindowPeerAttribute.NOBORDER
        GROUP = VclWindowPeerAttribute.GROUP
        OK = VclWindowPeerAttribute.OK
        OK_CANCEL = VclWindowPeerAttribute.OK_CANCEL
        YES_NO = VclWindowPeerAttribute.YES_NO
        YES_NO_CANCEL = VclWindowPeerAttribute.YES_NO_CANCEL
        RETRY_CANCEL = VclWindowPeerAttribute.RETRY_CANCEL
        DEF_OK = VclWindowPeerAttribute.DEF_OK
        DEF_CANCEL = VclWindowPeerAttribute.DEF_CANCEL
        DEF_RETRY = VclWindowPeerAttribute.DEF_RETRY
        DEF_YES = VclWindowPeerAttribute.DEF_YES
        DEF_NO = VclWindowPeerAttribute.DEF_NO
        NOLABEL = VclWindowPeerAttribute.NOLABEL
        AUTOHSCROLL = VclWindowPeerAttribute.AUTOHSCROLL
        AUTOVSCROLL = VclWindowPeerAttribute.AUTOVSCROLL

__all__ = ['VclWindowPeerAttribute', 'VclWindowPeerAttributeEnum']