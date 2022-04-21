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
# Libre Office Version: 7.2
# Namespace: com.sun.star.frame
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.frame import FrameSearchFlag as FrameSearchFlag
    if hasattr(FrameSearchFlag, '_constants') and isinstance(FrameSearchFlag._constants, dict):
        FrameSearchFlag._constants['__ooo_ns__'] = 'com.sun.star.frame'
        FrameSearchFlag._constants['__ooo_full_ns__'] = 'com.sun.star.frame.FrameSearchFlag'
        FrameSearchFlag._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global FrameSearchFlagEnum
        ls = [f for f in dir(FrameSearchFlag) if not callable(getattr(FrameSearchFlag, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(FrameSearchFlag, name)
        FrameSearchFlagEnum = IntEnum('FrameSearchFlagEnum', _dict)
    build_enum()
else:
    from ...lo.frame.frame_search_flag import FrameSearchFlag as FrameSearchFlag

    class FrameSearchFlagEnum(IntEnum):
        """
        Enum of Const Class FrameSearchFlag

        these types describe the algorithm to be used to search a frame
        
        Such flags will be used on methods XFrame.findFrame(), XDispatchProvider.queryDispatch() or XComponentLoader.loadComponentFromURL() if no special target frame name (e.g. \"_blank\", \"_self\") is used.
        """
        AUTO = FrameSearchFlag.AUTO
        """
        no longer supported
        
        Using of this flag will do nothing. Use right combination of other flags instead of this one.
        """
        PARENT = FrameSearchFlag.PARENT
        """
        allows search on the parent frames
        """
        SELF = FrameSearchFlag.SELF
        """
        includes the start frame himself
        """
        CHILDREN = FrameSearchFlag.CHILDREN
        """
        includes all child frames of the start frame
        
        Note: That means all direct children and of course her children too. Search doesn't stop at the next level inside the tree!
        """
        CREATE = FrameSearchFlag.CREATE
        """
        frame will be created if not found
        """
        SIBLINGS = FrameSearchFlag.SIBLINGS
        """
        includes the direct siblings of the start frame
        
        Normally it's interpreted as search on the direct children of the parent only. But in combination with e.g. the CHILDREN flag it can include all children of it too.
        """
        TASKS = FrameSearchFlag.TASKS
        """
        allow the search outside the current sub task tree of the whole possible frame tree
        
        If this flag isn't present, any search from bottom to top has to stop, if a top frame will be reached. It doesn't influence a search from top to bottom. But it can be used at the root of the frame tree to search on direct children of it only. Because the direct children of the root node are the root's of the task sub trees, which are top frames too. Instead of using the CHILDREN flag there, it's possible so to suppress a deeper search so.
        """
        ALL = FrameSearchFlag.ALL
        """
        includes all frames except frames in other tasks sub trees but doesn't create any new frame
        """
        GLOBAL = FrameSearchFlag.GLOBAL
        """
        searches in the whole hierarchy of frames but doesn't create any new frame
        """

__all__ = ['FrameSearchFlag', 'FrameSearchFlagEnum']
