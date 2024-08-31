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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.inspection
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
from .x_property_control import XPropertyControl as XPropertyControl_3f260fe2


class LineDescriptor(object):
    """
    Struct Class

    describes the appearance of a line representing a single property in an ObjectInspector.
    
    Such a line consists of
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API LineDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1inspection_1_1LineDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.inspection'
    __ooo_full_ns__: str = 'com.sun.star.inspection.LineDescriptor'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.inspection.LineDescriptor'
    """Literal Constant ``com.sun.star.inspection.LineDescriptor``"""

    def __init__(self, DisplayName: typing.Optional[str] = '', Control: typing.Optional[XPropertyControl_3f260fe2] = None, HelpURL: typing.Optional[str] = '', HasPrimaryButton: typing.Optional[bool] = False, PrimaryButtonId: typing.Optional[str] = '', PrimaryButtonImageURL: typing.Optional[str] = '', PrimaryButtonImage: typing.Optional[XGraphic_a4da0afc] = None, HasSecondaryButton: typing.Optional[bool] = False, SecondaryButtonId: typing.Optional[str] = '', SecondaryButtonImageURL: typing.Optional[str] = '', SecondaryButtonImage: typing.Optional[XGraphic_a4da0afc] = None, IndentLevel: typing.Optional[int] = 0, Category: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            DisplayName (str, optional): DisplayName value.
            Control (XPropertyControl, optional): Control value.
            HelpURL (str, optional): HelpURL value.
            HasPrimaryButton (bool, optional): HasPrimaryButton value.
            PrimaryButtonId (str, optional): PrimaryButtonId value.
            PrimaryButtonImageURL (str, optional): PrimaryButtonImageURL value.
            PrimaryButtonImage (XGraphic, optional): PrimaryButtonImage value.
            HasSecondaryButton (bool, optional): HasSecondaryButton value.
            SecondaryButtonId (str, optional): SecondaryButtonId value.
            SecondaryButtonImageURL (str, optional): SecondaryButtonImageURL value.
            SecondaryButtonImage (XGraphic, optional): SecondaryButtonImage value.
            IndentLevel (int, optional): IndentLevel value.
            Category (str, optional): Category value.
        """
        super().__init__()

        if isinstance(DisplayName, LineDescriptor):
            oth: LineDescriptor = DisplayName
            self.DisplayName = oth.DisplayName
            self.Control = oth.Control
            self.HelpURL = oth.HelpURL
            self.HasPrimaryButton = oth.HasPrimaryButton
            self.PrimaryButtonId = oth.PrimaryButtonId
            self.PrimaryButtonImageURL = oth.PrimaryButtonImageURL
            self.PrimaryButtonImage = oth.PrimaryButtonImage
            self.HasSecondaryButton = oth.HasSecondaryButton
            self.SecondaryButtonId = oth.SecondaryButtonId
            self.SecondaryButtonImageURL = oth.SecondaryButtonImageURL
            self.SecondaryButtonImage = oth.SecondaryButtonImage
            self.IndentLevel = oth.IndentLevel
            self.Category = oth.Category
            return

        kargs = {
            "DisplayName": DisplayName,
            "Control": Control,
            "HelpURL": HelpURL,
            "HasPrimaryButton": HasPrimaryButton,
            "PrimaryButtonId": PrimaryButtonId,
            "PrimaryButtonImageURL": PrimaryButtonImageURL,
            "PrimaryButtonImage": PrimaryButtonImage,
            "HasSecondaryButton": HasSecondaryButton,
            "SecondaryButtonId": SecondaryButtonId,
            "SecondaryButtonImageURL": SecondaryButtonImageURL,
            "SecondaryButtonImage": SecondaryButtonImage,
            "IndentLevel": IndentLevel,
            "Category": Category,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._display_name = kwargs["DisplayName"]
        self._control = kwargs["Control"]
        self._help_url = kwargs["HelpURL"]
        self._has_primary_button = kwargs["HasPrimaryButton"]
        self._primary_button_id = kwargs["PrimaryButtonId"]
        self._primary_button_image_url = kwargs["PrimaryButtonImageURL"]
        self._primary_button_image = kwargs["PrimaryButtonImage"]
        self._has_secondary_button = kwargs["HasSecondaryButton"]
        self._secondary_button_id = kwargs["SecondaryButtonId"]
        self._secondary_button_image_url = kwargs["SecondaryButtonImageURL"]
        self._secondary_button_image = kwargs["SecondaryButtonImage"]
        self._indent_level = kwargs["IndentLevel"]
        self._category = kwargs["Category"]


    @property
    def DisplayName(self) -> str:
        """
        denotes the human-readable display name used to present a property to the user
        """
        return self._display_name

    @DisplayName.setter
    def DisplayName(self, value: str) -> None:
        self._display_name = value

    @property
    def Control(self) -> XPropertyControl_3f260fe2:
        """
        denotes the control which should be used to represent the property at the UI.
        """
        return self._control

    @Control.setter
    def Control(self, value: XPropertyControl_3f260fe2) -> None:
        self._control = value

    @property
    def HelpURL(self) -> str:
        """
        specifies the URL to the help topic to be associated with the property
        """
        return self._help_url

    @HelpURL.setter
    def HelpURL(self, value: str) -> None:
        self._help_url = value

    @property
    def HasPrimaryButton(self) -> bool:
        """
        determines whether a button exists which can be used for a more complex, interactive property value input.
        
        If no image for the primary button is specified, but a primary button is present, the three dots will be displayed on the button.
        """
        return self._has_primary_button

    @HasPrimaryButton.setter
    def HasPrimaryButton(self, value: bool) -> None:
        self._has_primary_button = value

    @property
    def PrimaryButtonId(self) -> str:
        """
        describes a unique id to associate with the primary button
        
        In OpenOffice.org, UI elements sometimes require a so-called UniqueID, which can be used to uniquely (within the whole application) identify this UI element. For instance, automating the OpenOffice.org UI via a dedicated separate application (\"TestTool\") requires such IDs.
        
        If a primary button exists for a property's UI representation (HasPrimaryButton), it gets the ID specified herein.
        """
        return self._primary_button_id

    @PrimaryButtonId.setter
    def PrimaryButtonId(self, value: str) -> None:
        self._primary_button_id = value

    @property
    def PrimaryButtonImageURL(self) -> str:
        """
        describes the URL of an image to display on the primary button, if any.
        
        This URL will be used to obtain an actual com.sun.star.graphic.XGraphic object from a com.sun.star.graphic.GraphicProvider.
        
        The property will be ignored if HasPrimaryButton is FALSE.
        
        If you need to specify a graphic which does not have a URL, but is available as com.sun.star.graphic.XGraphic only, then you must leave PrimaryButtonImageURL empty, and use the PrimaryButtonImage property.
        """
        return self._primary_button_image_url

    @PrimaryButtonImageURL.setter
    def PrimaryButtonImageURL(self, value: str) -> None:
        self._primary_button_image_url = value

    @property
    def PrimaryButtonImage(self) -> XGraphic_a4da0afc:
        """
        describes a graphics to display at the primary button, if any.
        
        The property will be ignored if HasPrimaryButton is FALSE, or if PrimaryButtonImageURL is a non-empty string.
        """
        return self._primary_button_image

    @PrimaryButtonImage.setter
    def PrimaryButtonImage(self, value: XGraphic_a4da0afc) -> None:
        self._primary_button_image = value

    @property
    def HasSecondaryButton(self) -> bool:
        """
        determines whether a secondary button exists which can be used for a more complex, interactive property value input.
        
        A secondary button subordinated to the primary button. If no primary button exists (HasPrimaryButton), this member is ignored.
        """
        return self._has_secondary_button

    @HasSecondaryButton.setter
    def HasSecondaryButton(self, value: bool) -> None:
        self._has_secondary_button = value

    @property
    def SecondaryButtonId(self) -> str:
        """
        describes a unique id to associate with the primary button
        
        If a secondary button exists for a property's UI representation (HasSecondaryButton), it gets the ID specified herein.
        """
        return self._secondary_button_id

    @SecondaryButtonId.setter
    def SecondaryButtonId(self, value: str) -> None:
        self._secondary_button_id = value

    @property
    def SecondaryButtonImageURL(self) -> str:
        """
        describes the URL of an image to display on the secondary button, if any.
        
        This URL will be used to obtain an actual com.sun.star.graphic.XGraphic object from a com.sun.star.graphic.GraphicProvider.
        
        The property will be ignored if HasSecondaryButton is FALSE.
        
        If you need to specify a graphic which does not have a URL, but is available as com.sun.star.graphic.XGraphic only, then you must leave SecondaryButtonImageURL empty, and use the SecondaryButtonImage property.
        """
        return self._secondary_button_image_url

    @SecondaryButtonImageURL.setter
    def SecondaryButtonImageURL(self, value: str) -> None:
        self._secondary_button_image_url = value

    @property
    def SecondaryButtonImage(self) -> XGraphic_a4da0afc:
        """
        describes a graphics to display at the secondary button, if any.
        
        The property will be ignored if HasSecondaryButton is FALSE, or if SecondaryButtonImageURL is a non-empty string.
        """
        return self._secondary_button_image

    @SecondaryButtonImage.setter
    def SecondaryButtonImage(self, value: XGraphic_a4da0afc) -> None:
        self._secondary_button_image = value

    @property
    def IndentLevel(self) -> int:
        """
        describes the indent level for the property
        
        If a given property semantically depends on another one, the indent level can be used to visually represent this fact. For this, the dependent property's indent level would be one larger than the indent level of the other property.
        
        Normally, XPropertyHandlers will set this to 0 when describing the UI for a normal property.
        """
        return self._indent_level

    @IndentLevel.setter
    def IndentLevel(self, value: int) -> None:
        self._indent_level = value

    @property
    def Category(self) -> str:
        """
        describes the category into which the property should be sorted by the ObjectInspector.
        
        An ObjectInspector can visually group properties which semantically belong together (for instance using tab pages). The decision which properties actually belong together is made using this Category attribute.
        
        For your implementation of XPropertyHandler, it's recommended that you document the programmatic names used for property categories. This way, your handler might be re-used in different contexts, where only the XObjectInspectorModel needs to provide consistent UI names for the categories.
        """
        return self._category

    @Category.setter
    def Category(self, value: str) -> None:
        self._category = value


__all__ = ['LineDescriptor']
