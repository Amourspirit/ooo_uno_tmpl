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
# Namespace: com.sun.star.frame


class FrameSearchFlag(object):
    """
    Const Class

    these types describe the algorithm to be used to search a frame
    
    Such flags will be used on methods XFrame.findFrame(), XDispatchProvider.queryDispatch() or XComponentLoader.loadComponentFromURL() if no special target frame name (e.g. \"_blank\", \"_self\") is used.

    See Also:
        `API FrameSearchFlag <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1frame_1_1FrameSearchFlag.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.FrameSearchFlag'
    __ooo_type_name__: str = 'const'

    AUTO = 0
    """
    no longer supported
    
    Using of this flag will do nothing. Use right combination of other flags instead of this one.
    """
    PARENT = 1
    """
    allows search on the parent frames
    """
    SELF = 2
    """
    includes the start frame himself
    """
    CHILDREN = 4
    """
    includes all child frames of the start frame
    
    Note: That means all direct children and of course her children too. Search doesn't stop at the next level inside the tree!
    """
    CREATE = 8
    """
    frame will be created if not found
    """
    SIBLINGS = 16
    """
    includes the direct siblings of the start frame
    
    Normally it's interpreted as search on the direct children of the parent only. But in combination with e.g. the CHILDREN flag it can include all children of it too.
    """
    TASKS = 32
    """
    allow the search outside the current sub task tree of the whole possible frame tree
    
    If this flag isn't present, any search from bottom to top has to stop, if a top frame will be reached. It doesn't influence a search from top to bottom. But it can be used at the root of the frame tree to search on direct children of it only. Because the direct children of the root node are the root's of the task sub trees, which are top frames too. Instead of using the CHILDREN flag there, it's possible so to suppress a deeper search so.
    """
    ALL = 23
    """
    includes all frames except frames in other tasks sub trees but doesn't create any new frame
    """
    GLOBAL = 55
    """
    searches in the whole hierarchy of frames but doesn't create any new frame
    """

__all__ = ['FrameSearchFlag']
