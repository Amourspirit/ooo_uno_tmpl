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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.accessibility
import uno
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class AccessibleStateType(metaclass=UnoConstMeta, type_name="com.sun.star.accessibility.AccessibleStateType", name_space="com.sun.star.accessibility"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.accessibility.AccessibleStateType``"""
        pass

    class AccessibleStateTypeEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.accessibility.AccessibleStateType", name_space="com.sun.star.accessibility"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.accessibility.AccessibleStateType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.accessibility import AccessibleStateType as AccessibleStateType
    else:
        # keep document generators happy
        from ...lo.accessibility.accessible_state_type import AccessibleStateType as AccessibleStateType

    class AccessibleStateTypeEnum(IntFlag):
        """
        Enum of Const Class AccessibleStateType

        Collection of state types.
        
        This list of constants defines the available set of states that an object that implements XAccessibleContext can be in.
        
        The comments describing the states is taken verbatim from the Java Accessibility API 1.4 documentation.
        
        We are using constants instead of a more typesafe enum. The reason for this is that IDL enums may not be extended. Therefore, in order to include future extensions to the set of roles we have to use constants here.
        
        These states are giving values corresponding to the bits of a 64-bit value, since we OR them together to create bitsets to represent the combined state of an accessibility object .
        
        **since**
        
            OOo 1.1.2
        """
        INVALID = AccessibleStateType.INVALID
        """
        Indicates an invalid state.
        """
        ACTIVE = AccessibleStateType.ACTIVE
        """
        Indicates a window is currently the active window.
        """
        ARMED = AccessibleStateType.ARMED
        """
        Indicates that the object is armed.
        """
        BUSY = AccessibleStateType.BUSY
        """
        Indicates the current object is busy.
        """
        CHECKED = AccessibleStateType.CHECKED
        """
        Indicates this object is currently checked.
        """
        DEFUNC = AccessibleStateType.DEFUNC
        """
        User interface object corresponding to this object no longer exists.
        
        Indicates the user interface object corresponding to this object no longer exists.
        """
        EDITABLE = AccessibleStateType.EDITABLE
        """
        Indicates the user can change the contents of this object.
        """
        ENABLED = AccessibleStateType.ENABLED
        """
        Indicates this object is enabled.
        """
        EXPANDABLE = AccessibleStateType.EXPANDABLE
        """
        Indicates this object allows progressive disclosure of its children.
        """
        EXPANDED = AccessibleStateType.EXPANDED
        """
        Indicates this object is expanded.
        """
        FOCUSABLE = AccessibleStateType.FOCUSABLE
        """
        Object can accept the keyboard focus.
        
        Indicates this object can accept keyboard focus, which means all events resulting from typing on the keyboard will normally be passed to it when it has focus.
        """
        FOCUSED = AccessibleStateType.FOCUSED
        """
        Indicates this object currently has the keyboard focus.
        """
        HORIZONTAL = AccessibleStateType.HORIZONTAL
        """
        Indicates the orientation of this object is horizontal.
        """
        ICONIFIED = AccessibleStateType.ICONIFIED
        """
        Indicates this object is minimized and is represented only by an icon.
        """
        INDETERMINATE = AccessibleStateType.INDETERMINATE
        """
        Sometimes UI elements can have a state indeterminate.
        
        This can happen e.g. if a check box reflects the bold state of text in a text processor. When the current selection contains text which is bold and also text which is not bold, the state is indeterminate.
        """
        MANAGES_DESCENDANTS = AccessibleStateType.MANAGES_DESCENDANTS
        """
        Indicates the most (all) children are transient and it is not necessary to add listener to the children.
        
        Only the active descendant (given by the event) should be not transient to make it possible to add listener to this object and recognize changes in this object.
        
        The state is added to make a performance improvement. Now it is no longer necessary to iterate over all children to find out whether they are transient or not to decide whether to add listener or not. If there is an object with this state no one should iterate over the children to add listener. Only the active descendant should get listener if it is not transient.
        """
        MODAL = AccessibleStateType.MODAL
        """
        Object is modal.
        
        Indicates something must be done with this object before the user can interact with an object in a different window.
        """
        MULTI_LINE = AccessibleStateType.MULTI_LINE
        """
        Indicates this (text) object can contain multiple lines of text.
        """
        MULTI_SELECTABLE = AccessibleStateType.MULTI_SELECTABLE
        """
        More than one child may be selected at the same time.
        
        Indicates this object allows more than one of its children to be selected at the same time.
        """
        OPAQUE = AccessibleStateType.OPAQUE
        """
        Indicates this object paints every pixel within its rectangular region.
        """
        PRESSED = AccessibleStateType.PRESSED
        """
        Indicates this object is currently pressed.
        """
        RESIZABLE = AccessibleStateType.RESIZABLE
        """
        Indicates the size of this object is not fixed.
        """
        SELECTABLE = AccessibleStateType.SELECTABLE
        """
        Object is selectable.
        
        Indicates this object is the child of an object that allows its children to be selected, and that this child is one of those children that can be selected.
        """
        SELECTED = AccessibleStateType.SELECTED
        """
        Object is selected.
        
        Indicates this object is the child of an object that allows its children to be selected, and that this child is one of those children that has been selected.
        """
        SENSITIVE = AccessibleStateType.SENSITIVE
        """
        Indicates this object is sensitive.
        """
        SHOWING = AccessibleStateType.SHOWING
        """
        Object is displayed on the screen.
        
        An object has set the SHOWING state if itself and all of its parents have set the VISIBLE state and it lies at least partly inside the visible area of its parent. It is, though, not necessarily visible on the screen because it may be occluded by other objects.
        """
        SINGLE_LINE = AccessibleStateType.SINGLE_LINE
        """
        Indicates this (text) object can contain only a single line of text.
        """
        STALE = AccessibleStateType.STALE
        """
        Object information is stale and might not be up to date.
        
        Indicates that the information that is returned from this object might be out of sync with the application.
        """
        TRANSIENT = AccessibleStateType.TRANSIENT
        """
        Indicates this object is transient.
        """
        VERTICAL = AccessibleStateType.VERTICAL
        """
        Indicates the orientation of this object is vertical.
        """
        VISIBLE = AccessibleStateType.VISIBLE
        """
        Object wants to be displayed on the screen.
        
        A set VISIBLE state indicates that an object wants to be displayed on the screen. It is displayed, as indicated by a set SHOWING state, if all of its parents have also set the VISIBLE state and the object lies at least partly in the visible area of its parent.
        """
        MOVEABLE = AccessibleStateType.MOVEABLE
        """
        Indicates the position of the object is not fixed.
        """
        DEFAULT = AccessibleStateType.DEFAULT
        """
        Indicates the object is the default button in a window.
        """
        OFFSCREEN = AccessibleStateType.OFFSCREEN
        """
        Indicates the object is outside of the screen area.
        """
        COLLAPSE = AccessibleStateType.COLLAPSE
        """
        Indicates that the object is collapsed.
        """
        CHECKABLE = AccessibleStateType.CHECKABLE
        """
        Indicates this object is checkable, i.e.
        
        it has the potential to be checked. See also the CHECKED state.
        """

__all__ = ['AccessibleStateType', 'AccessibleStateTypeEnum']
