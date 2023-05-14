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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.inspection
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class PropertyCategoryDescriptor(object):
    """
    Struct Class

    describes a category of properties
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API PropertyCategoryDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1inspection_1_1PropertyCategoryDescriptor.html>`_
    """
    typeName: Literal['com.sun.star.inspection.PropertyCategoryDescriptor']

    def __init__(self, ProgrammaticName: typing.Optional[str] = ..., UIName: typing.Optional[str] = ..., HelpURL: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            ProgrammaticName (str, optional): ProgrammaticName value.
            UIName (str, optional): UIName value.
            HelpURL (str, optional): HelpURL value.
        """
        ...


    @property
    def ProgrammaticName(self) -> str:
        """
        contains the programmatic name of the category.
        
        This programmatic name is used internally: XPropertyHandler.describePropertyLine() sets a programmatic category name at LineDescriptor.Category, and an object inspector uses this to find the proper PropertyCategoryDescriptor.
        """
        ...

    @ProgrammaticName.setter
    def ProgrammaticName(self, value: str) -> None:
        ...

    @property
    def UIName(self) -> str:
        """
        provides a human-readable name (which can be presented at the UI) for a category.
        """
        ...

    @UIName.setter
    def UIName(self, value: str) -> None:
        ...

    @property
    def HelpURL(self) -> str:
        """
        provides a help URL to be associated with a category
        """
        ...

    @HelpURL.setter
    def HelpURL(self, value: str) -> None:
        ...

