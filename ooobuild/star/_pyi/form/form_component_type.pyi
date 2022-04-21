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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.form
from typing_extensions import Literal
"""
Const

These constants specify the class types used to identify a component.

See Also:
    `API FormComponentType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1form_1_1FormComponentType.html>`_
"""
CONTROL: Literal[1]
"""
This generic identifier is for controls which cannot be identified by another specific identifier.
"""
COMMANDBUTTON: Literal[2]
"""
specifies a control that is used to begin, interrupt, or end a process.
"""
RADIOBUTTON: Literal[3]
"""
specifies a control that acts like a radio button.

Grouped together, such radio buttons present a set of two or more mutually exclusive choices to the user.
"""
IMAGEBUTTON: Literal[4]
"""
specifies a control that displays an image that responds to mouse clicks.
"""
CHECKBOX: Literal[5]
"""
specifies a control that is used to check or uncheck to turn an option on or off.
"""
LISTBOX: Literal[6]
"""
specifies a control that displays a list from which the user can select one or more items.
"""
COMBOBOX: Literal[7]
"""
specifies a control that is used when a list box combined with a static text control or an edit control is needed.
"""
GROUPBOX: Literal[8]
"""
specifies a control that displays a frame around a group of controls with or without a caption.
"""
TEXTFIELD: Literal[9]
"""
specifies a control that is a text component that allows for the editing of a single line of text.
"""
FIXEDTEXT: Literal[10]
"""
specifies a control to display a fixed text, usually used to label other controls.
"""
GRIDCONTROL: Literal[11]
"""
is a table like control to display database data.
"""
FILECONTROL: Literal[12]
"""
specifies a control which can be used to enter text, extended by an (user-startable) file dialog to browse for files.
"""
HIDDENCONTROL: Literal[13]
"""
specifies a control that should not be visible.
"""
IMAGECONTROL: Literal[14]
"""
specifies a control to display an image.
"""
DATEFIELD: Literal[15]
"""
specifies a control to display and edit a date value.
"""
TIMEFIELD: Literal[16]
"""
specifies a control to display and edit a time value.
"""
NUMERICFIELD: Literal[17]
"""
specifies a field to display and edit a numeric value.
"""
CURRENCYFIELD: Literal[18]
"""
specifies a field to display and edit a currency value.
"""
PATTERNFIELD: Literal[19]
"""
specifies a control to display and edit a string according to a pattern.
"""
SCROLLBAR: Literal[20]
"""
specifies a control to display and edit, in the form of a scrollbar, a value from a continuous value range
"""
SPINBUTTON: Literal[21]
"""
specifies a control to edit, in the form of a spin field, a value from a continuous range of values
"""
NAVIGATIONBAR: Literal[22]
"""
specifies a control which provides controller functionality for the com.sun.star.form.component.DataForm it belongs to, such as functionality to navigate or filter this form.
"""

