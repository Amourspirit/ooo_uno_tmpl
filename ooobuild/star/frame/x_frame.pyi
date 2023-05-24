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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924
    from .x_controller import XController as XController_b00e0b8f
    from .x_frame_action_listener import XFrameActionListener as XFrameActionListener_26250efa
    from .x_frames_supplier import XFramesSupplier as XFramesSupplier_e12a0d1d


class XFrame(XComponent_98dc0ab5):
    """
    a frame object can be considered to be an \"anchor\" object where a component can be attached to.
    
    A frame can be (it's not a must!) a part of a frame tree. If not this frame won't be accessible by using the API. This mode make sense for previews. The root node of the tree can be a Desktop implementation.

    See Also:
        `API XFrame <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XFrame.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XFrame'

    def activate(self) -> None:
        """
        activates this frame and thus the component within.
        
        At first the frame sets itself as the active frame of its creator by calling XFramesSupplier.setActiveFrame(), then it broadcasts a FrameActionEvent with FrameAction.FRAME_ACTIVATED. The component within this frame may listen to this event to grab the focus on activation; for simple components this can be done by the FrameLoader.
        
        Finally, most frames may grab the focus to one of its windows or forward the activation to a sub-frame.
        """
        ...
    def addFrameActionListener(self, xListener: XFrameActionListener_26250efa) -> None:
        """
        registers an event listener, which will be called when certain things happen to the components within this frame or within sub-frames of this frame.
        
        E.g., it is possible to determine instantiation/destruction and activation/deactivation of components.
        """
        ...
    def contextChanged(self) -> None:
        """
        notifies the frame that the context of the controller within this frame changed (i.e.
        
        the selection).
        
        According to a call to this interface, the frame calls XFrameActionListener.frameAction() with FrameAction.CONTEXT_CHANGED to all listeners which are registered using XFrame.addFrameActionListener(). For external controllers this event can be used to requery dispatches.
        """
        ...
    def deactivate(self) -> None:
        """
        is called by the creator frame when another sub-frame gets activated.
        
        At first the frame deactivates its active sub-frame, if any. Then broadcasts a FrameActionEvent with FrameAction.FRAME_DEACTIVATING.
        """
        ...
    def findFrame(self, aTargetFrameName: str, nSearchFlags: int) -> XFrame:
        """
        searches for a frame with the specified name.
        
        Frames may contain other frames (e.g., a frameset) and may be contained in other frames. This hierarchy is searched with this method. First some special names are taken into account, i.e. \"\", \"_self\", \"_top\", \"_blank\" etc. SearchFlags is ignored when comparing these names with TargetFrameName; further steps are controlled by SearchFlags. If allowed, the name of the frame itself is compared with the desired one, and then ( again if allowed ) the method is called for all children of the frame. Finally may be called for the siblings and then for parent frame (if allowed).
        
        List of special target names:
        
        If no frame with the given name is found, a new top frame is created; if this is allowed by a special flag FrameSearchFlag.CREATE. The new frame also gets the desired name.
        """
        ...
    def getComponentWindow(self) -> XWindow_713b0924:
        """
        provides access to the component window
        
        Note: Don't dispose this window - the frame is the owner of it.
        """
        ...
    def getContainerWindow(self) -> XWindow_713b0924:
        """
        provides access to the container window of the frame.
        
        Normally this is used as the parent window of the component window.
        """
        ...
    def getController(self) -> XController_b00e0b8f:
        """
        provides access to the controller
        
        Note: Don't dispose it - the frame is the owner of it. Use XController.getFrame() to dispose the frame after you the controller agreed with a XController.suspend() call.
        """
        ...
    def getCreator(self) -> XFramesSupplier_e12a0d1d:
        """
        provides access to the creator (parent) of this frame
        """
        ...
    def getName(self) -> str:
        """
        access to the name property of this frame
        """
        ...
    def initialize(self, xWindow: XWindow_713b0924) -> None:
        """
        is called to initialize the frame within a window - the container window.
        
        This window will be used as parent for the component window and to support some UI relevant features of the frame service. Note: Re-parenting mustn't supported by a real frame implementation! It's designed for initializing - not for setting.
        
        This frame will take over ownership of the window referred from xWindow. Thus, the previous owner is not allowed to dispose this window anymore.
        """
        ...
    def isActive(self) -> bool:
        """
        determines if the frame is active.
        """
        ...
    def isTop(self) -> bool:
        """
        determines if the frame is a top frame.
        
        In general a top frame is the frame which is a direct child of a task frame or which does not have a parent. Possible frame searches must stop the search at such a frame unless the flag FrameSearchFlag.TASKS is set.
        """
        ...
    def removeFrameActionListener(self, xListener: XFrameActionListener_26250efa) -> None:
        """
        unregisters an event listener
        """
        ...
    def setComponent(self, xComponentWindow: XWindow_713b0924, xController: XController_b00e0b8f) -> bool:
        """
        sets a new component into the frame or release an existing one from a frame.
        
        A valid component window should be a child of the frame container window.
        
        Simple components may implement a com.sun.star.awt.XWindow only. In this case no controller must be given here.
        """
        ...
    def setCreator(self, Creator: XFramesSupplier_e12a0d1d) -> None:
        """
        sets the frame container that created this frame.
        
        Only the creator is allowed to call this method. But creator doesn't mean the implementation which creates this instance ... it means the parent frame of the frame hierarchy. Because; normally a frame should be created by using the API and is necessary for searches inside the tree (e.g. XFrame.findFrame())
        """
        ...
    def setName(self, aName: str) -> None:
        """
        sets the name of the frame.
        
        Normally the name of the frame is set initially (e.g. by the creator). The name of a frame will be used for identifying it if a frame search was started. These searches can be forced by:
        
        Note: Special targets like \"_blank\", \"_self\" etc. are not allowed. That's why frame names shouldn't start with a sign \"_\".
        """
        ...


